class Constants:
	# -------------Database credentials--------------------
	database="db"
	user='postgres'
	password='password'
	host='db'
	port='5432'


	# -------------CSV file path---------------------------
	csv_file_path = "../sales_data_cleaned.csv"


	# -------------Database Queries------------------------
	view_query = """create view cte as
	(select *, quantity*(sale_price-purchase_price) as profit
	from public.sales) """

	trans_profit_query = """select transaction_id, round(cast(sum(profit) as numeric), 2)
	from cte
	group by transaction_id
	having sum(profit) > 0.0
	order by sum(profit) desc"""

	prod_profit_query = """select product_id, round(cast(sum(profit) as numeric), 2)
	from cte
	group by product_id
	having sum(profit) > 0.0
	order by sum(profit) desc"""

	top_prod_query = """select x.product_id from 
	(select product_id, sum(quantity), dense_rank() over(order by sum(quantity) desc) as r
	from public.sales
	group by product_id
	order by sum(quantity) desc) x
	where x.r < 3"""