#!/usr/bin/python3

from PIL import Image
from PIL import ImageDraw
import numpy
from absl import flags
from absl import app

flags.DEFINE_integer("width", 4096, "Width of the output canvas.")
flags.DEFINE_integer("height", 4096, "Height of the output canvas.")
flags.DEFINE_integer("cols", 3, "Number of columns in the grid.")
flags.DEFINE_integer("rows", 3, "Number of rows in the grid.")
flags.DEFINE_string("output", "output.png", "Output filename.")

FLAGS = flags.FLAGS


def main(argv):
    size = (FLAGS.width, FLAGS.height)
    grid_size = (FLAGS.cols, FLAGS.rows)

    out_image = Image.new('RGB', size, color=(255, 255, 255))
    draw = ImageDraw.Draw(out_image)

    for v in numpy.array(range(1, grid_size[0])) * size[0] / grid_size[0]:
        draw.line((v, 0, v, size[1]), fill=(0, 0, 0), width=3)
    for h in numpy.array(range(1, grid_size[1])) * size[1] / grid_size[1]:
        draw.line((0, h, size[0], h), fill=(0, 0, 0), width=3)

    with open(FLAGS.output, 'wb') as out_file:
        out_image.save(out_file, 'png')


if __name__ == "__main__":
    app.run(main)
