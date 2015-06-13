# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:04:34 2015

@author: Deepti Boddapati
/deeptiboddapati
"""
import bs4, re, itertools, collections
'''
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
'''
def consolidate_tag():
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    tags = ['html', 'body', 'tr', 'td', 'u']
    ''''
    #will find all html tags in doc for now its hard coded. 
    for tag in lines.find_all(True):
        tags.append(tag.name)
    '''
    for i in lines(tags): #removes upperlevel navigable strings.
        for x in list(i.children):
            #print(type(x))
            if type(x) == bs4.element.NavigableString and len(x) <= 1:
                x.extract()
    for i in lines(tags):
        if len(i.find_next_siblings()) > 0:
            print('I have siblings!')
        # if there are siblings see if their name is the same as yours.
        # if the name is the the same then take their text out and put it inside yourself.

    file = open('destfile.html', 'w')
    file.write(lines.prettify())#Adds whitespace back in for formatting. 
    file.close()
    '''
    for m in lines(tags[0:]):
        print(type(m))
        for x in list(m.children):
            if x.siblings == True:
                print('true')
    '''

def main():
    #remove_empty_tag()
    #remove_title()
    #print([title])
    consolidate_tag()
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    print('inmain')
main()
