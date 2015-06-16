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
        # removes the tags with just space in them.
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
        #replaces weird spaces with normal spacing. 
        title += re.sub(r'(\s\s+)',r' ', chkstring) 
        if b is not None:#stops the loop when a period is found. 
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
        for x in i.children:
            if type(x) == bs4.element.NavigableString and len(x) <= 1:
                x.extract()
    for i in lines(tags[3]):
        i.unwrap()

    for i in lines(tags[4]):
        #find out if tag has siblings. 
        if len(i.find_next_siblings()) > 0:
            # if there are siblings see if their tag is the same
            for x in i.find_next_siblings():
                # if the name is the the same then remove the text and place inside tag.
                if x.name == i.name:
                    i.append(x.extract().get_text())

    file = open('destfile.html', 'w')
    file.write(lines.prettify())#Adds whitespace back in for formatting. 
    file.close()

def add_tags():
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    sec = re.compile("\A(SECTION)")
    sec1 =  re.compile("\A(Sec)")
    sec3 = re.compile("\A(SUBCHAPTER)")
    sec4 = re.compile("\A(\(.\))(?!\s\(.\))")

    regcheck = [[sec, 'SECTION', "p" ], [sec1, "Sec", 'p' ],[sec3,"Subchapter", "p"],[sec4, "list", "li" ]]

    #find each expression and add the classes above to it.
    for x in regcheck:#TODO google double for
        for i in lines('tr'):
            #check what the first word is
            if re.search(x[0], list(i.stripped_strings)[0]):
                i.name = x[2]
                i['class'] = x[1]
    print(type(lines("tr")[3].previous_sibling), len(lines("tr")[3].previous_sibling))
    file = open('destfile.html', 'w')
    file.write(lines.prettify())#Adds whitespace back in for formatting. 
    file.close()

    


def main():
    remove_empty_tag()
    title = remove_title()
    consolidate_tag()
    add_tags()
    file = open('destfile.html', 'r')    
    lines = bs4.BeautifulSoup(file.read())
    file.close()
    print('inmain')
main()
