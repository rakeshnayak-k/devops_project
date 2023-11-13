FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["python","manage.py", "runserver","127.0.0.1:8000"]

