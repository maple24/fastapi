FROM python:3.9.15-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend
COPY ./requirements.txt /backend/
RUN pip install --no-cache-dir -r /backend/requirements.txt
COPY . /backend/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]