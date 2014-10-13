"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_name, melon_seedless, melon_price

def make_melon_dict(name_dict, seed_dict, price_dict):
	d = {}

	for i in range(1,6):
		d[name_dict[i]] = [seed_dict[i], price_dict[i]]

	#print d
	return d

def print_melon(melon_info):

	for key in melon_info.keys():
		if melon_info[key][0] == True:
			seedstate = 'have'
		else:
			seedstate = 'do not have'

		print "%ss %s seeds and are $%0.2f" % (key, seedstate, 
			melon_info[key][1])


if __name__ == '__main__':
    big_melon_dict = make_melon_dict(melon_name, melon_seedless, 
    	melon_price)

    print_melon(big_melon_dict)

