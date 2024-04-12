from sqlalchemy import create_engine, insert, text
import time
import psycopg2 

time.sleep(5)

class ProcessCSVFile:
	def __init__(self):
		self.conn = psycopg2.connect(database="db", 
						user='root', password='password',  
						host='127.0.0.1', port='5432'
				)

		self.conn.autocommit = True
		self.cursor = conn.cursor() 
		print("Database connection is successful...")

	def rows_from_a_csv_file(self, filename, skip_first_line=False, dialect='excel', **fmtparams):
		with open(filename, 'r') as csv_file:
			reader = csv.reader(csv_file, dialect, **fmtparams)
			if skip_first_line:
				next(reader, None)
			for row in reader:
				yield row

	def push_row_data_to_db(self):
		for row in self.rows_from_a_csv_file(csv_file_path, skip_first_line=True):
			print(row[0])

			query = "INSERT INTO sales(TransactionID , ProductID , Quantity, SalePrice , PurchasePrice) values(%s,%s,%s,%s,%s)"%(row[0])

			self.cursor.execute(query)

			self.conn.commit()


	def export_csv_to_db(self, csv_file_path):
		query = "COPY sales(TransactionID , ProductID , Quantity, SalePrice , PurchasePrice) FROM "+csv_file_path+" DELIMITER ';'CSV HEADER;"
  
		self.cursor.execute(query)
		self.conn.commit()


	def close_db_conn(self):
		self.conn.close()


# engine = create_engine("postgresql+psycopg2://root:password@db:5432/db")
# conn = engine.connect()
# query=text("INSERT INTO identity (_name, surname) VALUES ('Michel', 'Palefrois'), ('Renaud', 'Bertop');")
# conn.execute(query)
# conn.commit()

# print('done')

def main():
	processCSVFile = ProcessCSVFile()

	option = int(input("Enter 1 to process row by row, 2 to push entire csv.\n"))

	match option:
		case 1:
			processCSVFile.push_row_data_to_db()

		case 2:
			csv_file_path = input("Enter the valid csv file path:: ")

			if csv_file_path != "":
				processCSVFile.export_csv_to_db(csv_file_path)


			else:
				print("CSV file path is an empty string. Using the default csv file...")
				processCSVFile.export_csv_to_db("../sales_data.csv")

if __name__ == '__main__':
	main()