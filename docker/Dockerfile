FROM python:3.10 as python-base

ENV POETRY_VERSION=1.8.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

ENV POETRY_CACHE_DIR=/opt/.cache

FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

FROM python-base as example-app

COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app


COPY poetry.lock pyproject.toml ./


RUN poetry install --no-interaction --no-cache

COPY ./app /app

RUN mkdir /app/migrations

COPY migrations /app/migrations

EXPOSE 5000


CMD poetry run python -m flask db upgrade && poetry run python -m flask run --host=0.0.0.0