import unittest
from transfer_sales_data import ProcessCSVFile
from constants import Constants
from app import Aggregation

class Test(unittest.TestCase):
	def test_data_upload_to_database(self):
		try:
			ProcessCSVFile().push_row_data_to_db("sample_data.csv")
		except:
			self.fail("Data upload failed")
	
	def test_aggregation_process_data(self):
		print(Aggregation().process_data())


if __name__ == '__main__':
    unittest.main()