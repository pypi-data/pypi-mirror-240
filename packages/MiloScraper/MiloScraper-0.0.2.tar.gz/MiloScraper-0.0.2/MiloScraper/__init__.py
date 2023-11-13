#
#
#
#
#
#


import cloudscraper as cloud
import json

scraper = cloud.create_scraper()

class milo:
  def __init__(self):
    self.headers = '{"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"}'
    self.url = "https://www.google.com/"

    
  def connect(url, headers=None, timeout=None):
    headers = headers
    try:
      r = scraper.get(url, headers=headers, timeout=timeout, verify=True)
      r.raise_for_status()
      return r
    except Exception as e:
      return e

  def decode(a):
    try:
      a = a.json()
      return a
    except Exception as e:
      return e
