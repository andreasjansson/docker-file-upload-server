FROM python:3.9-slim
RUN pip install flask
RUN mkdir /uploads
COPY server.py /server.py
CMD ["python", "/server.py"]
