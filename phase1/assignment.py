import nltk	
import sys
import re

match=[0]
ind_prof={}
nz_prof={}

class statistics():
	def __init__(self):
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
	#	print a,b
		dictionary[a]=b

# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(bat, num):
	toreturn = []
	# strike rate is in the 7th column
	for i in bat:
		temp = bat[i]
		k = float(temp[6])
		if k > num:
			toreturn.append(i)
	return  toreturn

# It retrieves the variable names corresponding to players, who have greater than 0 sixes
def parse_for_six(bat, num):
	toreturn  = []

	# number of six hit are in 6th column
	for i in bat:
		temp = bat[i]
		k = int(temp[5])
		if k > num:
			toreturn.append(i)
	return toreturn

# the function to make the model and answer the query, given the properly formatted strings
def answer_query1(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  ismom(x) -> isteam(x) given ismom(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' ((ismom(x)) & (ismom(x) -> isteam(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			print dt[i]

def answer_query2(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  hasloser(x) -> hasduck(x) given hasloser(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' ((hasloser(x)) & (hasloser(x) -> hasduck(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			print dt[i]

def answer_query3(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  israte(x) -> more6than4(x) given israte(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' ((israte(x)) & (israte(x) -> more6than4(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		print varnames
		for i in varnames:
			print dt[i]


def answer_query4(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  iswin(x) -> 4ndnot100(x) given iswin(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' ((iswin(x)) & (iswin(x) => 4ndnot100(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			print dt[i]


def answer_query5(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  is50(x) -> atleast1w(x) given is50(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse('(is50(x) & atleast1w(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					print p

def answer_query6(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  morethan7(x) -> 0w(x) given morethan7(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (morethan7(x) & 0w(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					print p

def answer_query7(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  nowicket(x) -> 8eco(x) given nowicket(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (nowicket(x) & 8eco(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					print p


def answer_query8(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  islost(x) -> morethan100(x) given islost(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (islost(x) & morethan100(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			print dt[i]

def answer_query9(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  match(x) -> rhbmorelhb(x) given match(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (match(x) -> rhbmorelhb(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			print dt[i]


def answer_query10(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		##print "Showing the player Names for which  nowicket(x) -> 8eco(x) given nowicket(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (isage26(x) & 250noduck(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					print p

def answer_query11(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	t=m.evaluate(query, g)
	print t
	if t==1:
		#print "Showing the player Names for which  nowicket(x) -> 8eco(x) given nowicket(x) is true"	
		l = nltk.LogicParser()
		c1 = l.parse(' (isplayer(x) & allmatches(x))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					print p

def query1():
	name={}
	count=0
	temp_strin2='ismom => {'
	for i in range(1,6):
		a=match[i].mom.keys()[0]
		#name.append(a[0])
		name['r'+str(count)]= a
		temp_strin2+='r'+str(count)+','
		count+=1
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin1=''
	for i in range(1,6):
		temp_strin1+=name['r'+str(i-1)] + ' => ' + 'r' + str(i-1) + '\n'
	temp_strin3= 'isteam => {'
	for i in range(1,6):
		a=match[i].mom.keys()[0]
		#print match[i].win,match[i].mom[a][0]
		if match[i].mom[a][0]==match[i].win:
			temp_strin3+='r' + str(i-1) + ','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	#print name,temp_strin1,temp_strin2,temp_strin3
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (ismom(x) -> isteam(x))'
	print v
	answer_query1(v, query, name)

def query2():
	name={}
	count=0
	temp_strin2='hasloser => {'
	temp_strin1=''
	for i in range(1,6):
		if match[i].win!='Tie':
			name['r'+str(count)]= 'match'+str(i)
			temp_strin2+='r'+str(count)+','
			temp_strin1+=name['r'+str(count)]+' => '+'r'+str(count)+'\n'
		count+=1
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='hasduck => {'
	for i in range(1,6):
		if match[i].win=='India':
			if match[i].batfirst=='India':
				a=match[i].bat2
			else:
				a=match[i].bat1
		elif match[i].win=='New Zealand':
			if match[i].batfirst=='New Zealand':
				a=match[i].bat2
			else:
				a=match[i].bat1
		b=a.keys()
		for j in b:
			if a[j][1]=='0':
				temp_strin3+='r'+str(i-1)+','
				break
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (hasloser(x) -> hasduck(x))'
	#print v
	answer_query2(v, query, name)
	
def query3():
	name={}
	count=0
	temp_strin2='israte => {'
	temp_strin1=''
	for i in range(1,6):
		for j in match[i].bat1:
			name[j+' in'+'match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+'match'+str(i)+' => '+'r'+str(count)+'\n'
			#print match[i].bat1[j][-1],count-1
			if float(match[i].bat1[j][-1])>200:
				temp_strin2+='r'+str(count)+','
			count+=1
		for j in match[i].bat2:
			name[j+' in'+'match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+'match'+str(i)+' => '+'r'+str(count)+'\n'
			#print match[i].bat2[j][-1],count-1
			if float(match[i].bat2[j][-1])>200:
				temp_strin2+='r'+str(count)+','
			count+=1	
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='more6than4 => {'
	for i in range(1,6):
		for j in match[i].bat1:
			if float(match[i].bat1[j][5])>float(match[i].bat1[j][4]):
				temp_strin3+=name[j+' in'+'match'+str(i)]+','
		for j in match[i].bat2:
			if float(match[i].bat2[j][5])>float(match[i].bat2[j][4]):
				temp_strin3+=name[j+' in'+'match'+str(i)]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (israte(x) -> more6than4(x))'
	#print v
	answer_query3(v, query, name)
				
def query4():
	name={}
	count=0
	temp_strin2='iswin => {'
	temp_strin1=''
	for i in range(1,6):
		if match[i].win!='Tie':
			name['r'+str(count)]= 'match'+str(i)
			temp_strin2+='r'+str(count)+','
			temp_strin1+=name['r'+str(count)]+' => '+'r'+str(count)+'\n'
		count+=1
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='4ndnot100 => {'
	for i in range(1,6):
		if match[i].win=='India':
			if match[i].batfirst=='India':
				a=match[i].bat1
			else:
				a=match[i].bat2
		elif match[i].win=='New Zealand':
			if match[i].batfirst=='New Zealand':
				a=match[i].bat1
			else:
				a=match[i].bat2
		b=a.keys()
		for j in b:
			if int(a[j][4])>1 and float(a[j][-1])<100:
				temp_strin3+='r'+str(i-1)+','
				break
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (iswin(x) -> 4ndnot100(x))'
	#query = 'all x exist y (hit4(x,y) -> sratenot100(x,y))'
	#print v
	answer_query4(v, query, name)


	
def query5():
	name={}
	count=0
	temp_strin2='is50 => {'
	temp_strin1=''
	for i in range(1,6):
		for j in match[i].bat1:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1
			#print match[i].bat1[j][-1],count-1
		for j in match[i].bat2:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1	
			#print match[i].bat2[j][-1],count-1
	for i in range(1,6):
		for j in match[i].bat1:
			if float(match[i].bat1[j][1])>50:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bat2:
			if float(match[i].bat2[j][1])>50:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='atleast1w => {'
	for i in range(1,6):
		for j in match[i].bowl1:
			if int(match[i].bowl1[j][3])>=1:
				if not name.has_key(j+' in'+' match'+str(i)):
					name[j+' in'+' match'+str(i)]= 'r'+str(count)
					temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
					count+=1
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bowl2:
			if int(match[i].bowl2[j][3])>=1:
				if not name.has_key(j+' in'+' match'+str(i)):
					name[j+' in'+' match'+str(i)]= 'r'+str(count)
					temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
					count+=1
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (is50(x) & atleast1w(x))'
#	print v
	answer_query5(v, query, name)


def query6():
	name={}
	count=0
	temp_strin2='morethan7 => {'
	temp_strin1=''
	for i in range(1,6):
		for j in match[i].bowl1:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1
			#print match[i].bat1[j][-1],count-1
		for j in match[i].bowl2:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1	
			#print match[i].bat2[j][-1],count-1
	for i in range(1,6):
		for j in match[i].bowl1:
			if float(match[i].bowl1[j][0])>7:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bowl2:
			if float(match[i].bowl2[j][0])>7:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='0w => {'
	for i in range(1,6):
		for j in match[i].bowl1:
			if int(match[i].bowl1[j][3])==0:
				if not name.has_key(j+' in'+' match'+str(i)):
					name[j+' in'+' match'+str(i)]= 'r'+str(count)
					temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
					count+=1
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bowl2:
			if int(match[i].bowl2[j][3])==0:
				if not name.has_key(j+' in'+' match'+str(i)):
					name[j+' in'+' match'+str(i)]= 'r'+str(count)
					temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
					count+=1
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (morethan7(x) & 0w(x))'
	#print v
	answer_query6(v, query, name)

def query7():
	name={}
	count=0
	temp_strin2='nowicket => {'
	temp_strin1=''
	for i in range(1,6):
		for j in match[i].bowl1:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1
			#print match[i].bat1[j][-1],count-1
		for j in match[i].bowl2:
			name[j+' in'+' match'+str(i)]= 'r'+str(count)
			temp_strin1+=j+' in'+' match'+str(i)+' => '+'r'+str(count)+'\n'
			count+=1	
			#print match[i].bat2[j][-1],count-1
	for i in range(1,6):
		for j in match[i].bowl1:
			if float(match[i].bowl1[j][3])==0:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bowl2:
			if float(match[i].bowl2[j][3])==0:
				temp_strin2+=name[j+' in'+' match'+str(i)]+','
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='8eco => {'
	for i in range(1,6):
		for j in match[i].bowl1:
			if float(match[i].bowl1[j][4])>8:
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
		for j in match[i].bowl2:
			if float(match[i].bowl2[j][4])>8:
				temp_strin3+=name[j+' in'+' match'+str(i)]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (nowicket(x) & 8eco(x))'
	#print v
	answer_query7(v, query, name)

def query8():
	name={}
	count=0
	temp_strin2='islost => {'
	temp_strin1=''
	for i in range(1,6):
		if match[i].win!='Tie':
			name['r'+str(count)]= 'match'+str(i)
			temp_strin2+='r'+str(count)+','
			temp_strin1+=name['r'+str(count)]+' => '+'r'+str(count)+'\n'
		count+=1
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='morethan100 => {'
	a={}
	for i in range(1,6):
		if match[i].win=='India':
			if match[i].batfirst=='India':
				a=match[i].bat2
			else:
				a=match[i].bat1
		elif match[i].win=='New Zealand':
			if match[i].batfirst=='New Zealand':
				a=match[i].bat2
			else:
				a=match[i].bat1
		b=a.keys()
		for j in b:
			if int(a[j][1])>100:
				temp_strin3+='r'+str(i-1)+','
				break
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (islost(x) & morethan100(x))'
	#print v
	answer_query8(v, query, name)


def query9():
	name={}
	count=1
	temp_strin2='match => {'
	temp_strin1=''
	for i in range(1,6):		
		name['r'+str(count)]= 'match'+str(i)
		temp_strin2+='r'+str(count)+','
		temp_strin1+=name['r'+str(count)]+' => '+'r'+str(count)+'\n'
		count+=1
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='rhbmorelhb => {'
	for i in range(1,6):
		rhb=0
		lhb=0
		for j in match[i].bowl1:
			if match[i].batfirst=='India':
				if nz_prof[j][-1][0]=='R' and match[i].bowl1.has_key(j):
					rhb+=int(match[i].bowl1[j][3])
				elif nz_prof[j][-1][0]=='L' and match[i].bowl1.has_key(j):
					lhb+=int(match[i].bowl1[j][3])
			else:
				if ind_prof[j][-1][0]=='R' and match[i].bowl1.has_key(j):
					rhb+=int(match[i].bowl1[j][3])
				elif ind_prof[j][-1][0]=='L' and match[i].bowl1.has_key(j):
					lhb+=int(match[i].bowl1[j][3])
		for j in match[i].bowl2:
			if match[i].batfirst=='New Zealand':
				#print j,nz_prof[j]
				if nz_prof[j][-1][0]=='R' and match[i].bowl2.has_key(j):
					rhb+=int(match[i].bowl2[j][3])
				elif nz_prof[j][-1][0]=='L' and match[i].bowl2.has_key(j):
					lhb+=int(match[i].bowl2[j][3])
			else:
				if ind_prof[j][-1][0]=='R' and match[i].bowl2.has_key(j):
					rhb+=int(match[i].bowl2[j][3])
				elif ind_prof[j][-1][0]=='L' and match[i].bowl2.has_key(j):
					lhb+=int(match[i].bowl2[j][3])
		if rhb>lhb:
			temp_strin3+='r'+str(i)+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (match(x) & rhbmorelhb(x))'
#	print v
	answer_query9(v, query, name)

def query10():
	name={}
	count=0
	temp_strin2='isage26 => {'
	temp_strin1=''
	for i in ind_prof:
		if i not in name:
			name[i] = 'r' + str(count)
			temp_strin1+=i+' => '+name[i]+'\n'
			count += 1
			if int(ind_prof[i][2][:2])<26:
				temp_strin2+=name[i]+','
	for i in nz_prof:
		if i not in name:
			name[i] = 'r' + str(count)
			temp_strin1+=i+' => '+name[i]+'\n'
			count += 1
			if int(nz_prof[i][2][:2])<26:
				temp_strin2+=name[i]+','
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='250noduck => {'
	for i in name:
		runs=0
		flag=0
		for j in range(1,6):
			if match[j].bat1.has_key(i):
				runs+=int(match[j].bat1[i][1])
				if int(match[j].bat1[i][1])==0:
					flag=1
			elif match[j].bat2.has_key(i):
				runs+=int(match[j].bat2[i][1])
				if int(match[j].bat2[i][1])==0:
					flag=1
		#print runs,i
		if runs>250 and flag==0:
			temp_strin3+=name[i]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (isage26(x) & 250noduck(x))'
	#print v
	answer_query10(v, query, name)


def query11():
	name={}
	count=0
	temp_strin2='isplayer => {'
	temp_strin1=''
	for i in ind_prof:
		if i not in name:
			name[i] = 'r' + str(count)
			temp_strin1+=i+' => '+name[i]+'\n'
			count += 1
			temp_strin2+=name[i]+','
	for i in nz_prof:
		if i not in name:
			name[i] = 'r' + str(count)
			temp_strin1+=i+' => '+name[i]+'\n'
			count += 1
			temp_strin2+=name[i]+','
	temp_strin2=temp_strin2[:-1]
	temp_strin2+='} \n'
	temp_strin3='allmatches => {'
	for i in name:
		matches_played=0
		for j in range(1,6):
			if i in match[j].bat1:
				matches_played+=1
			elif i in match[j].bat2:
				matches_played+=1
			elif i in match[j].bowl1:
				matches_played+=1
			elif i in match[j].bowl2:
				matches_played+=1
		if matches_played==5:
			temp_strin3+=name[i]+','
	temp_strin3=temp_strin3[:-1]
	temp_strin3+='} \n'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (isplayer(x) & allmatches(x))'
	#print v
	answer_query11(v, query, name)
	
def query12():
	p1="I Sharma"
	p2="RA Jadeja"
	p1wides=0
	p2wides=0
	for i in range(1,6):
		if p2 in match[i].bowl1:
			if len(match[i].bowl1[p2])>5:
				a=match[i].bowl1[p2][5]
				if re.search(',',match[i].bowl1[p2][5]):
					a=a.split(',')
					a=a[1]
					a=a[0:-2]
					p2wides+=int(a)
				else:
					a=a[1:-2]
					p2wides+=int(a)
		if p2 in match[i].bowl2:
			if len(match[i].bowl2[p2])>5:
				a=match[i].bowl2[p2][5]
				if re.search(',',match[i].bowl2[p2][5]):
					a=a.split(',')
					a=a[1]
					a=a[0:-2]
					p2wides+=int(a)
				else:
					a=a[1:-2]
					p2wides+=int(a)
		if p1 in match[i].bowl2:
			if len(match[i].bowl2[p1])>5:
				a=match[i].bowl2[p1][5]
				if re.search(',',match[i].bowl2[p1][5]):
					a=a.split(',')
					a=a[1]
					a=a[0:-2]
					p1wides+=int(a)
				else:
					a=a[1:-2]
					p1wides+=int(a)
		if p1 in match[i].bowl1:
			if len(match[i].bowl1[p1])>5:
				a=match[i].bowl1[p1][5]
				if re.search(',',match[i].bowl1[p1][5]):
					a=a.split(',')
					a=a[1]
					a=a[0:-2]
					p1wides+=int(a)
				else:
					a=a[1:-2]
					p1wides+=int(a)
	if p1wides>p2wides:
		print True, " - Ishant bowled more wides"
	else:
		print False, " - Jadeja bowled more wides"

def query13():
	scatch=0
	rcatch=0
	for i in range(1,6):
		if match[i].batfirst=='India':
			a=match[i].bat1
		else:
			a=match[i].bat2
		for j in a:
			b=a[j][0]
			if b[0]=='c':
				b=b.split(' b ')
				if re.search('Southee',b[0]) or (re.search('&',b[0]) and re.search('Southee',b[1])):
					scatch+=1
				if re.search('Ryder',b[0]):
					rcatch+=1
	if scatch>rcatch:
		print True," - Southee took more catches"
	else:
		print False," - Ryder took more catches"

def query14():
	name={}
	flag=0
	count=0
	for i in range(1,6):
		for i in match[i].mom:
			if i not in name:
				name[i] = 'r' + str(count)
				count += 1
			else:
				flag=1
				break
	if flag==1:
		print True," - "+i+"was awarded mom more than once"
	else:
		print False

def bowling_heuristics(bowl):
	val=int(bowl[0])*6+int(bowl[1])*5-int(bowl[2])+int(bowl[3])*10
	return val

def batting_heuristics(bat):
	val=0
	return val

def query15():
	jaddu='RA Jadeja'
	inn1=0.0
	inn2=0.0
	flag=0
	c1=0
	c2=0
	for i in range(1,6):
		val=0
		if match[i].batfirst=='India':
			a=match[i].bowl2
			flag=2
			c2+=1
		else:
			a=match[i].bowl1
			flag=1
			c1+=1
		if jaddu in a:
			val=bowling_heuristics(a[jaddu])
		if flag==1:
			inn1+=val
		else:
			inn2+=val
	inn1=float(float(inn1)/c1)
	inn2=float(float(inn2)/c2)
	if inn1>inn2:
		print "SIR JADEJA bowled better in innings1"
	elif inn1<inn2:
		print "SIR JADEJA bowled better in innings2"
	else:
		print "SIR JADEJA bowled same way in both innings"

def query16():
	dhoni='MS Dhoni'
	c=0
	totalruns=0
	boundaryruns=0
	srate=0
	for i in range(1,6):
		val=0
		if match[i].batfirst=='India':
			a=match[i].bat1
		else:
			a=match[i].bat2
		if dhoni in a:
			c+=1
			#print float(a[dhoni][6])
			srate+=float(a[dhoni][6])
			totalruns+=int(a[dhoni][1])
			boundaryruns+=int(a[dhoni][4])*4+int(a[dhoni][5])*6
	avgsrate=float(srate*1.0/c)
	#print avgsrate,totalruns,boundaryruns
	if boundaryruns*2.25>totalruns and avgsrate>90:
		print "True - Dhoni is a hard hitting batsman"
	else:
		print "False - Dhoni is not a hard hitting batsman"
def query17():
	ishant="I Sharma"
	jaddu="RA Jadeja"
	jad=0
	ish=0
	c1=0
	c2=0
	for i in range(1,6):
		val=0
		if match[i].batfirst=='India':
			a=match[i].bowl2
		else:
			a=match[i].bowl1
		if jaddu in a:
			c2+=1
			val=bowling_heuristics(a[jaddu])
			jad+=val
		if ishant in a:
			c1+=1
			val=bowling_heuristics(a[ishant])
			ish+=val
	ish=float(ish*1.0/c1)
	jad=float(ish*1.0/c2)
	if ish>jad:
		print "ISHANT is a better bowler than JADEJA"
	elif ish<jad:
		print "JADEJA is a better bowler than ISHANT"

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

def query18():
	oruns=0
	mruns=0
	ocount=0
	mcount=0
	for i in range(1,6):
		match.append(statistics())
		f1 = './match'+ str(i)+ '/odi'+ str(i) + '_inn1_bat.txt'
		f2 = './match'+ str(i)+ '/odi'+ str(i) + '_inn2_bat.txt'
		val1,val2,val3,val4=opening_middleorder(f1)
		oruns+=val1
		mruns+=val2
		ocount+=val3
		mcount+=val4
		val1,val2,val3,val4=opening_middleorder(f2)
		oruns+=val1
		mruns+=val2
		ocount+=val3
		mcount+=val4
	avgo=float(1.0*oruns/ocount)
	avgm=float(1.0*mruns/mcount)
	if avgo>avgm:
		print "Opening batsman have performed well"
	elif avgo<avgm:
		print "Middle order batsman have performed well"
	else:
		print "Both performed equally"


def query19():
	flag=0
	for i in range(1,6):
		if((match[i].win=='India' and match[i].toss=='India') or (match[i].win=='New Zealand' and match[i].toss=='New Zealand')):
			flag=1
			break
	if flag==1:
		print "True - teams winning the tosses also win the matches"
	else:
		print "False - teams winning the tosses does not win the matches"

def query20():
	indwin=0
	nzwin=0
	for i in range(1,6):
		if(match[i].win=="India"):
			indwin+=1
		elif(match[i].win=="New Zealand"):
			nzwin+=1
	if nzwin>indwin:
		print "New Zealand will win the next match"
	elif indwin>nzwin:
		print "India will win the next match"
	else:
		print "The match will be a tie"

def player_profile(dictionary,fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('	')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b


def main():
	f7='./player_profile/indian_players_profile.txt'
	f8='./player_profile/nz_players_profile.txt'
	player_profile(ind_prof,f7)
	player_profile(nz_prof,f8)
	for i in range(1,6):
		match.append(statistics())
		f1 = './match'+ str(i)+ '/odi'+ str(i) + '_inn1_bat.txt'
		f2 = './match'+ str(i)+ '/odi'+ str(i) + '_inn2_bat.txt'
		f3 = './match'+ str(i)+ '/odi'+ str(i) + '_inn1_bowl.txt'
		f4 = './match'+ str(i)+ '/odi'+ str(i) + '_inn2_bowl.txt'
		f5 = './match'+ str(i)+ '/mom.txt'
		f6 = './match'+ str(i)+ '/wonby.txt'
		f7 = './match'+ str(i)+ '/tosswin.txt'
		
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
	print '-'*40 + 'QUERY-1'+'-'*40
	query1()
	print
	print '-'*40 + 'QUERY-2'+'-'*40
	query2()
	print
	print '-'*40 + 'QUERY-3'+'-'*40
	query3()
	print
	print '-'*40 + 'QUERY-4'+'-'*40
	query4()
	print
	print '-'*40 + 'QUERY-5'+'-'*40
	query5()
	print
	print '-'*40 + 'QUERY-6'+'-'*40
	query6()
	print
	print '-'*40 + 'QUERY-7'+'-'*40
	query7()
	print
	print '-'*40 + 'QUERY-8'+'-'*40
	query8()
	print
	print '-'*40 + 'QUERY-9'+'-'*40
	query9()
	print
	print '-'*40 + 'QUERY-10'+'-'*40
	query10()
	print
	print '-'*40 + 'QUERY-11'+'-'*40
	query11()
	print
	print '-'*40 + 'QUERY-12'+'-'*40
	query12()
	print
	print '-'*40 + 'QUERY-13'+'-'*40
	query13()
	print
	print '-'*40 + 'QUERY-14'+'-'*40
	query14()
	print
	print '-'*40 + 'QUERY-15'+'-'*40
	query15()
	print
	print '-'*40 + 'QUERY-16'+'-'*40
	query16()
	print
	print '-'*40 + 'QUERY-17'+'-'*40
	query17()
	print
	print '-'*40 + 'QUERY-18'+'-'*40
	query18()
	print
	print '-'*40 + 'QUERY-19'+'-'*40
	query19()
	print
	print '-'*40 + 'QUERY-20'+'-'*40
	query20()
	print

if __name__ == "__main__":
	main()
