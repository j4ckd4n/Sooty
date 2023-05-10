from Plugins import Plugin

import socket

class ReverseDNSLookup(Plugin.Plugin):
  def __init__(self, ip: str = None, name: str = 'ReverseDNSLookup'):
    super().__init__(name)
    self._ip = ip

  def run(self):
    if self._ip == None:
      self._ip = input(' Enter IP to check: ').strip()

    try:
      s = socket.gethostbyaddr(self._ip)
      print('\n %s' % s[0])
    except:
      print(" Reverse Lookup for '%s' did not return a value." % s)
