import asyncio
import os.path

import click

from fontTools.ttLib import TTFont
from fontTools.subset import Subsetter
from ftools.helper import read_json, get_font_family, get_filter_range, create_dir, woff2_compress, generate_css, \
    write_css

from ftools.cli import pass_environment


@click.command("css", short_help="Generate css file from a font file. like Google Fonts")
@click.option("-i", "--input", type=click.Path(exists=True, readable=True), required=True, help="font file path")
@click.option("-o", "--output", type=click.Path(), required=True, help="output file path")
@click.option("-f", "--family", default=None, help="css font family")
@click.option("-w", "--weight", default="normal", help="css font weight")
@click.option("-s", "--style", default="normal", help="css font style")
@click.option("-d", "--display", default="swap", help="css font display")
@click.option("-v", "--flavor", type=click.Choice(["woff", "woff2", "otf", "ttf"]), default=["ttf"], multiple=True,
              help="font types like woff2")
@pass_environment
def cli(ctx, input, output, family, weight, style, display, flavor):
    """
    实现类似 Google Fonts 的效果 \n
    i/input: 源字体文件的路径 \n
    o/output: 输出字体文件的路径，只支持目录 \n
    f/family: css 里面的 font-family \n
    w/weight: css 里面的 font-weight, 默认 normal \n
    s/style: css 里面的 font-style, 默认 normal \n
    d/display: css 里面的 font-display, 默认 swap \n
    v/flavor: 字体文件的类型
    """
    font = TTFont(input)

    # 获取字体的 unicode 字符
    cmap = font.getBestCmap()

    # 读取本地 json 配置
    current_dir = os.path.abspath(os.getcwd())
    json_path = os.path.join(current_dir, "assets/google-font-unicode-range.json")

    unicode_range = read_json(json_path)

    # 获取 font family
    font_family = get_font_family(input, family)

    # 取交集数据
    final_unicode_range = get_filter_range(cmap, unicode_range)

    create_dir(output)

    lock_map = {}
    css_strs = []
    # register, run = concurrent_tasks_factory()
    for index, single_range in enumerate(final_unicode_range):
        subset_name = f"{font_family}.{index + 1}"
        ctx.log(f"generating: {subset_name}")

        if subset_name in lock_map:
            raise Exception(f"Duplicate {subset_name}")
        # 锁
        lock_map[subset_name] = True

        # 获取 subset
        _font = TTFont(input)
        subsetter = Subsetter()
        subsetter.populate(text="".join([chr(int(code)) for code in single_range]))
        subsetter.subset(_font)

        # 输出子字体文件
        [_font.save(f"{output}/{subset_name}.{f}") for f in flavor]

        # 只压缩为 woff2 格式，兼容性也不错
        [woff2_compress(f"{output}/{subset_name}.{f}", f"{output}/{subset_name}.{f}") for f in flavor if
         f == "woff2"]

        # 生成对应的 css
        css = generate_css(
            font_fomats=flavor,
            font_weight=weight,
            font_style=style,
            font_display=display,
            font_family=font_family,
            unicode_range=single_range,
            name=f"{subset_name}"
        )

        css_strs.append(css)

    # run()
    write_css(css_strs, f"{output}/font.css")
    ctx.log(f"Finished!, output dir path is: {output}.")
