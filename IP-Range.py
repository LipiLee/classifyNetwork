#!/usr/bin/env python

import httplib, urllib, sys

params = urllib.urlencode({'query': sys.argv[1]})
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
conn = httplib.HTTPConnection("whois.kisa.or.kr")
conn.request("POST", "/kor/whois.jsc", params, headers)
response = conn.getresponse()
lines = response.read().split('\n')
for line in lines:
  if 'CIDR' in line:
    print sys.argv[1], line.split(':')[1].strip()
    break
conn.close()
