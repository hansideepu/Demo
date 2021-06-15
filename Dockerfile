FROM python:3.7
COPY .  /src
WORKDIR /src
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python","run.py"]
