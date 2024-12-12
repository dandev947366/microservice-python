FROM docker.io/python:3.11

EXPOSE 8080

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./run_local.sh /code/run_local.sh

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

ENTRYPOINT ["bash", "./run_local.sh"]


