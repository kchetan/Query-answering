import nltk	
import sys


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
#	print dictionary

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
def make_model_and_answer(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain

	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  srate(x) -> gtsix(x) given srate(x) is true"
	
	l = nltk.LogicParser()
	c1 = l.parse(' ((srate(x)) & (srate(x) -> gtsix(x)))')
	varnames =  m.satisfiers(c1, 'x', g)
	#print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p



# the function to 
#	1. generate the appropriate Model, after getting the values of the required predicates;
#	2. construct the query 
#	3. to prove/disprove the query.
def generate_and_solve_query1(bats, bowl):
	
	# for this query, we only need to consider the columns in bats dictionary
	c1 = parse_for_sr(bats, 150.0)
	c2 = parse_for_six(bats, 0)

	#print c1
	#print c2

	#Now constructing strings which are needed to create the model:

	#first creating mapping from playername to variable: we create a temporary dictionary
	# For example,
	# MS Dhoni => r1
	# SK Raina => r2

	name_to_var = {}
	count = 0
	for i in bats:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'

	# this is for the predicate "srate"
	temp_strin2 = 'srate => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','

	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'


	#now for the predicate "gtsix"
	temp_strin3 = 'gtsix => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','

	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	print name_to_var
	print temp_strin1
	print temp_strin2
	print temp_strin3


	v = temp_strin1 + temp_strin2 + temp_strin3
	#print v

	# now forming the query
	query = 'all x (srate(x) -> gtsix(x))'

	make_model_and_answer(v, query, name_to_var)


def main():

	bats = {}
	bowl = {}
	f1 = './dataset/match2/odi2_inn1_bat.txt'
	f2 = './dataset/match2/odi2_inn2_bat.txt'
	f3 = './dataset/match2/odi2_inn1_bowl.txt'
	f4 = './dataset/match2/odi2_inn1_bowl.txt'
	
	add_to_dict(bats, f1)
	add_to_dict(bats, f2)

	add_to_dict(bowl, f3)
	add_to_dict(bowl, f4)
	generate_and_solve_query1(bats, bowl)

if __name__ == "__main__":
	main()
