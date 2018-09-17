from typing import Optional

from muchain.proto.muchain_pb2 import Block


class Chain:
    def __init__(self, blocks: [Block] = []):
        self.blocks = blocks

    def append(self, block: Block):
        self.blocks.append(block)

    def next_index(self) -> int:
        return len(self.blocks)

    def latest_block(self) -> Optional[Block]:
        return self.blocks[-1]
