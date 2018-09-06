import urllib2 , re
url = 'http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html'
response = urllib2.urlopen(url)
html = response.read()
html = html.split('\n')
sz = len(html)
co = 0
do = False
batFl = False
for i in range(0 , sz) :
	m1 = re.search('<table class="inningsTable" id="inningsBat1">' , html[i])
	if m1 :
		batFl = True
	m2 = re.search('<table class="inningsTable" id="inningsBat2">' , html[i])
	if m2 :
		batFl = False
	m2 = re.search('<td class="inningsDetails">Extras</td>' , html[i])
	if m2 :
		batFl = False
	if batFl :
		m3 = re.search('<tr class="inningsRow">' , html[i])
		#m4 = re.search('<td class="inningsIcon"' , html[i+1])
		#m5 = re.search('<td></td>' , html[i+1])
		if m3:
			name = re.split('.* class="playerName">(.*?)</a>.*' , html[i+2])
			out = re.split('<td width="259" class="battingDismissal">(.*?)..</td>' , html[i+3])
			l1 = re.split('.*>(.*?)</td>' , html[i+4])
			l2 = re.split('.*>(.*?)</td>' , html[i+5])
			l3 = re.split('.*>(.*?)</td>' , html[i+6])
			l4 = re.split('.*>(.*?)</td>' , html[i+7])
			l5 = re.split('.*>(.*?)</td>' , html[i+8])
			l6 = re.split('.*>(.*?)</td>' , html[i+9])
			if len(name) == len(out) == len(l1) == 3:
				print name[1] + str(',') + out[1] + str(',') + l1[1] + str(',') + l2[1] + str(',') + l3[1] + str(',') + l4[1] + str(',') + l5[1] + str(',') + l6[1]
