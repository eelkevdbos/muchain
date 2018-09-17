import logging
import time
from concurrent import futures

import grpc
from google.protobuf.empty_pb2 import Empty

from muchain.chain import Chain
from muchain.muchain import MuChain, build_arg_parser
from muchain.miner import Miner
from muchain.proto import muchain_pb2_grpc
from muchain.rpc.client import build_client
import muchain.proto.muchain_pb2 as proto
from muchain.proto.muchain_pb2_grpc import MuChainServicer


class Servicer(MuChainServicer):

    def __init__(self, client: MuChain):
        self.client = client

    def MineBlock(self, request: proto.Block, context):
        return self.client.mine_block(request)

    def ReceivePropagatedBlock(self, request: proto.Block, context):
        error = self.client.receive_block(request)
        return proto.Response(ok=(error is None), error=str(error))

    def LatestBlock(self, request, context):
        return self.client.latest_block() or proto.Block()

    def Ping(self, request, context):
        return Empty()


def serve():
    parser = build_arg_parser()
    args = parser.parse_args()
    logging.getLogger().setLevel(getattr(logging, args.loglevel.upper()))

    if len(args.node) == 0:
        logging.warning("MuChain initialized without peer nodes")

    mu = MuChain(
        chain=Chain(),
        miner=Miner(difficulty=args.difficulty),
        clients=[build_client(node) for node in args.node]
    )

    # Add servicer to grpc server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    muchain_pb2_grpc.add_MuChainServicer_to_server(Servicer(mu), server)
    _start_server_blocking(server, '[::]:50051')


def _start_server_blocking(server, listen_address):
    try:
        server.add_insecure_port(listen_address)
        server.start()
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
