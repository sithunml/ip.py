# My first script
# ip.py
import ipaddress

# my_ip = ipaddress.ip_interface("192.168.222.130/29")
def print_ip(my_ip):
    print ("For {}, we have the following:".format(my_ip.exploded))
    print ("IP: {}".format(my_ip.ip))
    print ("Subnet: {}".format(my_ip.network))
    print ("Netmask: {}".format(my_ip.netmask))
    print ("Broadcast: {}".format(my_ip.network.broadcast_address))

raw_ip = input("Type an IP adress <ENTER to quit>: ")

while raw_ip != '':
    ip = ipaddress.ip_interface(raw_ip)
    print_ip(ip)
    raw_ip = input ("Type an IP adress <ENTER to quit>: ")

