"""工具函数"""
import click

from shutil import rmtree
from os import path, makedirs
from asyncio import get_event_loop, gather
from fontTools.ttLib import TTFont, woff2
from fontTools.subset import Subsetter
from json import load

# TODO 应该可以支持更多的字体文件的，暂时没写
supported_fonts = [".woff", ".woff2", ".otf", ".ttf"]


def read_json(json_path):
    """读取 JSON"""
    try:
        with open(json_path, "r") as file:
            data = load(file)
        return data
    except Exception as e:
        click.echo(f"Error reading file in path {json_path}: {str(e)}")


async def read_txt(file_path):
    """读取 TXT"""
    if not file_path:
        click.echo("File path must be provided.")
        return
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        click.echo(f"Error reading file in path {file_path}: {str(e)}")


def create_dir(out_dir, rm=True):
    """创建目录"""
    if rm and path.exists(out_dir):
        rmtree(out_dir)
    makedirs(out_dir)


def concurrent_tasks_factory():
    """并发执行任务的工厂函数"""
    tasks = []

    async def gather_tasks():
        results = await gather(*tasks)
        return results

    def register(task):
        tasks.append(task)

    def run():
        loop = get_event_loop()
        return loop.run_until_complete(gather_tasks())

    return register, run


def woff2_compress(original_file_path, compressed_file_path):
    """压缩到体积最小的 woff2"""
    woff2.compress(original_file_path, output_file=compressed_file_path)


def save_subset_font(font_path, output_path, chrs, options=None):
    """提取子字体集到一个文件中"""
    font = TTFont(font_path)
    subsetter = Subsetter(options)
    subsetter.populate(text=chrs)
    subsetter.subset(font)

    font.save(output_path)


async def get_font_output_path(input_path, output_path, extension):
    """获取输出文件的路径，支持传入目录或者文件路径"""
    _, ext = path.splitext(output_path)
    is_file = bool(ext)

    if is_file:
        directory = path.dirname(path.abspath(output_path))
    else:
        directory = path.abspath(output_path)

    # 如果没有这个目录，创建一个
    if not path.exists(directory):
        makedirs(directory)

    if is_file:
        return output_path

    file_name, _ = path.splitext(path.basename(input_path))
    return f"{directory}/{file_name}.{extension}"


def get_font_family(input_path, font_family):
    """处理 font-family"""
    extracted_font_family = path.splitext(path.basename(input_path))[0]
    return font_family if font_family else extracted_font_family


def get_filter_range(camp, unicode_range):
    """获取配置 JSON 和字体 unicodes 的交集"""
    filter_unicode_range = []
    for items in unicode_range:
        unicodes = items['unicodes']
        filter_unicode = [unicode for unicode in unicodes if unicode in camp]
        if len(filter_unicode) > 0:
            filter_unicode_range.append(filter_unicode)

    return filter_unicode_range


def create_unicode_range(lst):
    """把 unicode 转成 unicode-range"""
    result = []
    workflow = []

    def do_work():
        nonlocal workflow, result
        if len(workflow) == 0:
            return

        if len(workflow) > 2:
            first = workflow[0]
            last = workflow[-1]
            result.append(f"U+{first:04X}-{last:04X}")
            workflow = []

        for item in workflow:
            result.append(f"U+{item:04X}")
        workflow = []

    for i in range(len(lst)):
        last = workflow[-1] if workflow else None
        if last is not None and lst[i] != last + 1:
            do_work()
        workflow.append(lst[i])

    do_work()

    return result


def generate_css(font_fomats, font_weight, font_style, font_display, font_family, unicode_range, name):
    """生成 css 代码片段"""
    format_map = {
        'ttf': 'truetype',
        'otf': 'opentype',
        'svg': 'svg',
        'eot': 'embedded-opentype',
        'woff': 'woff',
        'woff2': 'woff2',
    }

    src = '\n'.join([f'url("./{name}.{f}") format("{t}")' for f in font_fomats if (t := format_map.get(f))])
    range_str = ','.join(create_unicode_range(unicode_range))

    return f'''@font-face {{
  font-family: {font_family};
  src: {src};
  font-weight: {font_weight};
  font-style: {font_style};
  font-display: {font_display};
  unicode-range: {range_str};
}}'''


def write_css(css_str_arr, output_path):
    """写入 css 到某目录下"""
    with open(output_path, 'w') as file:
        file.write('\n'.join(css_str_arr))
