#!/usr/bin/python3

# Create a large list of VLANs (1000 of them)

vlan_start = 100
vlan_number = 1000

vlan_id = vlan_start
vlan_max = vlan_start + vlan_number

while vlan_id < vlan_max:
    print("vlan ", vlan_id)
    vlan_id = vlan_id + 1