FROM python:3.10 as base
LABEL authors="leonardo"

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN apt-get install postgresql-client libjpeg-dev -y

RUN apt-get install gcc libc-dev musl-dev zlib1g zlib1g-dev -y

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
#RUN apk del .tmp-build-deps

########
FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
#########

COPY . .