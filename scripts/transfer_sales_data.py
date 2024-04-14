# Importing essential libraries
import time
import psycopg2
import csv

time.sleep(5)

class ProcessCSVFile:
	# Database connection initialization
	def __init__(self):
		self.conn = psycopg2.connect(database="db", user='postgres', password='password', host='db', port='5432')

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
		self.failed_upload = []

		for row in self.rows_from_a_csv_file(csv_file_path, skip_first_line=True):
			try:
				t_id = int(row[0])
				p_id = int(row[1])
				quantity = int(row[2])
				sp = float(row[3])
				pp = float(row[4])
				
				# row = tuple(row)
				print(t_id, p_id, quantity, sp, pp)

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

	# csv_file_path = input("Enter the valid csv file path:: ")
	csv_file_path = "../sales_data_cleaned.csv"

	if csv_file_path != "":
		processCSVFile.push_row_data_to_db(csv_file_path)


	else:
		print("CSV file path is an empty string. Using the default csv file...")
		processCSVFile.push_row_data_to_db("../sales_data_cleaned.csv")


	processCSVFile.close_db_conn()

# driver code
if __name__ == '__main__':
	main()