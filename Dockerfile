FROM python:latest

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]