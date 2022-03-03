import os
import os.path
import fnmatch
import glob
import Queue
import string
from collections import deque
import xml.etree.ElementTree as ET
import xml.etree.cElementTree as cE
import shutil
from xml.dom import minidom
import re
import locale, codecs
from xml.dom.minidom import parseString
from xml.etree import ElementTree
from string import Template
queue=deque()
que_id_topics=deque()
que_origin=deque()
que_DOCID_topics=deque()
que_dectination=deque()
que_cat=deque()
que_final=deque()
for line in open('/home/administrator/Hamshahri/10.2454_AH-PERSIAN-CLEF2009.txt','r'):
    if '1' in line[-2:]:
        que_id_topics.append(line[17:-3])
        que_cat.append(line[:14])

path='/home/administrator/Hamshahri/python/sol_1'
#os.makedirs('/home/administrator/Hamshahri/python/sol/600-AH')
#for infile in glob.glob(os.path.join(path, '*.txt')):
#    que_origin.append(infile)
#    que_dectination.append(re.sub('sol_1', 'sol/600-AH', infile))

for f in os.listdir(path):
    if fnmatch.fnmatch(f, '*.txt'):
        queue.append(f[:-4])
for n in que_id_topics:
    for m in queue:
        if m==n:
            shutil.copyfile('/home/administrator/Hamshahri/python/sol_1/'+m+'.txt', '/home/administrator/Hamshahri/python/sol/650-AH/'+m+'.txt')
        

#path='/home/administrator/Hamshahri/python/sol_19'
#os.makedirs('/home/administrator/Hamshahri/python/sol/600-AH')
#for infile in glob.glob(os.path.join(path, '*.txt')):
#    que_origin.append(infile)
#    que_dectination.append(re.sub('sol_19', 'sol/600-AH', infile))
#    tree=ET.parse(infile)
#    root=tree.getroot()
#    for DOC in root.findall('DOC'):
#        que_DOCID_topics.append(DOC.find('DOCID').text)

#for x in que_DOCID_topics:
#    for y in que_id_topics:
#            if (x==y and que_cat.popleft()=='10.2452/600-AH'):
#                shutil.copyfile(que_origin.popleft(), que_dectination.popleft())
                
#for infile in glob.glob(os.path.join(path, '*.xml')):
#    tree=ET.parse(infile)
#    root=tree.getroot()
#    for DOC in root.findall('DOC'):
#        que_DOCID_topics.append(DOC.find('DOCID').text)
#for x in que_final1:
#    que_final2.append(re.sub('HAM1', 'python/sol/'+que_DOCID_topics.popleft()+'.txt', que_final1.popleft()))
