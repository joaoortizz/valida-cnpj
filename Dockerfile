FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY ./app /app