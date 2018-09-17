.PHONY: protoc

protoc:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./muchain/proto/muchain.proto

start:
	docker-compose up --build

stop:
	docker-compose down

sim:
	python -m muchain.tools.simulator

test-e2e:
	python -m unittest muchain.test.e2e