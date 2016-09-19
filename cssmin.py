#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#     Filename @  cssmin.py
#       Author @  Huoty
#  Create date @  2016-09-14 17:39:54
#  Description @  Minify your CSS
# *************************************************************

from __future__ import print_function

import sys
import requests

def cssmin(css_file, output_file=None):
    # Grab the file contents
    with open(css_file, 'r') as c:
        css = c.read()

    # Pack it, ship it
    payload = {'input': css}
    url = 'https://cssminifier.com/raw'
    print("Requesting mini-me of {}. . .".format(c.name))
    r = requests.post(url, payload)

    # Write out minified version
    minified = output_file if output_file else css_file.rstrip('.css')+'.min.css'
    with open(minified, 'w') as m:
        m.write(r.text)

    print("Minification complete. See {}".format(m.name))

# Script starts from here

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(prog="cssmin", description="Minify CSS file")
    parser.add_argument("cssfile", type=str, help="CSS file needed to convert")
    parser.add_argument("-o", "--output", type=str, help="Output file")
    options = parser.parse_args()
    cssmin(options.cssfile, options.output)
