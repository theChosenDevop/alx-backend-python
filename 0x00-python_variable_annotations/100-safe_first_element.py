
#!/usr/bin/env python3
"""
    Defines 100-safe_first_element module
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
