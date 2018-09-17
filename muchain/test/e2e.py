import unittest

from google.protobuf.empty_pb2 import Empty

from muchain import formatting
from muchain.proto.muchain_pb2 import Block
from muchain.rpc.client import build_client, wait_for_client


def create_clients():
    # Setup two rpc clients and wait for them to respond to pings
    client_a = build_client("localhost:5001")
    client_b = build_client("localhost:5002")

    wait_for_client(client_a)
    wait_for_client(client_b)

    return client_a, client_b


def start_stack():
    # Start our dev stack by executing docker-compose up
    # Not the cleanest, very effective
    import subprocess
    process = subprocess.Popen(
        "docker-compose up -d &> /dev/null",
        shell=True
    )
    process.wait()


class TestBlockPropagation(unittest.TestCase):

    @staticmethod
    def test_latest_hash_is_equal_between_clients():
        start_stack()
        client_a, client_b = create_clients()
        block_mined = client_a.MineBlock(Block(data="block_mined_on_a"))

        client_a_block = client_a.LatestBlock(Empty())
        client_b_block = client_b.LatestBlock(Empty())

        print("Latest block for client_a: {}".format(formatting.block_to_json(client_a_block)))
        print("Latest block for client_b: {}".format(formatting.block_to_json(client_b_block)))

        assert block_mined.hash == client_a_block.hash, "Latest block hash not equal to just mined block hash"
        assert client_a_block.hash == client_b_block.hash, "Latest block hash between clients not equal"
