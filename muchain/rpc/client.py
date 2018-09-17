import time

import grpc
from google.protobuf.empty_pb2 import Empty

from muchain.proto import muchain_pb2_grpc


def build_channel(address):
    return grpc.insecure_channel(address)


def build_client(address) -> muchain_pb2_grpc.MuChainStub:
    channel = build_channel(address)
    return muchain_pb2_grpc.MuChainStub(channel)


def wait_for_client(client):
    while True:
        try:
            return client.Ping(Empty())
        except Exception:
            time.sleep(1)
