#!/usr/bin/python3

import yaml

switch = 'leaf1-DC1'

file = open('underlay.yml', 'r')

underlay = yaml.safe_load(file)

for interface in underlay[switch]['interfaces']:
    ip = underlay[switch]['interfaces'][interface]['ipv4']
    mask = underlay[switch]['interfaces'][interface]['mask']

    print("interface", interface)
    print("   ip address", str(ip)+'/'+str(mask))
    if 'Ethernet' in interface:
        print("   mtu 9214")
        print("   no switchport")