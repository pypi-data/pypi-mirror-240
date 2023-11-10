def bool_to_char(b: bool) -> str:
    return {False: "n", True: "y"}[b]


def char_to_bool(c: str, default: bool = True) -> bool:
    """
    Transform a given char to boolean value. Raises KeyError if the char is not y/Y/n/N or empty.
    """
    return {"n": False, "y": True, "": default}[c.lower()]
