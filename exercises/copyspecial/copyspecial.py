#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    filenames = os.listdir(dir)
    mylist=[]
    reSpecial=re.compile(u'__\w+__')
    for filename in filenames:
        if reSpecial.search(filename) != None:
            mylist.append(os.path.abspath(os.path.join(dir, filename)))
    return mylist

def copy_to(paths, dir):
    if not(os.path.exists(dir)): 
        os.mkdir(dir) 
    for filename in paths:
        shutil.copy(filename, dir)
    print "Special files copied"
    return
    
def zip_to(paths, zippath):
    # Prepare paths for spaces in directory names
    paths=['"'+path+'"' for path in paths]
    
    command='zip -j ' + zippath +' '+ ' '.join(paths)
    print 'Command I am going to do: '+command
    
    (status, output) = commands.getstatusoutput(command)
    if status:    ## Error case, print the command's output to stderr and exit
        sys.stderr.write(output)
        sys.exit(1)

    # print output  
    print "Special files zipped"    
    return

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
      specials=get_special_paths(dir)
      if todir!='':
          copy_to(specials, todir)

      if tozip!='':
          zip_to(specials, tozip)
          
      if (todir=='' and tozip==''):
          for filename in specials: print filename
  
if __name__ == "__main__":
  main()
