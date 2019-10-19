FROM python:3.7.5

ENV \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VERSION=0.12.17

RUN mkdir /mate3 && pip --no-cache-dir install poetry
WORKDIR /mate3
ADD pyproject.toml poetry.lock /mate3/
RUN poetry install --no-interaction --no-dev --extras=mate3_pg

ADD mate3 /mate3/mate3
ADD registry_data /mate3/registry_data
ADD pg_config.yaml /mate3/

CMD poetry run mate3
