import bs4, re, itertools, collections


#find tr
#Make a list of prev siblings
#go back to the first one with a name
#check if its tr if so consoliidate and name it p

def remove_space(tag):
	file = open('destfile.html', 'r')    
	lines = bs4.BeautifulSoup(file.read())
	file.close()
	for x in (list(lines(tag)[0].next_siblings) + list(lines(tag)[0].previous_siblings)):
		if type(x) == bs4.element.NavigableString:
			x.extract()
	return lines

def consolidate_tag(rem, tag):
	if rem == 'parent':
		lines = rm_tag_str_parent(tag)
	elif rem == 'sibling same name':
		lines = rm_tag_str_same_sib(tag)
	elif rem == 'sibling different name':
		lines = rm_tag_str_dif_sib(tag)
	else:
		print('Must specify how you want to remove the tag.')
	return(lines)
def rm_tag_str_parent(tag):
	lines = remove_space(tag)
	for i in lines(tag):
		i.unwrap()
	return(lines)
def rm_tag_str_dif_sib(tag):
	lines = remove_space(tag)
	for y in lines(tag): #removes tr tags and puts their strings into other tags.
		firstele = True
		while y.previous_sibling and y.previous_sibling.name != tag:
			firstele = False
			y.previous_sibling.string = y.previous_sibling.string + y.string
			m = y.previous_sibling
			y.decompose()
		if firstele:
			y.name = 'p'
	return(lines)

def rm_tag_str_same_sib(tag):
	lines = remove_space(tag)
	for i in lines(tag):
		#find out if tag has siblings. 
		if i.find_next_siblings():
			# if there are siblings see if their tag is the same
			for x in i.find_next_siblings():
				# if the name is the the same then remove the text and place inside tag.
				if x.name == i.name:
					i.append(x.extract().get_text())
	return(lines)

lines = remove_space('tr')
a = list()
for ele in lines.find_all(True):
	a.append(ele.name)
print(set(a))

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