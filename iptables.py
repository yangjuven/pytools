#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse
from cStringIO import StringIO


BEGIN = "*filter\n\n-A INPUT -i lo -j ACCEPT\n"
ACCEPT = "-A INPUT -p tcp --dport %d -s %s -j ACCEPT\n"
REJECT = "-A INPUT -p tcp --dport %d -j REJECT\n"
COMMIT = "COMMIT\n\n# ref: http://wiki.debian.org/iptables\n"


def genIptableRules(port, allow_ips):
    iptables = StringIO()
    iptables.write(BEGIN)

    for allow_ip in allow_ips:
        iptables.write(ACCEPT % (port, allow_ip))

    iptables.write(REJECT % (port, ))
    iptables.write(COMMIT)

    return iptables.getvalue()


if __name__ == "__main__":
    usage = "usage: %prog [options]"

    option_list = (
        optparse.make_option("-p", "--port", dest="port", type="int",
            help="Specify destination port of service"),
        optparse.make_option("-s", "--source", action="append", dest="ips",
            help="Specify source ip you allow from"),
    )
    option_default = {}

    parser = optparse.OptionParser(usage=usage, option_list=option_list)
    parser.set_defaults(**option_default)
    options, args = parser.parse_args()

    if options.port is None:
        parser.error("Destination port must be specified")

    if options.ips is None:
        parser.error("Source ip must be specified")

    print genIptableRules(options.port, options.ips)
    sys.exit(0)
