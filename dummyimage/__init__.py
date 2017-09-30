#! /usr/bin/env python3
""" Simple module to save images generated using dummyimage.com """
import argparse
import requests
import re
import os
import shutil

def image_size(string):
    """Determines if a string is formatted as a valid image size"""
    value = str(string)
    if not re.match('^([1-9]\d*)[xX]([1-9]\d*)$',value):
        msg = "%r is not a valid image size string" % string
        raise argparse.ArgumentError(msg)
    return value
# end image_size
def hexcode(string):
    """Determines if a string is formatted as a valid hexadecimal color"""
    value = str(string)
    if not re.match('^([0-9a-fA-F]{3}){1,2}$',value):
        msg = "%r is not a valid hexadecimal color string" % string
        raise argparse.ArgumentError(msg)
    return value
# end hexcode

def request_image(args):
    size = args.size
    bg = args.bg
    fg = args.fg
    fmt = args.format
    text: str = f"&text={args.text}" if args.text else ''
    filename = f"./{args.text.replace(' ','-')}.{fmt}"
    outdir = f"{args.out}" if args.out else "./"
    image_url = f"https://dummyimage.com/{size}/{bg}/{fg}{fmt}{text}"
    img_request = requests.get(image_url, stream=True)
    if os.path.isdir(os.path.realpath(outdir)):
        outfile = os.path.realpath(f"{outdir}/{filename}")
        with open(outfile, mode='wb') as fh:
            shutil.copyfileobj(img_request.raw, fh)
    else:
        msg = f"File already exists! Cannot overwrite: {ofile}"
        raise FileExistsError(msg)
    
# end request_image

parser = argparse.ArgumentParser(prog='dmyimg', description="Get dummy image")
parser.add_argument('size', help='Size as [WIDTH]x[HEIGHT]', type=image_size)
parser.add_argument('bg', help='Hexadecimal color for background',type=hexcode)
parser.add_argument('fg', help='Hexadecimal color for foreground',type=hexcode)
parser.add_argument('text', help='The text to embed into the image')
parser.add_argument('-f','--format', help='Image format', choices=['gif','jpg','png'], default='jpg')
parser.add_argument('-o','--out', help='Output path')
parser.set_defaults(func=request_image)

def entry_func():
    ARGS = parser.parse_args()
    try:
        ARGS.func(ARGS)
    except Exception as ex:
        print(ex)
        parser.print_help()
# end entry_func

if __name__ == "__main__":
    entry_func()