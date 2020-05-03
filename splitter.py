#!/usr/bin/env python

"""
Samsung's S7 Motion Photo splitter.
S7 generates a container which encapsulates picture and video. The first part
is a JPEG with its usual footer plus Samsung's own (MotionPhoto_Data). Second
part is the video.

Algorithm: 
Count the bytes for each offset and write the files.
JPEG: byte zero to samsungs footer end
MP4: JPEG's footer + 1 to end of file (size of the file)

Behaviour:
This script handles multiple files and splits each one into a JPG and an MP4.
If the file does not contain a motion part, it proceeds to the next file.
At the end, the script reports a list of all files that could not be split.
"""

import sys
from os import path
from mmap import mmap


__author__ = "Christian Lete"
__license__ = "Apache 2.0"
__version__ = "0.9"
__maintainer__ = "Christian Lete"
__email__ = "christian.lete {at} gmail com"

#End of picture signature - not JPEG footer but "MotionPhoto_Data"
eop = "\x4D\x6F\x74\x69\x6F\x6E\x50\x68\x6F\x74\x6F\x5F\x44\x61\x74\x61"


def write_files(fname,jpeg,mp4):
  """
  Creates videos and files
  """
  sname = fname.replace('.jpg','')
  picture = sname + "_new" + ".jpg"
  video = sname + "_new" +  ".mp4"

  with open(picture,'w') as f:
      f.write(jpeg)

  if path.exists(video):
    sys.exit('Error: file %s exists' % video )
  else:
    with open(video,'w') as f:
      f.write(mp4)

def spliter(fname):
  """
  Splits video and picture
  """
  with open(fname,'r+b') as f:
    mm = mmap(f.fileno(),0)
    file_size = mm.size()

    # size of the file - len of the samsung magic = processed file
    magic_samsung = mm.find(eop)
    magic_samsung_lim = file_size - len(eop)

    #Do not process if magic is not found, and if found at the end
    if magic_samsung == -1 or  magic_samsung == magic_samsung_lim:
      raise Exception("Error: file %s has no motion photo" % fname)
    else:
      samsung_jpeg_offset = magic_samsung + len(eop)
      mpeg_start = samsung_jpeg_offset + 1
      mpeg_end = file_size
  
      #JPEG  here
      mm.seek(0)
      jpeg = mm.read(samsung_jpeg_offset)

      #MP4 here
      #Start in the first byte of the MP4 container
      mm.seek(mpeg_start - 1) 
      mp4 = mm.read(mpeg_end)
      write_files(fname,jpeg,mp4)
  

if len(sys.argv) < 2:
  sys.exit('Usage:: %s <files>' % sys.argv[0])

files = sys.argv[1:]
not_motion = []
for fname in files:
  try:
    spliter(fname)
  except:
    not_motion.append(fname)

for jpg_file in not_motion:
  print(jpg_file)

