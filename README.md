# multi-rblcheck

multi-rblcheck is a Python script to test a list of IP addresses against RBLs.

The output is a JSON object per IP address.

# Usage

~~~~
usage: rbl.py [-h] [-d] [-t] -i IP [-a]

multi-rblcheck A simple script to test a list of IP addresses against RBLs.
The output is a JSON object per IP address.

optional arguments:
  -h, --help      show this help message and exit
  -d, --debug     Include debug message
  -t, --test
  -i IP, --ip IP  IPv4 address to check against the RBLs (one or more IP
                  addresses)
  -a, --all       Include unlisted results
~~~~

# Requirements

- Python 3
- dnspython3 library

# Output

~~~~
{
  "not_listed": [],
  "date": "2017-12-25T14:08:58.111259+00:00",
  "query": "127.0.0.2",
  "info": [
    "\"Blocked - see http://www.spamcop.net/bl.shtml?127.0.0.2\"",
    "\"Sender has sent to LashBack Unsubscribe Probe accounts\"",
    "\"Sender has sent to LashBack Unsubscribe Probe accounts\"",
    "\"Blocked due to spam, see http://korea.services.net/blocked.phtml?addr=127.0.0.2\"",
    "\"Blocked due to spam, see http://korea.services.net/blocked.phtml?addr=127.0.0.2\"",
    "\"Blocked due to spam, see http://korea.services.net/blocked.phtml?addr=127.0.0.2\"",
    "\"Spam source - http://wpbl.info/record?ip=127.0.0.2\"",
    "\"Open SMTP Relay See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Hijacked/Disused Netblocks See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Hijacked/Disused Netblocks See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Testing class.\"",
    "\"wild.surbl.org permanent test point\"",
    "\"Test entry, see http://www.dnsbl.manitu.net/lookup.php?value=127.0.0.2\"",
    "\"Test entry, see http://www.dnsbl.manitu.net/lookup.php?value=127.0.0.2\"",
    "\"Dynamic IP Addresses See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Infected System, see http://www.blocklist.de/en/view.html?ip=127.0.0.2\"",
    "\"SOCKS Proxy See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"SOCKS Proxy See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"SOCKS Proxy See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"SOCKS Proxy See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Listed in PSBL, see http://psbl.org/listing?ip=127.0.0.2\"",
    "\"Misc Proxy/Server See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Misc Proxy/Server See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"https://www.spamhaus.org/query/ip/127.0.0.2\"",
    "\"https://www.spamhaus.org/query/ip/127.0.0.2\"",
    "\"RFC5782 Test Entry\"",
    "\"Test Record\"",
    "\"Exploitable Server See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"https://www.spamhaus.org/query/ip/127.0.0.2\"",
    "\"Blocked - see http://www.abuseat.org/lookup.cgi?ip=127.0.0.2\"",
    "\"Dial-Up/Cable/DSL IP Range - Use your providers SMTP Gateway\"",
    "\"Blocked at http://sigs.interserver.net/ip?ip=127.0.0.2\"",
    "\"HTTP Proxy See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Dynamic IP Addresses See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Dynamic IP Addresses See: http://www.sorbs.net/lookup.shtml?127.0.0.2\"",
    "\"Spam Received See: http://www.sorbs.net/lookup.shtml?127.0.0.2\""
  ],
  "listed": [
    "2.0.0.127.bl.spamcop.net",
    "2.0.0.127.ubl.unsubscore.com",
    "2.0.0.127.zen.spamhaus.org",
    "2.0.0.127.zen.spamhaus.org",
    "2.0.0.127.korea.services.net",
    "2.0.0.127.bogons.cymru.com",
    "2.0.0.127.bogons.cymru.com",
    "2.0.0.127.access.redhawk.org",
    "2.0.0.127.access.redhawk.org",
    "2.0.0.127.db.wpbl.info",
    "2.0.0.127.smtp.dnsbl.sorbs.net",
    "2.0.0.127.zombie.dnsbl.sorbs.net",
    "2.0.0.127.rbl.efnetrbl.org",
    "2.0.0.127.rbl.efnetrbl.org",
    "2.0.0.127.dnsbl.dronebl.org",
    "2.0.0.127.multi.surbl.org",
    "2.0.0.127.ix.dnsbl.manitu.net",
    "2.0.0.127.noptr.spamrats.com",
    "2.0.0.127.noptr.spamrats.com",
    "2.0.0.127.dnsbl.sorbs.net",
    "2.0.0.127.all.bl.blocklist.de",
    "2.0.0.127.socks.dnsbl.sorbs.net",
    "2.0.0.127.spam.spamrats.com",
    "2.0.0.127.spam.spamrats.com",
    "2.0.0.127.dyna.spamrats.com",
    "2.0.0.127.dyna.spamrats.com",
    "2.0.0.127.dnsbl.inps.de",
    "2.0.0.127.dnsbl.inps.de",
    "2.0.0.127.psbl.surriel.com",
    "2.0.0.127.misc.dnsbl.sorbs.net",
    "2.0.0.127.short.rbl.jp",
    "2.0.0.127.short.rbl.jp",
    "2.0.0.127.pbl.spamhaus.org",
    "2.0.0.127.b.barracudacentral.org",
    "2.0.0.127.b.barracudacentral.org",
    "2.0.0.127.wormrbl.imp.ch",
    "2.0.0.127.truncate.gbudb.net",
    "2.0.0.127.web.dnsbl.sorbs.net",
    "2.0.0.127.xbl.spamhaus.org",
    "2.0.0.127.cbl.abuseat.org",
    "2.0.0.127.spamguard.leadmon.net",
    "2.0.0.127.rbl.interserver.net",
    "2.0.0.127.http.dnsbl.sorbs.net",
    "2.0.0.127.dul.dnsbl.sorbs.net",
    "2.0.0.127.sbl.spamhaus.org",
    "2.0.0.127.sbl.spamhaus.org",
    "2.0.0.127.spam.dnsbl.sorbs.net"
  ]
}
~~~~

