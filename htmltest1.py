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

a = re.search(sec4, "(x)")
print(a)