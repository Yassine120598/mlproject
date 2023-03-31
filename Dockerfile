FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080