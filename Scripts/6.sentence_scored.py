# -*- coding: utf-8 -*-
from __future__ import division
import unicodedata
import codecs
import os
import os.path
import fnmatch
import string
import shutil
import re
import locale, codecs
from string import Template
pronoun_1=0
foreignwords_1=0
pronoun_2=0
foreignwords_2=0
end_line=0
b=1
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0
I=0



def sentence_length(line):
	wordcount=0
	words=string.split(line)
	wordcount+=len(words)
	return wordcount

def main_word_counter(line):
    mainwordcount=0
    words=string.split(line)
    for i in words:
            if i in ("سعدی شيرازی", "بزرگداشت", "سعدی", "ادبیات فارسی", "شاعر", "شیخ اجل", "مصلح الدین سعدی شيرازی"):
                    mainwordcount+=1
    return mainwordcount

def proper_word_counter(line):
    properwordcount=0
    words=string.split(line)
    for i in words:
        if i=='سعدی شيرازی' or i=='سعدی' or i=='شیخ اجل' or i=='مصلح الدین سعدی شيرازی':
            properwordcount+=1
    return properwordcount

def is_this_an_english_word (word):
    characters_here = list(word)
    is_english = True
    for c in characters_here:
	    if c not in string.ascii_letters:
		    is_english = False
		    break
    return is_english

def quotation_mark_counter(line):
    quotationcount=0
    words=string.split(line)
    for i in words:
        if i=='"':
            quotationcount+=1
    return quotationcount

def percentage_mark_counter(line):
    percentagecount=0
    words=string.split(line)
    for i in words:
        if i=='%':
            percentagecount+=1
    return percentagecount

def punctuation_mark_counter(line):
    punctuationcount=0
    words=string.split(line)
    for i in words:
        if i==':':
            punctuationcount+=1
    return punctuationcount

def parentheses_mark_counter(line):
    parenthesescount=0
    words=string.split(line)
    for i in words:
            if i=='(':
                    parenthesescount+=1
    return parenthesescount

def pronoun_counter(line):
    pronouncount=0
    pronoun=line.split()[1]
    if pronoun=='PRO':
            pronouncount+=1
    return pronouncount

def foreign_word_counter(line):
    foreignwordcount=0
    foreignwords=line.split()[1]
    if foreignwords=='FW':
            foreignwordcount+=1
    return foreignwordcount

f_name=open('/home/saeid/607-AH.txt', 'r')
g_name=open('/home/saeid/607-AH.txt.scored', 'w')
h_name=open('/home/saeid/607-AH.txt.tokenized.pos-tagged', 'r')

f_lines = f_name.readlines()
h_lines = h_name.readlines()

for m in f_lines:
        A=sentence_length(m)
        B=main_word_counter(m)
        C=proper_word_counter(m)
        D=quotation_mark_counter(m)
        E=percentage_mark_counter(m)
        F=punctuation_mark_counter(m)
        G=parentheses_mark_counter(m)
        end_line+=sentence_length(m)
        for x in h_lines:
                if b!=end_line:
                        pronoun_2+=pronoun_counter(x)
                        foreignwords_2+=foreign_word_counter(x)
                        b+=1
        
        H=pronoun_2-pronoun_1
        pronoun_1=0
        I=foreignwords_2-foreignwords_1
        foreignwords_1=0
        pronoun_1+=pronoun_2
        foreignwords_1+=foreignwords_2


        score=((1/A)+(B/A)+(C/A)+(D/A)+(E/A)+(F/A)+(1-G/A)+(1-H/A)+(I/A))
        
        g_name.write(str(score))
        g_name.write(' ')
        g_name.write(m)
          
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0
        H=0
        I=0
        b=1
        pronoun_2=0
        foreignwords_2=0

                
                                  
        
