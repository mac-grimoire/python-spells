#!/usr/bin/env python3

distro={ }
library=[]

distro["name"]="RedHat"
distro["versions"]=["4.0","5.0","6.0","7.0","8.0"]

library.append(distro.copy())
distro["name"]="Suse"
distro["versions"]=["10.0","11.0","15.0","42.0"]
library.append(distro.copy())

print(library)

