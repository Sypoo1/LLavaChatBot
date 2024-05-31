FROM python:3.11.4-slim

RUN apt-get update && apt-get install -y 

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "--server.enableCORS=false", "--server.port=8501", "main.py"]
