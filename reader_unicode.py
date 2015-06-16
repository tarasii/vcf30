# -*- encoding: utf8 -*-
# cp1251 

import re
import codecs

def find_unescaped(text, char, escape_char='\\'):
    unescaped_regex = '(?<!{0}{0})(?:{0}{0}{0}{0})*({1})'.format(escape_char, re.escape(char))
    regex = re.compile(unescaped_regex)

    char_match = regex.search(text)

    if char_match is None:
        return None
    return char_match.start(1)

def split_unescaped(text, separator, escape_char='\\'):
    result = []
    while True:
        index = find_unescaped(text, separator, escape_char)
        if index is not None:
            result.append(text[:index])
            text = text[index + 1:]
        else:
            result.append(text)
            return result

def vcard_to_dict(vcard_text):
    lines = vcard_text.splitlines(True)
    linesdict = {}

    for linex in lines:
        if not linex.strip('\r\n'):
            0
        elif linex[0] == " " or linex[0] == u'\r':
            linesdict[lineparts[0]] = linesdict[lineparts[0]] + linex.strip('\r\n ')
            
        else:
            lineparts = split_unescaped(linex.strip('\r\n'), ':')
            if len(lineparts)==1:
                print lineparts 
            linesdict.update({lineparts[0]:lineparts[1]})
           
    #if 'X-SKYPE-MOOD' in linesdict.keys():
    if  linesdict.has_key('X-SKYPE-MOOD'):
    	#print linesdict['N'] + "; " + linesdict['X-SKYPE-MOOD']
        print linesdict['N']
    	print linesdict['X-SKYPE-MOOD'].decode("utf-8")
    else:
        print linesdict['N']

    #print linesdict['N'] + "; "  
    #print linesdict.keys()

def vcard_to_list(vcard_text):
    lines = vcard_text.splitlines(True)
    lineslist = []

    for linex in lines:
        #if not linex[0:-1]:
        if not linex.strip('\r\n'):
            0
        elif linex[0] == " ":
            lastpos = len(lineslist)-1
            lineslist[lastpos] = lineslist[lastpos] + linex.strip('\r\n ')

        else:
            #lineparts = split_unescaped(linex[0:-1], ':')
            lineslist.append(linex.strip('\r\n'))

    #print lineslist[2]
    print lineslist[2:5]


filename = 'taras.ivaniv.vcf'
#filename = 'contacts.vcf'
file_pointer = codecs.open(filename, 'r', encoding='utf8')

contents = file_pointer.read().splitlines(True)

vcard_text = ''
for index in range(len(contents)):
   line = contents[index]
   vcard_text += line
    
   cnt = 0
   if line.find("END:VCARD")>= 0:
      #print vcard_text
      vcard_to_dict(vcard_text)
      #vcard_to_list(vcard_text)
      vcard_text = ''
