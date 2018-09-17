import hashlib
import json
from muchain.proto.muchain_pb2 import Block


def serialize_block_canonical(block: Block) -> str:
    """Serialize a block in a canonical manner"""
    props = {'index': block.index, 'data': block.data, 'nonce': block.nonce, 'previous_hash': block.previous_hash}
    return json.dumps(props, sort_keys=True).encode()


class Miner:
    def __init__(self, difficulty=3, hash_algo='sha256'):
        self.difficulty = difficulty
        self.hash_algo = hash_algo
        self._hash = getattr(hashlib, self.hash_algo, None)

    def hash(self, block):
        """Hash a block and return as hex digest"""
        return self._hash(serialize_block_canonical(block)).hexdigest()

    def has_valid_hash(self, block: Block):
        _block_hash = self.hash(block)
        return _block_hash[0:self.difficulty] == "0" * self.difficulty

    def mine(self, block: Block):
        while not (self.has_valid_hash(block)):
            block.nonce = block.nonce + 1
        block.hash = self.hash(block)

    def __repr__(self):
        return "<{} difficulty={} algo={}>".format(self.__class__.__name__, self.difficulty, self.hash_algo)
