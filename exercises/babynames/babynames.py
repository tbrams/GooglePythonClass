#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(fn):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f=open(fn, 'r')
  reYear=re.compile(r'<input type="text" name="year" id="yob" size="4" value="(\d\d\d\d)">')
  year = reYear.findall(f.read())
  f.close()

  f=open(fn, 'r')
  reRanking=re.compile(r'<tr align=\"right\"><td>(\d+)</td><td>(\w+?)</td><td>(\w+?)</td>')
  rankings = re.findall(reRanking, f.read())
  nDict={}
  for rank, mName, fName in rankings:
      for name in [fName, mName]:
          currentRank=nDict.get(name)
          if not(currentRank is None) and int(currentRank)>int(rank): 
                  print 'Found smaller rank of %s for %s, was %s'%(rank, name, currentRank)
                  nDict[name]=rank
          else:
              nDict[name]=rank
  f.close()
  
  # create alphabetically sorted list with names and ranks
  mylist=[name + ' ' + nDict[name] for name in sorted(nDict)]
  return year+mylist    


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for fn in args:
    result=extract_names(fn)
    output='\n'+'\n'.join(result)+'\n'
    if (summary):
        f=open(fn+'.summary', 'w')
        f.write(output)
        f.close
    else:
        print output

  
if __name__ == '__main__':
  main()
