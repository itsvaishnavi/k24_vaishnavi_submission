from transfer_sales_data import ProcessCSVFile
from constants import Constants

class Aggregation:
	def __init__(self):
		self.p = ProcessCSVFile()
		self.c= Constants()


	def process_data(self):
		self.p.cursor.execute(view_query)

		print("View created successfully...")

		self.p.cursor.execute(trans_profit_query)

		self.p.cursor.execute(prod_profit_query)

		self.p.cursor.execute(top_prod_query)