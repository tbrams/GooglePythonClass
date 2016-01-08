#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++

  print "read_urls:"+filename
    
  # Use a dict for storage to avoid having to consider what to do with doubles
  pDict={}
  # Compile a regular expression targeting the image files we are looking for
  rePuzzle=re.compile(u'GET (\S+/puzzle/\S+) HTTP/')

  # Open the specified logfile and store entry in the dictionary using only the filename as key 
  f=open(filename, 'r')
  for entry in  re.findall(rePuzzle, f.read()):
      shortname=os.path.basename(entry) 
      pDict[shortname]=entry
  f.close()
  
  print "filename is %s"%filename
  if not(filename.find('place_code.google.com')):
      # Create a list with all the sorted urls based on the last word for the return value
      # We do that by stepping back over ".jpg" and then 4 more, that we then select for sorting.
#      return [pDict[shortname] for shortname in sorted(pDict.keys(), key=lambda(x): x[-13:-4])]
      print 'try sort again..and'
      return [pDict[x] for x in sorted(pDict.keys(), key=lambda(x):x[-8:-4])]
  else:
      # Create a list with all the sorted urls for the return value
      return [pDict[filename] for filename in sorted(pDict.keys())]
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  
  # prepare output directory - if it is not there already, create it
  if not(os.path.exists(dest_dir)):
      os.mkdir(dest_dir)

  i=0
  imgstr=''
  for slice in img_urls:
      # use a simple naming scheme for new image files and make sure they end up in the given directory
      outfile='img'+str(i)+'.png'
      imgstr+='<img src="'+outfile+'">'
      outfile=os.path.join(dest_dir, outfile)
      print "Fetching "+outfile+' '+ os.path.basename(slice) 
      urllib.urlretrieve('http://code.google.com/'+slice, outfile)
      i+=1
  print "All image strips downloaded"

  f=open(os.path.join(dest_dir, 'index.html'), 'w')
  f.write('<html><body>')
  f.write(imgstr)
  f.write('</body></html>')
  f.close()
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
