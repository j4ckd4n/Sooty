from Plugins import Plugin

import os, requests


class VirusTotal(Plugin.Plugin):
  def __init__(self, value: str = None, name: str = 'VirusTotal'):
    super().__init__(name)

    self._api_key = os.getenv("VT_API_TOKEN")
    self._vt_url = "https://www.virustotal.com/vtapi/v2/file/report"

    self._options = {
      0: {
        "name": "Hash Reputation Lookup",
        "run": lambda: self._hashRating()
      },
      1: {
        "name": "Hash Details",
        "run": lambda: self._hashDetails()
      }
    }

  def _hashRating(self):
    fileHash = input(" Enter Hash of File: ").strip()

    params = {'apikey': self._api_key, 'resource': fileHash}
    response = requests.get(self._vt_url, params=params)

    try:
      result = response.json()
      if result['response_code'] == 0:
        print("\n Hash was not found in Malware Database")
      elif result['response_code'] == 1:
        print(" VirusTotal Report: %d/%d detections found" % (result['positives'], result['total']))
        print("   Report Link: https://www.virustotal.com/gui/file/%s/detection" % fileHash)
    except Exception as e:
      print(e)

  def _hashDetails(self):
    fileHash = input(" Enter Hash of File: ").strip()

    params = {'apikey': self._api_key, 'resource': fileHash}
    response = requests.get(self._vt_url, params=params)

    try:
      result = response.json()
      if result['response_code'] == 0:
        print("\n Hash was not found in Malware Database")
      elif result['response_code'] == 1:
        print("\n Scan Date: %s" % result['scan_date'])
        print(" Permalink: %s" % result['permalink'] )
        print(" Hashes:\n\t MD5: %s\n\t SHA-1: %s\n\t SHA-256: %s\n" % (result['md5'], result['sha1'], result['sha256']))
        
        print(" AV Lookups:")
        scans = result['scans']
        for scan in scans.keys():
          if scans[scan]['detected'] == True:
            print("\t %s\n\t\t Result: %s\n\t\t Version: %s" % (scan, scans[scan]['result'], scans[scan]['version']))
        
        print()
    except Exception as e:
      print(e)

  def run(self):
    if self._api_key == None:
      print(" No API key found. Define it as an environment 'VT_API_TOKEN'.")
      return

    print("\n --------------------------------- ")
    print("\n        V I R U S T O T A L        ")
    print("\n --------------------------------- ")
    print(" What would you like to do? \n")
    for item in self._options.keys():
      print(f" OPTION {item}: {self._options[item]['name']}")
    val = int(input(">> "))
    if val not in self._options:
      print("Invalid value specified")
      self.run()
    else:
      self._options[val]['run']()