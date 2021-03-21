FROM python:3.8.0

ENV VIRTUAL_ENV=/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY makefile makefile
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN . /venv/bin/activate && make install

COPY . .

CMD [ "make", "run"]
