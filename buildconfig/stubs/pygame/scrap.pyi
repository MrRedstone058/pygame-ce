from typing import List, Optional
from collections.abc import ByteString

def init() -> None: ...
def get_init() -> bool: ...
def get(data_type: str) -> Optional[bytes]: ...
def get_types() -> List[str]: ...
def put(data_type: str, data: ByteString) -> None: ...
def contains(data_type: str) -> bool: ...
def lost() -> bool: ...
def set_mode(mode: int) -> None: ...
def put_text(text: str) -> None: ...
def get_text() -> str: ...
def has_text() -> bool: ...
