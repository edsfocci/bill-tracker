import bs4, re


class html_cleanup():

  def __init__(self):
    self.text = None
    self.sec = re.compile("\A(SECTION)")
    self.sec1 =  re.compile("\A(Sec)")
    self.sec3 = re.compile("\A(SUBCHAPTER)")
    self.sec4 = re.compile("\A(\(.\))(?!\s?\(.\))")
    self.regcheck = [[self.sec, 'SECTION', "p"], [self.sec1, "Sec", 'p'],
      [self.sec3, "Subchapter", "p"], [self.sec4, "list", "li"]]
    self.title = None


  def set_text(self, text):
    self.text = bs4.BeautifulSoup(text)


  def remove_space(self, tag):
    for x in (list(self.text(tag)[0].next_siblings) +\
      list(self.text(tag)[0].previous_siblings)):
        if type(x) == bs4.element.NavigableString:
          x.extract()


  def remove_empty_tag(self):
    taglist = list(map(lambda x: x.name, self.text.find_all(True)))
    taglist = list(set(taglist))

    for tag in taglist:
      i = 0
      text_tag_length = len(self.text(tag))

      # removes the tags with just space in them.
      while i < (text_tag_length):
        if self.text(tag)[i].getText().isspace():
          self.text(tag)[i].decompose()
          text_tag_length -= 1
        else:
          i += 1


  def remove_title(self):
    self.title = re.sub(r'(\s\s+)', r' ',
      self.text('title')[0].extract().get_text())

    # Gets the second table in text which contains the bill.
    self.text = self.text('table')[-1].extract()

    # Gets the first sentence of the bill.
    for x in self.text('td'):
      chkstring = x.get_text() # TODO: Ask Mark if he wants the text extracted.
      b = re.search('[.]',chkstring)
      # Replaces weird spaces with normal spacing.
      self.title += re.sub(r'(\s\s+)',r' ', chkstring)
      if b is not None: # Stops the loop when a period is found.
        break


  def consolidate_tag(self, rem, tag):

    def rm_tag_str_parent(tag):
      for i in self.text(tag):
        i.unwrap()


    def rm_tag_str_dif_sib(tag):
      # Removes tr tags and puts their strings into other tags.
      for y in self.text(tag):
        first_element = True

        while y.previous_sibling and y.previous_sibling.name != tag:
          first_element = False
          m = y.previous_sibling
          y.extract()
          string_list = list(y.contents)
          for q in string_list:
            m.append(q)

        if first_element:
          y.name = 'p'


    def rm_tag_str_same_sib(tag):
      for i in self.text(tag):
        # Find out if tag has siblings.
        if i.find_next_siblings():
          # If there are siblings see if their tag is the same
          for x in i.find_next_siblings():
            # If the name is the the same
            # then remove the text and place inside tag.
            if x.name == i.name:
              i.append(x.extract().get_text())


    if rem == 'parent':
      rm_tag_str_parent(tag)
    elif rem == 'sibling same name':
      rm_tag_str_same_sib(tag)
    elif rem == 'sibling different name':
      rm_tag_str_dif_sib(tag)
    else:
      print('Must specify how you want to remove the tag.')


  def add_tags(self, tag):
    # Find each expression and add the classes in the set to it.
    for x in self.regcheck:
      for i in self.text(tag):
        #check what the first word is
        if re.search(x[0], list(i.stripped_strings)[0]):
          i.name = x[2]
          i['class'] = x[1]


  def remove_allspaces(self):
    self.output = self.text.prettify()
    self.output = self.output.split()
    self.output = ' '.join(self.output)
    self.output = re.sub(r'\{.+\}\s*', '', self.output)


def htmltext(text):
  ttobj = html_cleanup()
  #set text
  ttobj.set_text(text)
  #remove empty tag
  ttobj.remove_empty_tag()
  #consolidate tag same sib u
  ttobj.consolidate_tag('sibling same name', 'u')
  #consolidate tag parent td
  ttobj.consolidate_tag('parent', 'td')
  #remove title
  ttobj.remove_title()
  #remove space
  ttobj.remove_space('tr')
  #add tags
  ttobj.add_tags('tr')
  #consolidate tag diff sib tr
  ttobj.consolidate_tag('sibling different name', 'tr')
  ttobj.remove_allspaces()
  return ttobj.output
