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
    title = domfile('title')[0].extract().get_text()
    #gets the second table in text which contains the bill. 
    domfile = domfile('table')[1].extract()
    #gets the first sentence of the bill.
    for x in domfile('td')[:10]:
        chkstring = x.get_text() #TODO ask mark if he wants the text extracted.
        b = re.search('\.',chkstring)
        if b is not None:  
            break
        title += chkstring
    writef = open('destfile.html', 'w')
    writef.write(domfile.prettify())
    return title

def main():
    remove_empty_tag()
    title = remove_title()
    print(title)
    
main()