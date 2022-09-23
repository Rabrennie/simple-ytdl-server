FROM sanicframework/sanic:3.8-latest

RUN apk add gcc g++ make libffi-dev openssl-dev

WORKDIR /sanic

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]
