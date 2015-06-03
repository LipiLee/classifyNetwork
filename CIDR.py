#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET

f = open('Detail.list', 'r')
for url in f:
  try:
    xml = urllib2.urlopen(url).read()
    root = ET.fromstring(xml)
    # FIXME garbage HTTP address is added in node name
    # check ElementTree.py
    for netBlock in root.iter('{http://www.arin.net/whoisrws/core/v1}netBlock'):
      cidrLength = netBlock.find('{http://www.arin.net/whoisrws/core/v1}cidrLength').text
      start = netBlock.find('{http://www.arin.net/whoisrws/core/v1}startAddress').text
      print url, start + '/' +  cidrLength 
  except Exception:
    pass
