# -*- encoding: cp1251 -*-

import re

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
        if not linex[0:-1]:
            0
        elif linex[0] == " ":
            linesdict[lineparts[0]] = linesdict[lineparts[0]] + linex[1:-1]
            
        else:
            lineparts = split_unescaped(linex[0:-1], ':')
            linesdict.update({lineparts[0]:lineparts[1]})
           

    print linesdict['N']

def vcard_to_list(vcard_text):
    lines = vcard_text.splitlines(True)
    lineslist = []

    for linex in lines:
        if not linex[0:-1]:
            0
        elif linex[0] == " ":
            lastpos = len(lineslist)-1
            lineslist[lastpos] = lineslist[lastpos] + linex[1:-1]

        else:
            lineparts = split_unescaped(linex[0:-1], ':')
            lineslist.append(linex[0:-1])

    print lineslist[2]


filename = 'test.vcf'
file_pointer = open(filename, 'r')

contents = file_pointer.read().splitlines(True)


vcard_text = ''
for index in range(len(contents)):
   line = contents[index]
   vcard_text += line
    
   cnt = 0
   if line.find("END:VCARD")>= 0:
      vcard_to_dict(vcard_text)
      vcard_text = ''
