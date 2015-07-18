#####
# Bill scrapers
# -----
# All the public functions do is scrape,
# no processing (except converting xml to dict whenever possible;
# minor processing)

from urllib import request
import re, xmltodict

# Deprecated: will be removed after July 2015
from annotation_app.helpers import std as STD


### Helper function
# ftpopen is not 100% reliable on first try
def keep_trying_ftpopen(url, tries=7):
  # TODO: figure out optimal number of 'tries'

  # One last try, return None if fail
  if tries <= 1:
    try:
      with request.urlopen(url) as response:
        return response.read()
    except:
      return

  try:
    with request.urlopen(url) as response:
      return response.read()
  except:
    return keep_trying_ftpopen(url, tries=tries-1)


### Public functions

# INPUT: initial_data format:
# {'session': '84R', 'chamber_origin': 'S', 'number': 5}

# OUTPUT: bill_text, FORMAT: byte_string
#   If not found, return None

def scrape_bill_text(initial_data):
  bill_data = initial_data

  # example full URL:
  # 'ftp://ftp.legis.state.tx.us/bills/833/billtext/HTML/house_bills/HB00001_HB00099/HB00010I.HTM'
  bill_text_files_url_unformatted = 'ftp://ftp.legis.state.tx.us/bills/' +\
    '{0}/billtext/HTML/{1}_bills/{2}B{3}0{4}_{2}B{3}99/'

  bill_text_filename_unformatted = '{0}B{1}\w.HTM$'

  # Are you looking for Senate Bills (SB) or House Bills (HB)?
  ch_abbr = bill_data['chamber_origin']
  if ch_abbr == 'S':
    chamber = 'senate'
  elif ch_abbr == 'H':
    chamber = 'house'
  else:
    return

  # Get proper bill_text_file_url
  bill_number = str(bill_data['number'])
  if bill_data['number'] > 99:
    bill_text_files_url = bill_text_files_url_unformatted.format(
      bill_data['session'], chamber, ch_abbr, bill_number[:-2].zfill(3), 0)
  else:
    bill_text_files_url = bill_text_files_url_unformatted.format(
      bill_data['session'], chamber, ch_abbr, '000', 1)

  bill_text_filename_regex = bill_text_filename_unformatted.format(
    ch_abbr, bill_number.zfill(5))

  # Parse folder structure for latest version of bill_text
  response = keep_trying_ftpopen(bill_text_files_url)
  if response == None:
    return response

  response = str(response)[2:]
  response = response.split('\\r\\n')[:-1]
  files = list(STD.filterr(lambda x: re.search(bill_text_filename_regex, x,
    re.IGNORECASE), response))

  # If len(files) is 0, no files found
  if len(files) == 0:
    return

  from datetime import date
  def map_dates_and_filenames(text):
    matches = re.search('^(\d+)-(\d+)-(\d+).+' + '(' +\
      bill_text_filename_regex[:-1] + ')$', text, re.IGNORECASE)
    bill_date = date(year=int(matches.group(3))+2000,
      month=int(matches.group(1)), day=int(matches.group(2)))
    return [bill_date, matches.group(4)]

  # Wizardry to actually get the latest filename
  files = list(STD.mapp(map_dates_and_filenames, files))
  bill_text_filename = STD.maxx(files, key=lambda x: x[0])[1]

  # Get bill text (finally!)
  return keep_trying_ftpopen(bill_text_files_url + bill_text_filename)


# INPUT: initial_data format:
# {'session': '84R', 'chamber_origin': 'S', 'number': 5}

# OUTPUT: bill_history, FORMAT: dict
#   If not found, return None

def scrape_bill_history(initial_data):
  bill_data = initial_data

  # example full URL:
  # 'ftp://ftp.legis.state.tx.us/bills/84R/billhistory/senate_bills/SB00001_SB00099/SB 10.xml'
  bill_hist_file_url_unformatted = 'ftp://ftp.legis.state.tx.us/bills/' +\
    '{0}/billhistory/{1}_bills/{2}B{3}0{5}_{2}B{3}99/{2}B {4}.xml'

  # Are you looking for Senate Bills (SB) or House Bills (HB)?
  ch_abbr = bill_data['chamber_origin']
  if ch_abbr == 'S':
    chamber = 'senate'
  elif ch_abbr == 'H':
    chamber = 'house'
  else:
    return

  # Get proper bill_hist_file_url
  bill_number = str(bill_data['number'])
  if bill_data['number'] > 99:
    bill_hist_file_url = bill_hist_file_url_unformatted.format(
      bill_data['session'], chamber, ch_abbr, bill_number[:-2].zfill(3),
      bill_number, 0)

  else:
    bill_hist_file_url = bill_hist_file_url_unformatted.format(
      bill_data['session'], chamber, ch_abbr, '000', bill_number, 1)

  # Get XML data
  response = keep_trying_ftpopen(bill_hist_file_url)
  if response == None:
    return response

  return xmltodict.parse(str(response)[14:-1])['billhistory']

  # Get only data I want
  # bill_data['caption'] = data['caption']['#text']
  # bill_data['history_url'] = bill_hist_file_url


# input = {'session': '84R', 'chamber_origin': 'S', 'number': 5}
### Testers
def scrape_bill_text_test():
  return scrape_bill_text(
    {'session': '84R', 'chamber_origin': 'S', 'number': 5})

def scrape_bill_history_test():
  return scrape_bill_history(
    {'session': '84R', 'chamber_origin': 'S', 'number': 5})


### Speed test
def speedtest():
  from timeit import Timer
  t = Timer(lambda: scrape_bill_history_test())
  print(t.timeit(number=1))
