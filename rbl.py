#!/usr/bin/env python
# coding=utf-8
#
# Quick-and-dirty(tm) Python script to check a set of IPv4 addresses against known RBLs
#

__author__ = "Alexandre Dulaunoy"
__copyright__ = "Copyright 2017, Alexandre Dulaunoy"
__license__ = "AGPL version 3"
__version__ = "0.1"

import sys
import argparse
import json
import datetime

try:
    import dns.resolver
    resolver = dns.resolver.Resolver()
    resolver.timeout = 0.2
    resolver.lifetime = 0.2
except:
    print('dnspython3 is missing, pip install dnspython3')
    sys.exit(0)

parser = argparse.ArgumentParser(description='multi-rblcheck\nA simple script to test a list of IP addresses against RBLs.\n The output is a JSON object per IP address.')
parser.add_argument("-d","--debug", default=False, action='store_true', help='Include debug message')
parser.add_argument("-t", "--test", default=False, action='store_true')
parser.add_argument("-i", "--ip", default=None, action='append', required=True, help='IPv4 address to check against the RBLs (one or more IP addresses)')
parser.add_argument("-a", "--all",  default=False, action='store_true', help='Include unlisted results')
args = parser.parse_args()

if args.test:
    args.ip = ['127.0.0.1']

rbls = {
 'spam.spamrats.com': 'http://www.spamrats.com',
 'spamguard.leadmon.net': 'http://www.leadmon.net/SpamGuard/',
 'rbl-plus.mail-abuse.org': 'http://www.mail-abuse.com/lookup.html',
 'web.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'ix.dnsbl.manitu.net': 'http://www.dnsbl.manitu.net',
 'virus.rbl.jp': 'http://www.rbl.jp',
 'dul.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'bogons.cymru.com': 'http://www.team-cymru.org/Services/Bogons/',
 'psbl.surriel.com': 'http://psbl.surriel.com',
 'misc.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'httpbl.abuse.ch': 'http://dnsbl.abuse.ch',
 'combined.njabl.org': 'http://combined.njabl.org',
 'smtp.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'korea.services.net': 'http://korea.services.net',
 'drone.abuse.ch': 'http://dnsbl.abuse.ch',
 'rbl.efnetrbl.org': 'http://rbl.efnetrbl.org',
 'cbl.anti-spam.org.cn': 'http://www.anti-spam.org.cn/?Locale=en_US',
 'b.barracudacentral.org': 'http://www.barracudacentral.org/rbl/removal-request',
 'bl.spamcannibal.org': 'http://www.spamcannibal.org',
 'xbl.spamhaus.org': 'http://www.spamhaus.org/xbl/',
 'zen.spamhaus.org': 'http://www.spamhaus.org/zen/',
 'rbl.suresupport.com': 'http://suresupport.com/postmaster',
 'db.wpbl.info': 'http://www.wpbl.info',
 'sbl.spamhaus.org': 'http://www.spamhaus.org/sbl/',
 'http.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'csi.cloudmark.com': 'http://www.cloudmark.com/en/products/cloudmark-sender-intelligence/index',
 'rbl.interserver.net': 'http://rbl.interserver.net',
 'ubl.unsubscore.com': 'http://www.lashback.com/blacklist/',
 'dnsbl.sorbs.net': 'http://www.sorbs.net',
 'virbl.bit.nl': 'http://virbl.bit.nl',
 'pbl.spamhaus.org': 'http://www.spamhaus.org/pbl/',
 'socks.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'short.rbl.jp': 'http://www.rbl.jp',
 'dnsbl.dronebl.org': 'http://www.dronebl.org',
 'blackholes.mail-abuse.org': 'http://www.mail-abuse.com/lookup.html',
 'truncate.gbudb.net': 'http://www.gbudb.com/truncate/index.jsp',
 'dyna.spamrats.com': 'http://www.spamrats.com',
 'spamrbl.imp.ch': 'http://antispam.imp.ch',
 'spam.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'wormrbl.imp.ch': 'http://antispam.imp.ch',
 'query.senderbase.org': 'http://www.senderbase.org/about',
 'opm.tornevall.org': 'http://dnsbl.tornevall.org',
 'netblock.pedantic.org': 'http://pedantic.org',
 'access.redhawk.org': 'http://www.redhawk.org/index.php?option=com_wrapper&Itemid=33',
 'cdl.anti-spam.org.cn': 'http://www.anti-spam.org.cn/?Locale=en_US',
 'multi.surbl.org': 'http://www.surbl.org',
 'noptr.spamrats.com': 'http://www.spamrats.com',
 'dnsbl.inps.de': 'http://dnsbl.inps.de/index.cgi?lang=en',
 'bl.spamcop.net': 'http://bl.spamcop.net',
 'cbl.abuseat.org': 'http://cbl.abuseat.org',
 'dsn.rfc-ignorant.org': 'http://www.rfc-ignorant.org/policy-dsn.php',
 'zombie.dnsbl.sorbs.net': 'http://www.sorbs.net',
 'dnsbl.njabl.org': 'http://dnsbl.njabl.org',
 'relays.mail-abuse.org': 'http://www.mail-abuse.com/lookup.html',
 'rbl.spamlab.com': 'http://tools.appriver.com/index.aspx?tool=rbl',
 'all.bl.blocklist.de': 'http://www.blocklist.de/en/rbldns.html'
}


def checkAll(ip=None):
    if ip is None:
        return None
    results = {}
    results['query'] = ip
    results['date'] = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    results['listed'] = []
    results['info'] = []
    results['not_listed'] = []
    for rbl in rbls:
      ipRev =  '.'.join(ip.split('.')[::-1])
      query = ipRev+'.'+rbl
      if args.debug:
        print ('{}'.format(query))
      try:
        resolver.query(query,'A')
        try:
            txt = resolver.query(query, 'TXT')
        except:
            results['listed'].append(query)
        results['listed'].append(query)
        results['info'].append(str(txt[0]))
      except:
        if args.all:
            results['not_listed'].append(query)
    return results

for ip in args.ip:
    print (json.dumps(checkAll(ip=ip)))
