import time


class Customer(object):
    pass

class Order(object):
	pass

def load_orders(filename):
	orders = {}
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')
	columns = len(header)

	# Process each line in a file
	for line in f:
		# create a new instance of the class Order
		order = Order()

		#give that instance a new attribute for each header column, and
		#assign that attribute the value of the corresponding order column
		for i in range(columns):
			setattr(order, header[i], line[i])

		orders[order.order_id] = order

	# Close the file
	f.close()

	return orders

def load_customers(filename):
	customers = {}
	f = open(filename)

	# First line of the file should be the header, 
	#   split that into a list
	header = f.readline().rstrip().split(',')
	columns = len(header)
	# Process each line in a file, 
	# follow same logic as before for orders
	for line in f:
		customer = Customer()
		data = line.rstrip().split(',')
		for i in range(columns):
			setattr(customer, header[i], data[i])

		# Add the customer to our dictionary by customer id
		customers[customer.customer_id] = customer

	# Close the file
	f.close()

	return customers

def find_high_rollers(orders):
	"""Returns list of order ids where the order had more than 20 melons"""

	high_rollers = []
	order_ids = orders.keys()

	for order_id in order_ids:
		if int(orders[order_id].num_watermelons) > 20:
			high_rollers.append(order_id)

	return order_id


def display_customer(customer):
	print "---------------------"
	print "Next Customer to call"
	print "---------------------\n"
	print "Name: ", customer.first, customer.last
	print "Phone: ", customer.tel
	print "\n"

def main():

	customers = load_customers('customers.csv')
	orders    = load_orders('orders.csv')
	high_rollers = find_high_rollers(orders)

	#while True:
	for order_id in high_rollers:

		cid = orders[order_id].customer_id
		customer = customers[cid]

		if customer.called == '':
			display_customer(customer)
			break


		# print "Ready for next customer? (Y/N)"
		# answer = input('>> ').lower()
		# if answer == 'n':
		# 	break
		# else:
		# 	continue


if __name__ == '__main__':
	main()

#TESTING CODE




# # testing the customer function
# these_people = load_customers('customers.csv')
# keys = these_people.keys()
# for i in range(5):
# 	print these_people[keys[i]].email


# testing the order function
# these_orders = load_orders('orders.csv')

# keys = these_orders.keys()
# for i in range(5):
# 	print these_orders[keys[i]].num_watermelons



#THIS WOULD BE NICE BUT IS PROBABLY UNNECESSARY
# def merge_customers(orders, customers):

# 	orderids = orders.keys()
# 	important_attrs = [num_watermelons, num_othermelons, order_total]

# 	for orderid in orderids:
# 		cid = orders[orderid].customer_id
# 		setattr(customers[cid], address, orders[orderid].address)
# 		setattr(customers[cid], city, orders[orderid].city)
# 		setattr(customers[cid], address, orders[orderid].address)
# 		setattr(customers[cid], address, orders[orderid].address)
# 		setattr(customers[cid], address, orders[orderid].address)
# 		setattr(customers[cid], address, orders[orderid].address)

