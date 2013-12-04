#!/usr/bin/env python

"""
open source domain lisensed in MIT, by Victor X.D. Huang, bayvictor@gmail.com
simple a few line filename fixxing for ilegal characters for all subdirs.
run under proxy-style environment like cywin,mingw, linux, mac etc.
"""

import os
import sys
import string

def replace_illegal_char_in_filename():
  p = os.popen('find . -type f |sed \'s/\.\/\.//g\' ' , 'r')
  lines = p.readlines()
  p.close()



  for jj in range(0, len(lines)):
    line=lines[jj].split("\n")[0]
    new_line = ''.join( ch if ch.isalnum() else '_' for ch in line )
    words = new_line.split("_")
    new_line2 = '_'.join( word for word in words[:-1] ) + "." + words[-1]
    for kk in range(0,len(new_line2)):
      if new_line2[kk] != '_':
        break

    new_line2 = new_line2[kk:]
    os.system("mv "+ "\"" + line+"\" "+ new_line2 + " " )

if __name__=="__main__":
  replace_illegal_char_in_filename()


	
