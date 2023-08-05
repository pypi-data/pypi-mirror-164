#!/usr/bin/env python
##
## This is file `sagetex-makestatic.py',
## generated with the docstrip utility.
##
## The original source files were:
##
## scripts.dtx  (with options: `staticscript')
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
Removes SageTeX macros from `inputfile' and replaces them with the
Sage-computed results to make a "static" file. You'll need to have run
Sage on `inputfile' already.

`inputfile' can include the .tex extension or not. If you provide
`outputfile', the results will be written to a file of that name.
Specify `-o' or `--overwrite' to overwrite the file if it exists.

See the SageTeX documentation for more details.
"""
import sys
import time
import os.path
import argparse

from sagetexparse import DeSageTex

def argparser():
    p = argparse.ArgumentParser(description=__doc__.strip())
    p.add_argument('inputfile', help="Input file name (basename or .tex)")
    p.add_argument('outputfile', nargs='?', default=None, help="Output file name")
    p.add_argument('-o', '--overwrite', action="store_true", default=False,
                   help="Overwrite output file if it exists")
    p.add_argument('-s', '--sout', action="store", default=None,
                   help="Location of the .sagetex.sout file")
    return p

def run(args):
    src, dst, overwrite = args.inputfile, args.outputfile, args.overwrite

    if dst is not None and (os.path.exists(dst) and not overwrite):
        print('Error: %s exists and overwrite option not specified.' % dst,
              file=sys.stderr)
        sys.exit(1)

    src, ext = os.path.splitext(src)
    texfn = src + '.tex'
    soutfn = args.sout if args.sout is not None else src + '.sagetex.sout'
    desagetexed = DeSageTex(texfn, soutfn)
    header = ("%% SageTeX commands have been automatically removed from this file and\n"
              "%% replaced with plain LaTeX. Processed %s.\n"
              "" % time.strftime('%a %d %b %Y %H:%M:%S', time.localtime()))

    if dst is not None:
        dest = open(dst, 'w')
    else:
        dest = sys.stdout

    dest.write(header)
    dest.write(desagetexed.result)

if __name__ == "__main__":
    run(argparser().parse_args())
