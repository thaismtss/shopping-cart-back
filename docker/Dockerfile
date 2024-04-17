FROM python:3.10 as python-base

ENV POETRY_VERSION=1.8.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

ENV POETRY_CACHE_DIR=/opt/.cache

FROM python-base as poetry-base

RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

FROM python-base as dev
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_DEBUG=on
ENV DEBUG=True

COPY ./app /app

RUN mkdir /app/migrations

COPY migrations /app/migrations

EXPOSE 5000

CMD python -m flask db upgrade && python -m flask run --host=0.0.0.0