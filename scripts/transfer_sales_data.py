from sqlalchemy import create_engine, insert, text
import time
import psycopg2
import csv

time.sleep(5)

class ProcessCSVFile:
	def __init__(self):
		self.conn = psycopg2.connect(database="db", user='postgres', password='password', host='db', port='5432')

		self.conn.autocommit = True
		self.cursor = self.conn.cursor() 
		print("Database connection is successful...")

	def rows_from_a_csv_file(self, filename, skip_first_line=False, dialect='excel', **fmtparams):
		with open(filename, 'r') as csv_file:
			reader = csv.reader(csv_file, dialect, **fmtparams)
			if skip_first_line:
				next(reader, None)
			for row in reader:
				yield row

	def push_row_data_to_db(self, csv_file_path):
		for row in self.rows_from_a_csv_file(csv_file_path, skip_first_line=True):
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


	def export_csv_to_db(self, csv_file_path):
		query = "COPY sales(transaction_id , product_id , quantity, sale_price , purchase_price) FROM "+csv_file_path+" DELIMITER ';'CSV HEADER;"
  
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

	option = 1

	# csv_file_path = input("Enter the valid csv file path:: ")
	csv_file_path = "../sales_data.csv"

	match option:
		case 1:
			if csv_file_path != "":
				processCSVFile.push_row_data_to_db(csv_file_path)


			else:
				print("CSV file path is an empty string. Using the default csv file...")
				processCSVFile.push_row_data_to_db("../sales_data.csv")


		case 2:
			if csv_file_path != "":
				processCSVFile.export_csv_to_db(csv_file_path)


			else:
				print("CSV file path is an empty string. Using the default csv file...")
				processCSVFile.export_csv_to_db("../sales_data.csv")

if __name__ == '__main__':
	main()