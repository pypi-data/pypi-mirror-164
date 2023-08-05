#!/usr/bin/env python
##
## This is file `sagetex-run.py',
## generated with the docstrip utility.
##
## The original source files were:
##
## scripts.dtx  (with options: `ifnecessaryscript')
## 
## This is a generated file. It is part of the SageTeX package.
## 
## Copyright (C) 2008--2015 by Dan Drake <dr.dan.drake@gmail.com>
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 2 of the License, or (at your
## option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
## Public License for more details.
## 
## You should have received a copy of the GNU General Public License along
## with this program.  If not, see <http://www.gnu.org/licenses/>.
## 
"""
Given a filename f, examines f.sagetex.sage and f.sagetex.sout and
runs Sage if necessary.
"""

import hashlib
import sys
import os
import re
import subprocess
import shutil
import argparse

def argparser():
    p = argparse.ArgumentParser(description=__doc__.strip())
    p.add_argument('--sage', action='store', default=find_sage(),
                   help="Location of the Sage executable")
    p.add_argument('src', help="Input file name (basename or .sagetex.sage)")
    return p

def find_sage():
    return shutil.which('sage') or 'sage'

def run(args):
    src = args.src
    path_to_sage = args.sage

    if src.endswith('.sagetex.sage'):
        src = src[:-13]
    else:
        src = os.path.splitext(src)[0]

    # Ensure results are output in the same directory as the source files
    os.chdir(os.path.dirname(src))
    src = os.path.basename(src)

    usepackage = r'usepackage(\[.*\])?{sagetex}'
    uses_sagetex = False

    # If it does not use sagetex, obviously running sage is unnecessary.
    if os.path.isfile(src + '.tex'):
        with open(src + '.tex') as texf:
            for line in texf:
                if line.strip().startswith(r'\usepackage') and re.search(usepackage, line):
                    uses_sagetex = True
                    break
    else:
        # The .tex file might not exist if LaTeX output was put to a different
        # directory, so in that case just assume we need to build.
        uses_sagetex = True

    if not uses_sagetex:
        print(src + ".tex doesn't seem to use SageTeX, exiting.", file=sys.stderr)
        sys.exit(1)

    # if something goes wrong, assume we need to run Sage
    run_sage = True
    ignore = r"^( _st_.goboom|print\('SageT| ?_st_.current_tex_line)"

    try:
        with open(src + '.sagetex.sage', 'r') as sagef:
            h = hashlib.md5()
            for line in sagef:
                if not re.search(ignore, line):
                    h.update(bytearray(line,'utf8'))
    except IOError:
        print('{0}.sagetex.sage not found, I think you need to typeset {0}.tex first.'
              ''.format(src), file=sys.stderr)
        sys.exit(1)

    try:
        with open(src + '.sagetex.sout', 'r') as outf:
            for line in outf:
                m = re.match('%([0-9a-f]+)% md5sum', line)
                if m:
                    print('computed md5:', h.hexdigest())
                    print('sagetex.sout md5:', m.group(1))
                    if h.hexdigest() == m.group(1):
                        run_sage = False
                        break
    except IOError:
        pass

    if run_sage:
        print('Need to run Sage on {0}.'.format(src))
        sys.exit(subprocess.call([path_to_sage, src + '.sagetex.sage']))
    else:
        print('Not necessary to run Sage on {0}.'.format(src))

if __name__ == "__main__":
    run(argparser().parse_args())
