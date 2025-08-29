FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5010
CMD ["python3", "flask_test.py"]