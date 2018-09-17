import logging
from typing import Optional

from muchain import formatting
from muchain.chain import Chain
from muchain.errors import MuChainError
from muchain.errors import InvalidBlockHash
from muchain.errors import BlockIndexError
from muchain.miner import Miner
from muchain.proto.muchain_pb2 import Block


class MuChain:
    def __init__(self, chain: Chain, miner: Miner, clients: []):
        self.chain = chain
        self.miner = miner
        self.clients = clients

    def mine_block(self, block: Block) -> Block:
        # Update block index + prev_hash before mining
        self._set_block_index(block)
        self._set_previous_hash(block)
        # Mine block and append to chain
        self.miner.mine(block)
        self.chain.append(block)
        logging.info("Block mined: {}".format(formatting.block_to_json(block)))
        # Propagate block to other clients
        self._propagate_block(block)
        return block

    def receive_block(self, block) -> Optional[MuChainError]:
        logging.info("Block received: {}".format(formatting.block_to_json(block)))
        if not self.miner.has_valid_hash(block):
            return InvalidBlockHash("Invalid block hash: {}".format(block.hash))
        if block.index != self.chain.next_index():
            return BlockIndexError("Invalid block index: {}".format(block.index))
        self.chain.append(block)

    def latest_block(self) -> Optional[Block]:
        return self.chain.latest_block()

    def _set_block_index(self, block):
        # Set block index to next in chain
        block.index = self.chain.next_index()

    def _set_previous_hash(self, block):
        # Update block prev hash, but skip if genesis
        if block.index > 0:
            block.previous_hash = self.miner.hash(self.chain.latest_block())

    def _propagate_block(self, block):
        """Propagate block to other clients"""
        for client in self.clients:
            client.ReceivePropagatedBlock(block)


def build_arg_parser():
    import argparse
    parser = argparse.ArgumentParser('muchain')
    parser.add_argument('--difficulty', required=False, default=4, type=int)
    parser.add_argument('--loglevel', required=False, default='debug', type=str)
    parser.add_argument('--node', required=False, action='append', default=[])
    return parser
