FROM python:3.12.4
WORKDIR /proyecto
RUN apt-get update
RUN apt install sqlite3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "proyecto/manage.py", "runserver", "0.0.0.0:8000"]