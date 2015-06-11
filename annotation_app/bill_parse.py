import re
import bs4
import requests

class Bill_Import():

    def __init__(self):
        #bool for issenate or ishouse
        self.bill_number = str
        self.issenate = True #TODO fix this hard coding. 
        self.ishouse = False
        self.url = {'billurl' : ['http://www.capitol.state.tx.us/tlodocs/84R/billtext/html/','.htm'],
                    'sections' : ["http://www.capitol.state.tx.us/BillLookup/",".aspx?LegSess=84R&Bill="]}
        self.endchar = ["I", "S", "E", "H", "F"] #TODO breaks if bill is introduced house
        self.rawauthors = 'string'
        self.rawhistory = 'string'
        #outside vars
        self.billtext = list()
        self.subjects = list()
        self.authors = list()
        self.coauthors = list()
        self.cosponsors = list()
        self.sponsors = list()
        self.title = list()
    def set_bill_num(self, num):
        num = str(num)
        if not num.isalnum():
            print('error must be a number')
        else:
            self.bill_number = num
    def get_bill_num(self):
        return self.bill_number
    #function for setting if the bill is senate or house
    def set_sen_rep(self,sen,rep):
        if sen == rep:
            print('Bill must originate in either house or senate')
        elif sen:
            self.issenate = True
        else:
            self.ishouse = True

    def pull_billtext(self):
        if self.issenate:
            chamber = 'SB'
        else:
            chamber = 'HB'
        x = 0
        while x < 5:
            path = self.url['billurl'][0]+  chamber + self.bill_number.zfill(5) + self.endchar[x] + self.url['billurl'][1]
            x += 1
            res = requests.get(path)
            if not res.status_code == requests.codes.ok:
                print('not a vaild bill!')
                break
            self.billtext.append(res.text)
            
    def remove_empty_tag(self):
        print('empty tag func')
        taglist = ['td','tr','u']
        domfile = bs4.BeautifulSoup(self.billtext[-1])
        for x in range(len(taglist)):
            i = 0
            while i < (len(domfile(taglist[x]))):
                #print(taglist[x])
                if domfile(taglist[x])[i].getText().isspace():
                    domfile(taglist[x])[i].extract()
                else:
                    i +=1
        a = domfile.prettify()
        self.billtext[-1] = a

    def get_title(self):
        domfile = bs4.BeautifulSoup(self.billtext[-1])
        title1 = re.sub(r'(\s\s+)',r' ', domfile('title')[0].extract().get_text())
        #gets the second table in text which contains the bill. 
        domfile = domfile('table')[1].extract()
        #gets the first sentence of the bill.
        for x in domfile('td'):
            chkstring = x.get_text() #TODO ask mark if he wants the text extracted.
            b = re.search('[.]',chkstring)
            title1 += re.sub(r'(\s\s+)',r' ', chkstring) #strips repeated whitespace
            if b is not None:
                break
        self.title = [title1]
    
    def pull_history(self):
        if self.issenate:
            chamber = 'SB'
        else:
            chamber = 'HB'
        path = self.url['sections'][0]+'History'+self.url['sections'][1]+chamber+self.bill_number
        rawhtml = requests.get(path)
        self.rawhistory = bs4.BeautifulSoup(rawhtml.text)

    def set_subjects(self):
        td = self.rawhistory.find('td', {'id': 'cellSubjects'}).getText()
        regex = re.compile(".*?\((.*?)\)")
        # Find all the strings between (...) - parenthesis
        result = re.findall(regex, td)
        # Delete the content between the parenthesis
        for par in result:
          td = td.replace(par, "")
        subjects_list = td.split("()")
        # Skip last element (it's an empty string anyway)
        subjects_list = subjects_list[:len(subjects_list)-1]
        self.subjects = subjects_list
    def set_data(self):
        self.set_author()
        self.set_coauthor()
        self.set_sponsors()
        self.set_cosponsors()
        
    def set_author(self):
        self.authors = self.check_empty('cellAuthors')
    def set_coauthor(self):
        self.coauthors = self.check_empty('cellCoauthors')
    def set_sponsors(self):
        self.sponsors = self.check_empty('cellSponsors')
    def set_cosponsors(self):
        self.cosponsors = self.check_empty('cellCosponsors')
    
    def check_empty(self, cellid):
        #Fixed error where it breaks when there is no text in the field. 
        
        if self.rawhistory.find('td',id = cellid) ==  None:
            print('noneif')
            return ['']
        else:
            self.rawhistory.find('td',id = cellid).getText()
            text = self.rawhistory.find('td',id = cellid).getText().split('|')
            return text
       
newbill = Bill_Import()
newbill.bill_number = '15'
newbill.pull_billtext()
newbill.remove_empty_tag()
newbill.get_title()
print(newbill.title)