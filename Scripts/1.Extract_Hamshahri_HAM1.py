import os
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
que_id_topics=deque()
que_origin=deque()
que_DOCID_topics=deque()
que_cat=deque()
que_final=deque()

path='/home/saeid/Untitled Folder'
for infile in glob.glob(os.path.join(path, '*.xml')):
    que_origin.append(infile)
    tree=ET.parse(infile)
    root=tree.getroot()
    for DOC in root.findall('DOC'):
        que_DOCID_topics.append(DOC.find('DOCID').text)
    for x in que_DOCID_topics:
        que_final.append('/home/saeid/extracted_XML/'+x+'.txt')
    for y in que_origin:
        context = cE.iterparse(y, events=('start', 'end'))
        context = iter(context)
        event, root = context.next() # get the root element of the XML doc
        for event, elem in context:
            if event == 'end':
                if elem.tag == 'DOC': # i want to write out all <bucket> entries
                    elem.tail = None
                    output=open(que_final.popleft(), 'w')
                    output.write('<HAMSHAHRI>')
                    output.write(cE.tostring(elem))
                    output.write('</HAMSHAHRI>')
                        
