FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR /mcrm
COPY . /mcrm/
RUN pip install poetry
RUN poetry install
# RUN poetry export --output otm/requirements.txt