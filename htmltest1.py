import bs4, re, itertools, collections

file = open('destfile.html', 'r')    
lines = bs4.BeautifulSoup(file.read())
file.close()

#find tr
#Make a list of prev siblings
#go back to the first one with a name
#check if its tr if so consoliidate and name it p

count = 0
a = list(lines('li')[0].previous_siblings)+list(lines('li')[0].next_siblings)
b =list(lines('tr')[0].previous_siblings) + list(lines('tr')[0].next_siblings)
print('is a b', len(a) == len(b))
print(len(list(lines('li')[0].next_siblings) + list(lines('li')[0].previous_siblings)))
for x in (list(lines('tr')[0].next_siblings) + list(lines('tr')[0].previous_siblings)):
	print('"',x,"'")
	print(len(list(lines('tr')[0].next_siblings)))
	if type(x) == bs4.element.NavigableString:
		print('extracting')
		x.extract()

print('outside for', len(list(lines('li')[0].next_siblings) + list(lines('li')[0].previous_siblings)))

l = list(lines('li')[0].previous_siblings)+list(lines('li')[0].next_siblings)


for y in lines('tr'): #removes tr tags and puts their strings into other tags.
	firstele = True
	while y.previous_sibling and y.previous_sibling.name != 'tr':
		firstele = False
		y.previous_sibling.string = y.previous_sibling.string+y.string
		m = y.previous_sibling
		y.decompose()
	if firstele:
		y.name = 'p'
print(lines.prettify())
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
''''
#create regex for each of the situations above 

sec = re.compile("\A(SECTION)")
sec1 =  re.compile("\A(Sec)")
sec3 = re.compile("\A(SUBCHAPTER)")
sec4 = re.compile("\A(\(.\))(?!\s?\(.\))")

regcheck = [[sec, 'SECTION', "p" ], [sec1, "Sec", 'p' ],[sec3,"Subchapter", "p"],[sec4, "list", "li" ]]

#find each expression and add the classes above to it.

#print(re.search(sec, list(lines("tr")[-4].stripped_strings)[0]))
for x in regcheck:#TODO google double for
	for i in lines('tr'):
		print('1-------------------------------')
		print(i)
		#check what the first word is
		if re.search(x[0], list(i.stripped_strings)[0]):
			i.name = x[2]
			i['class'] = x[1]
			i.append(lines('tr')[0].unwrap())
			print('2-------------------------------')
			print(i)

'''''