# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:04:34 2015

@author: Deepti Boddapati
/deeptiboddapati
"""
import bs4, re, itertools, collections

def remove_empty_tag():
    taglist = ['td','tr','u'] 
    file = open('file.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close() 
    for x in range(len(taglist)):
        i = 0
        while i < (len(lines(taglist[x]))):
            if lines(taglist[x])[i].getText().isspace():
                lines(taglist[x])[i].extract()
            else:
                i +=1
    writef = open('destfile.html', 'w')
    writef.write(lines.prettify())
    writef.close()


def remove_title():
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    title = re.sub(r'(\s\s+)',r' ', lines('title')[0].extract().get_text())
    #gets the second table in text which contains the bill. 
    lines = lines('table')[1].extract()
    #gets the first sentence of the bill.
    for x in lines('td'):
        chkstring = x.get_text() #TODO ask mark if he wants the text extracted.
        b = re.search('[.]',chkstring)
        title += re.sub(r'(\s\s+)',r' ', chkstring) 
        if b is not None:
            break
    writef = open('destfile.html', 'w')
    writef.write(lines.prettify())
    writef.close()
    return title

def consolidate_tag():
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    tags = ['html', 'body', 'tr', 'td', 'u']

    for i in lines(tags): #removes upperlevel navigable strings.
        for x in list(i.children):
            #print(type(x))
            if type(x) == bs4.element.NavigableString and len(x) <= 1:
                x.extract()

    for i in lines(tags[3]):
        i.unwrap()
    for i in lines(tags[-1]):
        #find out if tag has siblings. 
        if len(i.find_next_siblings()) > 0:
            # if there are siblings see if their tag is the same
            for x in (list(i.find_next_siblings())):
                # if the name is the the same then remove the text and place inside tag.
                if x.name == i.name:
                    i.append(x.extract().get_text())
    ptag = lines.new_tag('p', {id :"SECTION"})
    count = 0
    for i in list(lines('tr')):
        #check what the first word is
        print(count, list(i.stripped_strings)[0], list(i.stripped_strings)[0].find('SECTION')== True)
        print(i.name)
        count += 1
        '''
        if 'SECTION' in list(i.stripped_strings)[0]:
            print(i.parent.name)
            i.wrap(ptag)
            print(i.parent.name)
        '''
    file = open('destfile.html', 'w')
    file.write(lines.prettify())#Adds whitespace back in for formatting. 
    file.close()

def main():
    remove_empty_tag()
    remove_title()
    #print([title])
    consolidate_tag()
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    print('inmain')
main()
