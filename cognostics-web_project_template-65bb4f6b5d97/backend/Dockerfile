FROM python:3-slim

WORKDIR /usr/src/app

# Install system requirements
RUN apt-get update -q \
  && apt-get install -qy netbase \
  && rm -r /var/lib/apt/lists/*

# Install python requirements
ADD requirements.txt ./
RUN pip install -r requirements.txt

# add the backend folder
ADD . .

CMD ["python", "./run.py"]
