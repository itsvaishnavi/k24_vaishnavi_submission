# Importing essential libraries
import time
import psycopg2
import csv
from constants import Constants

time.sleep(5)

class ProcessCSVFile:
	# Database connection initialization
	def __init__(self):
		self.c= Constants()

		# DB connection string
		self.conn = psycopg2.connect(database=self.c.database, user=self.c.user, password=self.c.password, host=self.c.host, port=self.c.port)

		self.conn.autocommit = True
		self.cursor = self.conn.cursor() 
		print("Database connection is successful...")


	# Generator function to get all the rows in csv
	def rows_from_a_csv_file(self, filename, skip_first_line=False, dialect='excel', **fmtparams):
		with open(filename, 'r') as csv_file:
			reader = csv.reader(csv_file, dialect, **fmtparams)
			if skip_first_line:
				next(reader, None)
			for row in reader:
				yield row


	# Store data into the database
	def push_row_data_to_db(self, csv_file_path):
		# list to store the row data if database upload fails
		self.failed_upload = []

		
		for row in self.rows_from_a_csv_file(csv_file_path, skip_first_line=True):
			try:
				# Data validation in the python script in order to upload data to db and to ensure the right data type
				t_id = int(row[0])
				p_id = int(row[1])
				quantity = int(row[2])
				sp = float(row[3])
				pp = float(row[4])
				
				# row = tuple(row)
				# print(t_id, p_id, quantity, sp, pp)

				# SQL query
				query = "INSERT INTO sales(transaction_id , product_id , quantity, sale_price , purchase_price) values (%s,%s,%s,%s,%s)"%(t_id, p_id, quantity, sp, pp)

				self.cursor.execute(query)

				self.conn.commit()
				
			
			except Exception as e:
				self.failed_upload.append(row)
				print("Exception::", e)

		
	
	# close db connection
	def close_db_conn(self):
		self.conn.close()


# main function
def main():
	processCSVFile = ProcessCSVFile()

	csv_file_path = processCSVFile.c.csv_file_path #value set as "../sales_data_cleaned.csv"

	processCSVFile.push_row_data_to_db(csv_file_path)


# driver code
if __name__ == '__main__':
	main()