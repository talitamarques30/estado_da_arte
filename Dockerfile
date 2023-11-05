FROM python:3.11

WORKDIR /app
EXPOSE 8000
COPY . .

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]