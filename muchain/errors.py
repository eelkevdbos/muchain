class MuChainError(Exception):
    pass


class InvalidBlockHash(MuChainError):
    pass


class BlockIndexError(MuChainError):
    pass