# Copyright ©, 2022-present, Lightspark Group, Inc. - All Rights Reserved

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass
class UpdateNodeSharedSecretInput:
    node_id: str

    shared_secret: str


def from_json(obj: Mapping[str, Any]) -> UpdateNodeSharedSecretInput:
    return UpdateNodeSharedSecretInput(
        node_id=obj["update_node_shared_secret_input_node_id"],
        shared_secret=obj["update_node_shared_secret_input_shared_secret"],
    )
