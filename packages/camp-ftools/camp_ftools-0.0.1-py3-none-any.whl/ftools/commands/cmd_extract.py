import click

from ftools.helper import get_font_output_path, woff2_compress, read_txt, concurrent_tasks_factory, save_subset_font
from ftools.cli import pass_environment


@click.command("extract", short_help="Extract subset into new font file")
@click.option("-i", "--input", type=click.Path(exists=True, readable=True), required=True, help="font file path")
@click.option("-o", "--output", type=click.Path(), required=True, help="output file path")
@click.option("-c", "--characters", type=click.Path(exists=True, readable=True), required=True, help="txt file path")
@click.option("-v", "--flavor", type=click.Choice(["woff", "woff2", "otf", "ttf"]), multiple=False, default="woff2",
              help="font types")
@pass_environment
def cli(ctx, input, output, characters, flavor):
    """
    从一个字体中提取固定字符的子字体集到一个新文件中，转出为 woff2 格式的文件会自动压缩 \n
    i/input: 源字体文件的路径 \n
    o/output: 输出字体文件的路径 \n
    c/characters: 需要提取的字符文件路径，目前支持 TXT 格式文件 \n
    v/flavor: 转出的字体文件格式类型，默认是 woff2
    """
    # 协程
    register, run = concurrent_tasks_factory()

    # 注册
    register(read_txt(characters))
    register(get_font_output_path(input, output, flavor))

    chrs, output_path = run()

    # 提取字体
    save_subset_font(input, output_path, chrs)

    # 压缩字体
    [woff2_compress(output_path, output_path) for f in flavor if f == "woff2"]

    ctx.log(f"Finished!, output file path is {output_path}.")
