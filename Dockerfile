FROM python:3.6
WORKDIR /muchain
RUN python -m pip install --upgrade pip pipenv
COPY Pipfile.lock Pipfile.lock
COPY Pipfile Pipfile
RUN pipenv install --deploy --system
COPY . /muchain
EXPOSE 50051
ENTRYPOINT ["python", "-m", "muchain.rpc.server"]