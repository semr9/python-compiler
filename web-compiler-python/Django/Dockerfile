# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /server
COPY /server /server/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # syntax=docker/dockerfile:1
# FROM python:3

# RUN apt-get update

# # WORKDIR /code
# COPY requirements.txt requirements.txt
# RUN python -m pip install --upgrade pip
# RUN pip install -r requirements.txt

# COPY . .

# WORKDIR /server

# EXPOSE 8000

# CMD ["ls", "manage.py", "runserver", "127.0.0.1:8000"]