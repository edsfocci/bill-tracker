from urllib import request
from os.path import isfile
import re

from annotation_app.helpers.bill_scrapers import scrape_bill_text


save_path = 'search/Bills-TX_84R/'

# Hardcoded session
session = '84R'


### Helper function
# ftpopen is not 100% reliable on first try
def keep_trying_ftpopen(url, tries=10):
  # TODO: figure out optimal number of 'tries'

  # One last try, allow exception
  if tries <= 1:
    with request.urlopen(url) as response:
      data = response.read()

    return data

  try:
    with request.urlopen(url) as response:
      data = response.read()

    return data

  except:
    return keep_trying_ftpopen(url, tries=tries-1)


def bill_search_history_crawler(session):
  # example full URL:
  # 'ftp://ftp.legis.state.tx.us/bills/84R/billhistory/house_bills/HB00001_HB00099/'
  bill_hist_url_unformatted = 'ftp://ftp.legis.state.tx.us/bills/' +\
    '{0}/billhistory/{1}_bills/'

  chambers = ['senate', 'house']
  for chamber in chambers:
    # Abbreviate chamber for chamber_origin data later
    ch_abbr = chamber[0].upper()

    # Get list of directory paths in bill_history chamber folder
    bill_hist_chamber_url = bill_hist_url_unformatted.format(session, chamber)
    response = str(keep_trying_ftpopen(bill_hist_chamber_url))

    bill_hist_folder_urls = response.split('\\r\\n')[:-1]
    bill_hist_folder_urls = map(lambda x: bill_hist_chamber_url + x[-15:] + '/',
      bill_hist_folder_urls)

    # Grab bill_history data from each directory within bill_history path
    for bill_hist_folder_url in bill_hist_folder_urls:

      # Get bill_history filenames
      response = str(keep_trying_ftpopen(bill_hist_folder_url))
      for line in response.split('\\r\\n')[:-1]:
        filename_regex = re.search(r'[S,H]B (\d+)\.xml$', line)
        filename = filename_regex.group(0)

        if not isfile(save_path + filename):

          # Get XML data
          response = keep_trying_ftpopen(bill_hist_folder_url + filename)
          with open(save_path + filename, 'w') as bill_xml_file:
            bill_xml_file.write(response.decode("utf-8"))

        # Get bill_text
        input = {
          'session': session,
          'chamber_origin': ch_abbr,
          'number': int(filename_regex.group(1))
        }
        bill_text, bill_text_filename = scrape_bill_text(input)

        if not isfile(save_path + bill_text_filename):
          with open(save_path + bill_text_filename, 'w') as bill_text_file:
            bill_text_file.write(bill_text.decode("utf-8"))


### Execution
bill_search_history_crawler(session)

### Speed test
# from timeit import Timer
# t = Timer(lambda: bill_search_history_crawler(session))
# print(t.timeit(number=1))
