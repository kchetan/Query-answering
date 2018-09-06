import nltk	
import sys
import re

match=[0]
ind_prof={}
nz_prof={}

class statistics():
	def __init__(self):
		self.indcom=[0]
		self.nzcom=[0]
		self.bat1={}
		self.bat2={}
		self.bowl1={}
		self.bowl2={}
		self.mom={}
		self.win=''
		self.batfirst=''
		self.toss=''

# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def toss(fname):
	f=open(fname,'r')
	for line in f:
		break
	temp=line[:-1]
	return temp

def win(dictionary,fname):
	f = open(fname, 'r')
	for line in f:
		temp=line[:-1]
		#print temp
		dictionary=temp
	return dictionary
		#print dictionary

def mom(dictionary,fname):
	f = open(fname, 'r')
	for line in f:
		temp=line[:-1]
		temp=temp.split(',')
		a=temp[0]
		b=temp[1:]
	dictionary[a]=b
	#	print a,b

def opening_middleorder(fname):
	f = open(fname, 'r')
	count=0
	opening=0
	middle=0
	ocount=0
	mcount=0
	for line in f:
		count+=1
		temp = line[:-1]
		temp = temp.split(',')
		a = int(temp[2])
		if count==1 or count==2:
			ocount+=1
			opening+=a
		elif count==5 or count==6:
			mcount+=1
			middle+=a
	return opening,middle,ocount,mcount

def player_profile(dictionary,fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('	')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def com(arr,fname):
	f = open(fname, 'r')
	count=0
	ball=0
	for line in f:
		temp=line[:-1]
		if count==1:
			a={}
			a[ball]=temp
			arr.append(a)
			count=0
		if re.match(r'^([0-9]+)\.[0-6]$',temp):
			count=1
			temp=temp.split('.')
			ball=int(temp[0])*6
			ball=ball+int(temp[1])
	return arr


def playerofmatch(rem,count):
	b={}
	c={}
	string='pom'
	for i in range(1,6):
		m='match'+str(i)
		a=match[i].mom.keys()
		arr=string+' => {'
		for j in a:
			if j in rem.keys():
				arr+=rem[j]+','
			else:
				rem[j]='r'+str(count)
				arr+='r'+str(count)+','
				count+=1
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		b[m]=a
		c[m]=arr
	return b,c,string,rem,count

def winningteam(rem,count):
	b={}
	c={}
	string='wt'
	for i in range(1,6):
		ar=[]
		arr=string + ' => {'
		m='match'+str(i)
		a=match[i].win
		if match[i].win=='New Zealand':
			for j in  nz_prof.keys():
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		elif match[i].win=='India':
			for j in  ind_prof.keys():
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def losingside(rem,count):
	b={}
	c={}
	string='ls'
	for i in range(1,6):
		ar=[]
		m='match'+str(i)
		a=match[i].win
		arr=string + ' => {'
		if match[i].win=='New Zealand':
			for j in  ind_prof.keys():
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1

		elif match[i].win=='India':
			for j in  nz_prof.keys():
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def duck(rem,count):
	b={}
	c={}
	string='duck'
	for i in range(1,6):
		ar=[]
		m='match'+str(i)
		a1=match[i].bat1.keys()
		a2=match[i].bat2.keys()
		arr=string + ' => {'
		for j in a1:
			if int(match[i].bat1[j][1])==0:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		for j in a2:
			if int(match[i].bat2[j][1])==0:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def srate(num,rem,count,k):
	b={}
	c={}
	string='srate'
	for i in range(1,6):
		ar=[]
		arr=string + ' => {'
		m='match'+str(i)
		a1=match[i].bat1.keys()
		a2=match[i].bat2.keys()
		for j in a1:
			if k*float(match[i].bat1[j][6])>=num*k:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		for j in a2:
			if k*float(match[i].bat2[j][6])>=num*k:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def mstf(rem,count):
	b={}
	c={}
	string='mstf'
	for i in range(1,6):
		ar=[]
		arr=string + ' => {'
		m='match'+str(i)
		a1=match[i].bat1.keys()
		a2=match[i].bat2.keys()
		for j in a1:
			if  int(match[i].bat1[j][5])>int(match[i].bat1[j][4]):
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		for j in a2:
			if int(match[i].bat2[j][5])>int(match[i].bat2[j][4]):
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def bbo(num,rem,count):
	b={}
	c={}
	string='bbo'
	for i in range(1,6):
		ar=[]
		arr=string + ' => {'
		m='match'+str(i)
		a1=match[i].bowl1.keys()
		a2=match[i].bowl2.keys()
		for j in a1:
			if  float(match[i].bowl1[j][0])>num:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		for j in a2:
			if float(match[i].bowl2[j][0])>num:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count


def fgw(rem,count):
	b={}
	c={}
	string='fgw'
	for i in range(1,6):
		ar=[]
		arr=string + ' => {'
		m='match'+str(i)
		a1=match[i].bowl1.keys()
		a2=match[i].bowl2.keys()
		for j in a1:
			if  float(match[i].bowl1[j][3])==0:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		for j in a2:
			if float(match[i].bowl2[j][3])==0:
				ar.append(j)
				if j in rem.keys():
					arr+=rem[j]+','
				else:
					rem[j]='r'+str(count)
					arr+='r'+str(count)+','
					count+=1
		b[m]=ar
		if arr[-1]!='{':
			arr=arr[:-1]
		arr+='} \n'
		c[m]=arr
	return b,c,string,rem,count

def case(desc,rem,count):
	if re.search(r'player of match',desc,re.I):
		b,c,string,rem,count=playerofmatch(rem,count)
	elif re.search(r'winning team',desc,re.I):
		b,c,string,rem,count=winningteam(rem,count)
	elif re.search(r'losing side',desc,re.I):
		b,c,string,rem,count=losingside(rem,count)
	elif re.search(r'duck',desc,re.I):
		b,c,string,rem,count=duck(rem,count)
	elif re.search(r'strike rate',desc,re.I):
		i=1
		num=0
		n1=re.search(r'.*?(([0-9]+)(\.[0-9]+)*).*',desc,re.I)
		if n1.group(1):
			num=n1.group(1)
		else:
			n1.group(2)
		if desc.find('above') or desc.find('more') or desc.find('great'):
			i=1
		else:
			i=-1
		b,c,string,rem,count=srate(float(num),rem,count,i)
	elif re.search(r' more sixes than fours',desc,re.I):
		b,c,string,rem,count=mstf(rem,count)
	elif re.search(r'bowler .* overs',desc,re.I):
		i=1
		num=0
		n1=re.search(r'.*?([0-9]+) overs.*',desc,re.I).group(1)
		if n1:
			num=(n1)
		if desc.find('above') or desc.find('more') or desc.find('great'):
			i=1
		else:
			i=-1
		b,c,string,rem,count=bbo(int(num),rem,count)
	elif re.search(r'failed.*?wicket.*',desc,re.I):
		b,c,string,rem,count=fgw(rem,count)
	return b,c,string,rem,count

def allmatch(b1,c1,b2,c2,string1,string2,rem,connector):
	ans={}
	flag=0
	for i in range(1,6):
		m='match'+str(i)
		temp=''
		for j in rem.keys():
			temp+=j + ' => ' + rem[j]+ '\n'
		v = temp + c1[m] + c2[m]
		if connector==3 or connector==2 or connector==1:
			query='all x (' + string1+ '(x) -> '+string2+'(x))'
		if connector==4 or connector==5:
			query='all x (' + string2+ '(x) -> '+string1+'(x))'
		print v
		#print query
		t,temp=answer_query1(query,v,rem,string1,string2,connector,i)
		ans.update(temp)
		if t!=1:
			flag=1
	if flag==1:
		print False
	else:
		print True
		for p,q in  ans.iterkeys():
			print p +' --> '+ q

def exists(b1,c1,b2,c2,string1,string2,rem,connector):
	ans={}
	flag=0
	for i in range(1,6):
		m='match'+str(i)
		temp=''
		for j in rem.keys():
			temp+=j + ' => ' + rem[j]+ '\n'
		v = temp + c1[m] + c2[m]
		if connector==3 or connector==2 or connector==1:
			query='all x (' + string1+ '(x) -> '+string2+'(x))'
		if connector==4 or connector==5:
			query='all x (' + string2+ '(x) -> '+string1+'(x))'
		#print v
		#print query
		t,temp=answer_query1(query,v,rem,string1,string2,connector,i)
		ans.update(temp)
		if t==1:
			flag=1
	if flag==0:
		print False
	else:
		print True
		#print ans
		for p,q in  ans.iteritems():
			print p +' --> '+ str(q)

def answer_query1(query,v,rem,string1,string2,connector,i):
	        val = nltk.parse_valuation(v)
		dom = val.domain
		
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		#print "The anwer for the query is : ",
		t=m.evaluate(query, g)
		#print t
		ans={}
		if t==1:
			#print "Showing the player Names for which  ismom(x) -> isteam(x) given ismom(x) is true"
			l = nltk.LogicParser()
			if connector==3 or connector==2 or connector==1:
				c1 = l.parse('('+ string1+ '(x) &'+ query +')')
			if connector==4 or connector==5:
				c1 = l.parse('('+ string2+ '(x) &'+ query +')')
			varnames =  m.satisfiers(c1, 'x', g)
			m='match'+str(i)
			arr=[]
			for i in varnames:
				for p,q in rem.iteritems():
					if q==i:
						arr.append(p)
			ans[m]=arr		
		return t,ans


	


def query_processing(q):
	quantifier=0
	desc=None
	if re.search(r'^for.*?match.*?,',q,re.I|re.M):
		quantifier=1
		a=q.split(re.search(r'^for.*?match.*?,',q,re.I|re.M).group())[1][1:]
	elif re.search('^there exists.*?player',q,re.I|re.M):
		quantifier=2
		a=q.split(re.search('^there exists.*?player.*?,',q,re.I|re.M).group())[1][1:]
	elif re.search(r'^for all inning.*?,',q,re.I|re.M):
		quantifier=3
		a=q.split(re.search(r'^for all inning.*?,',q,re.I|re.M).group())[1][1:]
	elif re.search(r'^there.*?match.*?',q,re.I|re.M):
		quantifier=4
		a=q.split(re.search(r'^there.*?match.*?,',q,re.I|re.M).group())[1][1:]
	else:
		print "wrong format"
		return
	connector=0
	if re.search(r'and',q,re.I|re.M):
		connector=1
		desc1=a.split('and')[0]
		desc2=a.split('and')[1][:-1]
	elif re.search('if.*?then',q,re.I|re.M):
		connector=2
		desc1=re.search('if(.*?)then(.*)',a,re.I|re.M).group(1)
		desc2=re.search('if(.*?)then(.*)\.',a,re.I|re.M).group(2)
	elif re.search(r'is given to',q,re.I|re.M):
		connector=3
		desc1=a.split('is given to')[0]
		desc2=a.split('is given to')[1][:-1]
	elif re.search(r'consists of',q,re.I|re.M):
		connector=4
		desc1=a.split('consists of')[0]
		desc2=a.split('consists of')[1][:-1]
	elif re.search(r'contains',q,re.I|re.M):
		connector=5
		desc1=a.split('contains')[0]
		desc2=a.split('contains')[1][:-1]
	else:
		print "wrong format"
		return
	rem={}
	count=0
	b1,c1,string1,rem,count=case(desc1,rem,count)
	b2,c2,string2,rem,count=case(desc2,rem,count)
	'''
	print b1
	print b2
	print c1
	print c2
	print rem
	'''
	if quantifier==1 or quantifier==3:
		allmatch(b1,c1,b2,c2,string1,string2,rem,connector)
	if quantifier==2 or quantifier==4:
		exists(b1,c1,b2,c2,string1,string2,rem,connector)


def main():
	f7='../dataset/player_profile/indian_players_profile.txt'
	f8='../dataset/player_profile/nz_players_profile.txt'
	player_profile(ind_prof,f7)
	player_profile(nz_prof,f8)
	for i in range(1,6):
		match.append(statistics())
		f1 = '../dataset/match'+ str(i)+ '/odi'+ str(i) + '_inn1_bat.txt'
		f2 = '../dataset/match'+ str(i)+ '/odi'+ str(i) + '_inn2_bat.txt'
		f3 = '../dataset/match'+ str(i)+ '/odi'+ str(i) + '_inn1_bowl.txt'
		f4 = '../dataset/match'+ str(i)+ '/odi'+ str(i) + '_inn2_bowl.txt'
		f5 = '../dataset/match'+ str(i)+ '/mom.txt'
		f6 = '../dataset/match'+ str(i)+ '/wonby.txt'
		f7 = '../dataset/match'+ str(i)+ '/tosswin.txt'
		f8 = '../dataset/match'+ str(i)+ '/commentary_in.txt'
		f9 = '../dataset/match'+ str(i)+ '/commentary_nz.txt'
		
		add_to_dict(match[i].bat1, f1)
		add_to_dict(match[i].bat2, f2)
		if ind_prof.get(match[i].bat1.keys()[0]):
			match[i].batfirst='India'
		else:
			match[i].batfirst='New Zealand'
		add_to_dict(match[i].bowl1, f3)
		add_to_dict(match[i].bowl2, f4)
		match[i].win=win(match[i].win,f6)
		mom(match[i].mom,f5)
		match[i].toss=toss(f7)
		match[i].indcom=com(match[i].indcom,f8)
		match[i].nzcom=com(match[i].nzcom,f9)
	q=raw_input()
	query_processing(q)

if __name__ == "__main__":
	main()
