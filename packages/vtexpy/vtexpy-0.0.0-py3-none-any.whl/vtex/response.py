from typing import Any, Dict, List, Union

from dataclasses import dataclass


@dataclass(frozen=True)
class VTEXResponse:
    data: Union[Dict[str, Any], List[Any], None]
    status: int
    headers: Dict[str, str]
