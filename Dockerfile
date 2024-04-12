FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./scripts/transfer_sales_data.py"]