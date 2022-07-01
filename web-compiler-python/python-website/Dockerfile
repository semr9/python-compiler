FROM python:3.6-alpine

RUN adduser -D helloworlduser

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py wsgi.py boot.sh ./
RUN chmod +x boot.sh
COPY templates /app/templates
COPY static /app/static
#COPY . /app

ENV FLASK_APP main.py

RUN chown -R helloworlduser:helloworlduser ./
USER helloworlduser

RUN ls /app

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]