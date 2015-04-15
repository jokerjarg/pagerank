import re
import sys
import pagerank

# coded by : jok3r, mass google pagerank checking
# http://www.meonsecurity.com, jokerjarg@gmail.com

if(len(sys.argv) < 2):
	print "[*] Usage : python prank.py sites.txt"
	sys.exit()
websites = []
ranked = []
highranks = []
try:
    sites=open(sys.argv[1],"r").readlines()
except IOError:
    print " [-] Error Loading the List!"
    sys.exit()	
def add(site):
	for website in websites:
		if site == website:
			return False
	return True
def highRank(rank):
	if int(rank) >= 4:
		return True
	else:
		return False
for s in sites :
	s = s.replace("\n","")
	if(add(s) == True):
		websites.append(s)		
	else:
		print s, " exists "
print " ***results**** "
for website in websites:
	res = pagerank.GetPageRank(website)
	ranked.append(website+" : "+res)
	if(highRank(res) == True):
		highranks.append(website+" : "+res)
print "Results : "
for r in ranked:
	r = r.replace("\n","")
	print r
print "\nHigh Ranks :"
for h in highranks:
	h = h.replace("\n","")
	print h
