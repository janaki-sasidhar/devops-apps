FROM python:3.12-bullseye
RUN apt update -y
RUN pip install flask
WORKDIR /app
COPY script.py /app/script.py
EXPOSE 5000
ENV FLASK_APP=script.py
CMD ["flask", "run", "--host=0.0.0.0"]