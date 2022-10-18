FROM python:3.10

ENV APP_HELP /app

WORKDIR $APP_HELP

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "HW_2.py"]