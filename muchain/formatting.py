from google.protobuf import json_format

from muchain.proto.muchain_pb2 import Block


def block_to_json(block: Block) -> str:
    return json_format.MessageToJson(block, including_default_value_fields=True)