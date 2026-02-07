FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
ENV FLAG=CTF{easy_upload_validation}
EXPOSE 5000
CMD ["python","app.py"]
