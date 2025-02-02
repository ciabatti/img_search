# Usa un'immagine Python leggera
FROM python:3.10-slim

# Evita la scrittura di bytecode e assicura output immediato nei log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Imposta la directory di lavoro
WORKDIR /app

# Installa dipendenze di sistema necessarie (opzionale ma consigliato per alcuni pacchetti Python)
RUN apt-get update && apt-get install -y gcc

# Copia il file requirements.txt ed installa le dipendenze
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia tutto il progetto dentro il container
COPY . /app/

# Colleziona i file statici (senza chiedere input)
RUN python manage.py collectstatic --noinput

# Comando per avviare Django con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "image_search.wsgi:application"]
