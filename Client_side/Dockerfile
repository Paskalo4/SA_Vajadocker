# Uporabi Python 3.9 slim kot osnovno sliko
FROM python:3.9-slim

# Nastavi delovni imenik za odjemalca
WORKDIR /client

# Kopiraj vse datoteke iz trenutnega imenika (v okviru gradbenega konteksta) v imenik v vsebniku
COPY . /client

# Namesti potrebne Python knjižnice (Flask in requests)
RUN pip install --no-cache-dir Flask requests

# Odpiraj vrata za povezavo (port 8080)
EXPOSE 8080

# Zaženi Python aplikacijo
CMD ["python", "client.py"]
