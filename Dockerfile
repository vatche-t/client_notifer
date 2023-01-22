FROM python:3.8
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x bin/*.sh
CMD "bin/run_docker.sh"
