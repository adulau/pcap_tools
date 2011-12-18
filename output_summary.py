#!/usr/bin/python

__description__ = 'Summarize a PCAP file to standard out'
__author__ = 'Brandon Dixon'
__version__ = '1.0'
__date__ = '2011/12/1'

from libs.c2utils import pcap_miner
import time, re, optparse, getpass, time

def main():
    oParser = optparse.OptionParser(usage='usage: %prog [options]\n' + __description__, version='%prog ' + __version__)
    oParser.add_option('-f', '--file', type='string', help='input PCAP file for processing')
    oParser.add_option('-v', '--verbose', action="store_true", default=False, help='verbose logging on performed actions')
    (options, args) = oParser.parse_args()

    if options.file:
        miner = pcap_miner(options.file)
	#file 1 - DNS queries and domains returned	
	print "== DNS Queries and Domains ==\n"
	for dns in miner.get_dns_request_data():
	    print(dns['type'] + " - " + dns['request'] + " - " + dns['response'])	

	print "\n== Destination Addresses ==\n"
	#file 3 - IPs of attackers with whois 
	for ip in miner.get_destination_ip_details():
	    print(ip['ip_address'] + " - " + ip['owner'] + " - " + ip['asn'] + " - " + ip['block'])	
		
	print "\n== Request Dump ==\n"
	#file 5 - whatever can be dumped from the request
	for info in miner.get_http_request_data():
	    for key, value in info.items():
		print(key + " - " + value)
	    print("\n")
	
    else:
        oParser.print_help()
        return

if __name__ == '__main__':
    main()

