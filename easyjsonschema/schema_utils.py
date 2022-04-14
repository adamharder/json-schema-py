from typing import Optional
import jsonschema


def optional_int_check(some_val:Optional[int]):
    if some_val is not None:
        if not isinstance(some_val, int):
            raise jsonschema.ValidationError(f"value ({some_val}) must be an integer.")


def optional_bool_check(some_val:Optional[bool]):
    if some_val is not None:
        if not isinstance(some_val, bool):
            raise jsonschema.ValidationError(f"value ({some_val}) must be a boolean.")
