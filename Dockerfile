FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./scripts ./scripts

ADD sample_data.csv ./scripts

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]