import string
import time
import random

from muchain.proto.muchain_pb2 import Block
from muchain.rpc.client import build_client


def simulate():
    clients = [build_client('localhost:5001'), build_client('localhost:5002'), build_client('localhost:5003'), ]
    while True:
        # Pick a random client
        client = clients[random.randint(0, len(clients) - 1)]
        # Generate a random block with random data
        _block = client.MineBlock(Block(data=("".join([random.choice(string.ascii_letters) for _ in range(15)]))))
        # Sleep for a bit
        time.sleep(random.randint(5, 10))


if __name__ == '__main__':
    simulate()
