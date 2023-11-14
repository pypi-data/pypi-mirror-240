# file version 0.0.1
# made
# by 
# culty


# imports
import cloudscraper as cloud
import json, time


# scraper
scraper = cloud.create_scraper()

headers = '{"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"}'

class milo:
  def __init__(self):
    self.url = "https://www.google.com/"
    
  # connect milo.connect
  def connect(self, headers=None, timeout=None): # with headers
    try:
      r = scraper.get(self, headers=headers, timeout=timeout, verify=True)
      r.raise_for_status()
      return r
    except Exception as e:
      return e

  # connect milo.connect
  def get(self, headers=None, timeout=None): # with headers
    try:
      r = scraper.get(self, headers=headers, timeout=timeout, verify=True)
      r.raise_for_status()
      return r
    except Exception as e:
      return e

  # connect milo.connect
  def con(self, headers=None, timeout=None): # with headers
    try:
      r = scraper.get(self, headers=headers, timeout=timeout, verify=True)
      r.raise_for_status()
      return r
    except Exception as e:
      return e

  # json decoder
  def decode(self):
    try:
      self = self.json()
      return self
    except Exception as e:
      return e

  # json decoder
  def json_decode(self):
    try:
      self = self.json()
      return self
    except Exception as e:
      return e

  # sleep thing
  def sleep(self):
    try:
      time.sleep(self)
      return f"sleeped for time {self} Second"
    except Exception as e:
      return e

  # made by culty have fun
