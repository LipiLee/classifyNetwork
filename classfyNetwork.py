#!/usr/bin/env python

import urllib2
import xml.etree.ElementTree as ET

f = open('Address.list', 'r')
for url in f:
  try:
    xml = urllib2.urlopen(url).read()
    root = ET.fromstring(xml)
    # FIXME garbage HTTP address is added in node name
    # check ElementTree.py
    for netRef in root.iter('{http://www.arin.net/whoisrws/core/v1}netRef'):
      start = netRef.get('startAddress')
      end = netRef.get('endAddress')
      print url, start, end
  except Exception:
    pass
