FROM python:3.8.1
ADD . /photoshop_detector
WORKDIR /photoshop_detector
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]