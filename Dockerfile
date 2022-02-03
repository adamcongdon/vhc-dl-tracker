# syntax=docker/dockerfile:1

FROM python

WORKDIR /the/workdir/path

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
#CMD ["/bin/bash", "-c", "python3", -m , "gunicorn", "app:server", "--host=0.0.0.0"]