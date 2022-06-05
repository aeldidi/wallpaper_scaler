# /usr/bin/env python3
import argparse
import pathlib
from PIL import Image, ImageFilter


def filepath(p):
    if pathlib.Path(p).exists():
        return p
    else:
        raise argparse.ArgumentTypeError(f"file '{p}' does not exist")


parser = argparse.ArgumentParser(
    description="Scales any image to be a wallaper, bluring the edges if the "
    + "aspect ratios are different."
)
parser.add_argument(
    "--width", type=int, help="the width of the output image", required=True
)
parser.add_argument(
    "--height", type=int, help="the height of the output image", required=True
)
parser.add_argument(
    "--output",
    "-o",
    type=str,
    help="the file to output to (defaults to output.png)",
    default="output.png",
)
parser.add_argument(
    "file",
    type=filepath,
    help="the file to generate a wallpaper from.",
)


def main(args):
    base = Image.open(args.file)
    blurimage = base.filter(ImageFilter.GaussianBlur(50))

    h_factor = args.height // base.size[1]
    w_factor = args.width // base.size[0]

    if h_factor == 0:
        num = (base.size[1] // args.height) + 1
        if num % 2 != 0:
            num += 1
        h_factor = 1 / num

    if (base.size[0] * w_factor) < args.width or w_factor == 0:
        w_factor += 1

    blurimage = blurimage.resize(
        (base.size[0] * w_factor, base.size[1] * w_factor), Image.Resampling.NEAREST
    )
    vertical = (blurimage.size[1] - args.height) // 2
    blurimage = blurimage.crop((0, vertical, args.width, args.height + vertical))

    if h_factor >= 1:
        base = base.resize(
            (int(base.size[0] * h_factor), int(base.size[1] * h_factor)),
            Image.Resampling.NEAREST,
        )
    else:
        base = base.resize(
            (int(base.size[0] * h_factor), int(base.size[1] * h_factor)),
            Image.Resampling.NEAREST,
        )

    pos = (
        (args.width // 2) - (base.size[0] // 2),
        (args.height // 2) - (base.size[1] // 2),
    )

    blurimage.paste(base, pos)
    blurimage.save(args.output)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
