FROM python:3.9

COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt

COPY Visualisation.ipynb /opt/scripts/

EXPOSE 8082

CMD ["voila", "--port=8082", "--Voila.ip='0.0.0.0'", "--theme=dark", "/opt/scripts/"]
#CMD voila --port=8082 --theme=dark /opt/scripts/