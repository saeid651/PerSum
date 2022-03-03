import os
import os.path
import fnmatch
import glob
import Queue
import string
from collections import deque
import shutil
import re
import locale, codecs
from string import Template
que_address_files=deque()
que_address_files_write=deque()
que_for_loop=deque()
def clean(x): return x.strip()
a=1
b=1
sentence_length=0

path='/home/saeid/607-AH'
for infile in glob.glob(os.path.join(path, '*.tokenized_2')):
    que_address_files.append(infile)
    que_address_files_write.append(infile+'.sentence-extracted')
    que_for_loop.append(infile)

for count in que_for_loop:
    f_name=open(que_address_files.popleft(), 'r')
    o_name=open(que_address_files_write.popleft(), 'w')

    lines = f_name.readlines()
    for line in lines:
        if line!="\n":
            b+=1

        elif line=="\n":
            all_lines = map(clean, lines)
            sentence=" ".join(all_lines[a:b]).strip()
            print sentence
            a=b
            b+=1
            o_name.write(sentence)
            o_name.write("\n")
    a=1
    b=1
        
