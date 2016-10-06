FROM python:3.6

RUN apt-get update
RUN pip install --upgrade pip

RUN apt-get install -y liblapack-dev libatlas-base-dev gfortran g++

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN pip install nose==1.3.7 coveralls==1.1 pylint==1.6.4

WORKDIR /app
COPY . /app/

RUN chmod -R 644 /app/tests

CMD ["/app/inspect.sh"]
