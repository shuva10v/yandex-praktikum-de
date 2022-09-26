FROM python:3.9

COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt

COPY tracker.py /opt/app/
COPY index.html /opt/app/
EXPOSE 8082
WORKDIR /opt/app/
CMD ["uvicorn", "tracker:app", "--port", "8082", "--host", "0.0.0.0"]
