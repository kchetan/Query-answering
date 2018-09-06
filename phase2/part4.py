import nltk	
import sys
import re

from nltk.corpus import wordnet as wn

powerplay={'1':'35 over - bowler I Sharma\n34 over - bowler Anderson','2':'29 over - bowler Southee\n34 over - bowler Jadeja','3':'34 over - bowler Kumar','4':'35 over - bowler Southee\n35 over - bowler Ashwin','5':'33 over - bowler Mcclenaghan\n35 over - bowler Shami'}
weather={'4':'It"s a clear and sunny day','2':' the weather is fair at the moment and the forecast for the day isn"t bad','3':'It s nice and clear','1':'Looks a beautiful morning','5':'A nice weather for a game of cricket'}
match=[0]
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

def srchcom(mat,bold,player,words):
	com1=match[mat].indcom
	com2=match[mat].nzcom
	com=com1+com2[1:]
	m=0
	dic={}
	syns=[]
	if bold:
		syns = wn.synsets(bold)
	barr=[]
	for s in syns:
		for l in s.lemmas:
			if l.name not in barr and l.name!='away':
				barr.append(l.name)
	
	arr=[]
	for i in words:
		syns = wn.synsets(i)
		for s in syns:
			for l in s.lemmas:
				if l.name not in arr and l.name!='away':
					arr.append(l.name)
	for i in range(1,len(com)):
		h=0
		string=com[i].values()[0]
		if player and re.search(player,string,re.I):
			h=h+100
		for j in barr:
			if  re.search(' '+j+'[^a-zA-Z],*',string,re.I):
				h=h+45
		for j in arr:
			if re.search(' '+j+'[^a-zA-Z],*',string,re.I):
				h=h+20
		if h>=m:
			#print com[i]
			m=h
			dic=com[i]
	return dic


def query_processing(q):
	match=0
	bold=None
	s1=re.search(r'<b>(.*?)</b>',q,re.I)
	if s1:
		bold=s1.group(1)
		q=q.replace(s1.group(0),'')
	q=q.replace(',','')
	q=q.replace('?','')
	q=q.replace('.','')
	if re.search('match 1',q,re.I):
		match=1
		q=q.replace('match 1','')
	elif re.search('first match',q,re.I):
		match=1
		q=q.replace('first match','')
	elif re.search('match 2',q,re.I):
		match=2
		q=q.replace('match 2','')
	elif re.search('second match',q,re.I):
		match=2
		q=q.replace('second match','')
	elif re.search('match 3',q,re.I):
		match=3
		q=q.replace('match 3','')
	elif re.search('third match',q,re.I):
		match=3
		q=q.replace('third match','')
	elif re.search('match 4',q,re.I):
		match=4
		q=q.replace('match 4','')
	elif re.search('fourth match',q,re.I):
		match=4
		q=q.replace('fourth match','')
	elif re.search('match 5',q,re.I):
		match=5
		q=q.replace('match 5','')
	elif re.search('fifth match',q,re.I):
		match=5
		q=q.replace('fifth match','')
	words=q.split(' ')
	prep=['was','in','the','is','on','of','for','by','from','to']
	ques=['what','which','who','when','how']
	player=None
	i=0
	while i< len(words):
		words[i]=words[i].lower()
		if  words[i] in ques:
			words.remove(words[i])
			i=i-1
		i+=1
	if '' in words:
		words.remove('')
	for j in prep:
		i=0
		while i<len(words):
			#print j,words[i],i
			if re.search('^'+str(j)+'$',words[i],re.I):
				try:
					words.remove(words[i])
					i=i-1
				except:
					break
			i+=1
	if '' in words:
		words.remove('')
	for i in words:
		for j in ind_prof.keys():
			if re.search(i,j,re.I):
				player=i
				words.remove(i)
				break
		for j in nz_prof.keys():
			if re.search(i,j,re.I):
				player=i
				words.remove(i)
				break
	#print words,bold,player,match
	if bold=='dismissed':
		bold='out'
	elif bold=='boundary':
		bold='four'
	elif bold=='single':
		bold='1 run'
	if re.search('powerplay',q,re.I):
		print powerplay[str(match)]
	elif re.search('weather',q,re.I):
		print weather[str(match)]
	else:
		dic=srchcom(match,bold,player,words)
		b=int((dic.keys()[0]))
		if b%6==0:
			b=b/6-1
			o=str(b)+'.'+'6'
		else:
			o=str(b/6)+'.'+str(b%6)
			b=b/6
		print o,'---> ',dic.values()[0]


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
