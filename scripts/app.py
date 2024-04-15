# Import essential modules and libraries
from transfer_sales_data import ProcessCSVFile
from constants import Constants
from decimal import *

class Aggregation:
	def __init__(self):
		self.p = ProcessCSVFile() #Database connection definition
		self.c= Constants() #SQL queries


	def process_data(self):
		try:
			
			#Exceutes create view query
			self.p.cursor.execute(self.c.view_query) 

			print("View created successfully...")
			
			#=============Exceutes transaction profit query=============
			self.p.cursor.execute(self.c.trans_profit_query) 

			trans_profit_records = self.p.cursor.fetchall()

			# print(list(trans_profit_records))

			trans_profit_dict = dict(list(trans_profit_records))

			trans_profit_dict = {k:float(v) for k,v in trans_profit_dict.items()}

			#=============Exceutes product profit query=============
			self.p.cursor.execute(self.c.prod_profit_query) 

			prod_profit_records = self.p.cursor.fetchall()

			# print(list(prod_profit_records))

			prod_profit_dict = dict(list(prod_profit_records))

			prod_profit_dict = {k:float(v) for k,v in prod_profit_dict.items()}

			#=============Exceutes top products query=============
			self.p.cursor.execute(self.c.top_prod_query) 

			top_prod_records = self.p.cursor.fetchall()

			# print(list(top_prod_records))

			out = []
			for t in list(top_prod_records):
				for item in t:
					out.append(item)

			t=(trans_profit_dict, prod_profit_dict, out)
			
			return t

		except Exception as e:
			print("Exception :: ", e)
		

def main():
	aggregation = Aggregation()

	print(aggregation.process_data())


if __name__ == '__main__':
	main()