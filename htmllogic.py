# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:04:34 2015

@author: Deepti Boddapati
/deeptiboddapati
"""
import bs4, re
def remove_empty_tag():
    taglist = ['td','tr','u']
    file = open('file.html', 'r')
    writef = open('destfile.html', 'w')
    
    domfile = bs4.BeautifulSoup(file.read())
    
    for x in range(len(taglist)):
        i = 0
        while i < (len(domfile(taglist[x]))):
            if domfile(taglist[x])[i].getText().isspace():
                domfile(taglist[x])[i].extract()
            else:
                i +=1
    #self.billtext[-1]=domfile.prettify()
    writef.write(str(domfile.prettify()))
    writef.close()
    file.close()

def remove_title():
    file = open('destfile.html', 'r')    
    domfile = bs4.BeautifulSoup(file.read())
    title = re.sub(r'(\s\s+)',r' ', domfile('title')[0].extract().get_text())
    #gets the second table in text which contains the bill. 
    domfile = domfile('table')[1].extract()
    #gets the first sentence of the bill.
    for x in domfile('td'):
        chkstring = x.get_text() #TODO ask mark if he wants the text extracted.
        b = re.search('[.]',chkstring)
        title += re.sub(r'(\s\s+)',r' ', chkstring) 
        if b is not None:
            break
    writef = open('destfile.html', 'w')
    writef.write(domfile.prettify())
    writef.close()
    return title
    
def consolidate_tag():
    #some consolidation.

def main():
    remove_empty_tag()
    title = remove_title()
    print([title])
    
main()