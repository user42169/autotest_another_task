

import nmap

nm = nmap.PortScanner()

scan_range = nm.scan(hosts="192.168.88.0/24", ports='22-443')

print (scan_range['scan'])
