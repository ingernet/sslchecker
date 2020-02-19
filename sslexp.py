#!/usr/bin/python3
from subprocess import Popen, PIPE, check_output
from os import open, O_WRONLY

servers = [
        "server1.domain.com",
        "server2.domain.com",
        "server3.domain.com"
        ]

for s in servers:
    print("querying {}".format(s))
    dn = open("/dev/null", O_WRONLY)
    q = Popen(["/usr/bin/openssl", "s_client", "-servername", s, "-connect","{}:443".format(s)], stdout=PIPE, stdin=PIPE, stderr=dn, shell=False)
    y = check_output(["/usr/bin/openssl", "x509", "-noout", "-dates"], stdin=q.stdout)
    print(y.decode("utf-8"))
