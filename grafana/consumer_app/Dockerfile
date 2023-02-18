FROM python:3.9

COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt

COPY consumer.py /opt/app/
WORKDIR /opt/app/
CMD ["python3", "consumer.py", "test_topic"]
