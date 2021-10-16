#!/usr/bin/python

import argparse
import math
import sys

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

ap = argparse.ArgumentParser(description='Attention Wallpaper Generator')
ap.add_argument('filename', type=str)
api = ap.add_argument_group(title='image options')
api.add_argument('-W', '--width', type=int, default=1920)
api.add_argument('-H', '--height', type=int, default=1080)
api.add_argument('-B', '--background', type=str, default='white')
api.add_argument('-F', '--foreground', type=str, default='black')
apt = ap.add_argument_group(title='text options')
apt.add_argument('-T', '--text', type=str)
apt.add_argument('--text-font', type=str, default='Noto-Serif-CJK-JP-Black')
apt.add_argument('--text-size', type=int, default=160)
apt.add_argument('--text-kerning', type=float, default=-0.025)
apt.add_argument('--text-scale-x', type=float, default=0.7)
apt.add_argument('--text-scale-y', type=float, default=1.0)
aps = ap.add_argument_group(title='stripe options')
aps.add_argument('--stripe-height', type=float, default=0.5)
aps.add_argument('--stripe-band-width', type=float, default=0.2)
a = ap.parse_args()

sw = math.ceil(a.width / 2)
sh = math.ceil(a.text_size * a.stripe_height)
sbw = math.ceil(a.text_size * a.stripe_band_width)
sbx = math.ceil(sh / math.sqrt(3))

def draw_stripe(image: Image, drawing: Drawing, x: int, y: int, flip: bool, flop: bool):
    with Image(width=sw, height=sh) as stripe_image:
        with Drawing(drawing) as stripe_drawing:
            for i in range(math.ceil(sbx / sbw * -2), math.ceil(sw / sbw * 2)):
                ix = 2 * i * sbw
                stripe_drawing.polygon([(ix, 0),
                                        (ix + sbw, 0),
                                        (ix + sbx + sbw, sh),
                                        (ix + sbx, sh)])
            stripe_drawing.draw(stripe_image)
        if flip:
            stripe_image.flip()
        if flop:
            stripe_image.flop()
        image.composite(stripe_image, x, y)


with Image(width=a.width, height=a.height, background=Color(a.background)) as image:
    with Drawing() as drawing:
        drawing.fill_color = Color(a.foreground)
        if sh * sbw > 0:
            draw_stripe(image, drawing, 0, 0, True, True)
            draw_stripe(image, drawing, sw, 0, True, False)
            draw_stripe(image, drawing, 0, a.height - sh, False, True)
            draw_stripe(image, drawing, sw, a.height - sh, False, False)
        drawing.gravity = 'center'
        drawing.font = a.text_font
        drawing.font_size = a.text_size
        drawing.text_kerning = a.text_size * a.text_kerning
        drawing.scale(a.text_scale_x, a.text_scale_y)
        drawing.text(0, 0, a.text if a.text is not None else sys.stdin.read())
        drawing.draw(image)
    image.save(filename=a.filename)
