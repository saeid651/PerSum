import os
import os.path
import fnmatch
import glob
from collections import deque
import shutil
from xml.dom import minidom
from xml.dom.minidom import parseString
queue=deque()
que_id_topics=deque()
for line in open('/home/saeid/HAM1/10.2454_AH-PERSIAN-CLEF2009.txt','r'):
    if '1' in line[-2:]:
        que_id_topics.append(line[17:-3])

path='/home/saeid/extracted_XML_files'
for f in os.listdir(path):
    if fnmatch.fnmatch(f, '*.txt'):
        queue.append(f[:-4])
for n in que_id_topics:
    for m in queue:
        if m==n:
            shutil.copyfile('/home/saeid/extracted_XML_files/'+m+'.txt', '/home/saeid/categorized_txt_files/650-AH/'+m+'.txt')
        

