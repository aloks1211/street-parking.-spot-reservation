FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app/streetparkingspotreservation
COPY requirements.txt /app/streetparkingspotreservation
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
