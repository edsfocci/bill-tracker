import bs4, re, itertools, collections

file = open('destfile.html', 'r')    
lines = bs4.BeautifulSoup(file.read())
file.close()


'''
SECTION

Sec
(1)
(a)
SUBCHAPTER

dont get

Subchapter
Section
section
(x) (x) or (x)(X)

'''

#create regex for each of the situations above 

sec = re.compile("\A(SECTION)")
sec1 =  re.compile("\A(Sec)")
sec3 = re.compile("\A(SUBCHAPTER)")
sec4 = re.compile("\A(\(.\))(?!\s\(.\))")
"\A(\(.\))(?!\(.\))"

regcheck = [[sec, 'SECTION', "p" ], [sec1, "Sec", 'p' ],[sec3,"Subchapter", "p"],[sec4, "list", "li" ]]

#find each expression and add the classes above to it.

#print(re.search(sec, list(lines("tr")[-4].stripped_strings)[0]))
for x in regcheck:#TODO google double for
	for i in lines('tr'):
	        #check what the first word is
	        if re.search(x[0], list(i.stripped_strings)[0]):
	            i.name = x[2]
	            i['class'] = x[1]
	            print(i)