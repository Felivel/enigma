FROM python:3.6-alpine

ENV FLASK_APP app.py

RUN adduser -D enigma
USER enigma

WORKDIR /home/enigma

RUN python -m venv venv
RUN venv/bin/pip install flask

COPY templates templates
COPY app.py boot.sh ./

# run-time configuration
EXPOSE 5000

ENTRYPOINT ["./boot.sh"]