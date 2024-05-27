#!/usr/bin/python3
import sys
import BSSIDApple_pb2
import pycurl
from io import BytesIO

if __name__ == "__main__":
  bssid = sys.argv[1]
  s1 = "%s%s%s%s%s*%scom.apple.Maps" % (chr(18), chr(19), chr(10), chr(17), bssid, chr(14))
  data = "\x00\x01\x00\x05"+"en_US"+"\x00\x00\x00\x09"+"5.1.9B176"+"\x00\x00\x00\x01\x00\x00\x00" + chr(len(s1)) + s1

  c = pycurl.Curl()
  c.setopt(pycurl.URL, 'https://gs-loc.apple.com/clls/wloc')
  b = BytesIO()
  c.setopt(c.WRITEFUNCTION, b.write)
  c.setopt(c.POSTFIELDS, data)
  c.perform()
  c.close()

  liste_wifi = BSSIDApple_pb2.BlockBSSIDApple()
  liste_wifi.ParseFromString(b.getvalue()[10:])
  print(liste_wifi)

