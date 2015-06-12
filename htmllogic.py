# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:04:34 2015

@author: Deepti Boddapati
/deeptiboddapati
"""
import bs4, re

def remove_empty_tag():
    taglist = ['td','tr','u']   
    
    for x in range(len(taglist)):
        i = 0
        while i < (len(lines(taglist[x]))):
            if lines(taglist[x])[i].getText().isspace():
                lines(taglist[x])[i].extract()
            else:
                i +=1
'''
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
    for x in lines('tr'):
        for i in x.descendants:
            for y in i.find_next_siblings():
                if y is None:
                    y.extract()
                elif y.name == i.name:
                    print(y.string)
    print(i)
def main():
    remove_empty_tag()
    #title = remove_title()
    #print([title])
    consolidate_tag()
main()
