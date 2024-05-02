
#!/usr/bin/env python3
"""
    Defines 100-safe_first_element module
"""


def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None