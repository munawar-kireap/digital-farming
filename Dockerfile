FROM public.ecr.aws/docker/library/python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 80

CMD [ "uvicorn", "app.main:app" , "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]