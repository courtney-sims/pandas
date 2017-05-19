FROM ubuntu:latest
RUN apt-get update -y && apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENV FLASK_APP hello.py
ENTRYPOINT ["python"]
#CMD ["-m flask run"]
CMD ["hello.py"]
