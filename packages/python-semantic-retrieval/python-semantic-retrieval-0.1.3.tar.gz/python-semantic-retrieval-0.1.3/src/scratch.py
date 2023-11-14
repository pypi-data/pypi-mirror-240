import asyncio
import dataclasses
from typing import Any
from pydantic import BaseModel
from result import Err, Ok, Result


# Define a dataclasses.dataclass object
@dataclasses.dataclass
class MyDataClass:
    integer_field: int
    string_field: str


# Define a pydantic BaseModel object
class MyPydanticModel(BaseModel):
    integer_field: int
    string_field: str


data_class_object = MyDataClass(123, "test string")
pydantic_object = MyPydanticModel(integer_field=123, string_field="test string")


def test_case(data: Any):
    print("\n\n", data)
    print(safe_serialize_arbitrary_for_logging(data, max_elements=10))


def safe_serialize_arbitrary_for_logging(data: Any, max_elements: int = 10, indent: str = ""):
    match data:
        case Ok(ok):
            return safe_serialize_arbitrary_for_logging({"Ok": ok}, max_elements, indent + "  ")
        case Err(err):
            return safe_serialize_arbitrary_for_logging({"Err": err}, max_elements, indent + "  ")
        case _:
            pass

    if isinstance(data, BaseModel):
        data = data.model_dump()
    if dataclasses.is_dataclass(data):
        data = dataclasses.asdict(data)
    if isinstance(data, dict):
        keys = list(data.keys())
        result = []
        result.append("{")
        for key in keys[:max_elements]:
            result.append(
                f'{indent}  {repr(key)}: {safe_serialize_arbitrary_for_logging(data[key], max_elements, indent + "  ")},'
            )
        if len(keys) > max_elements:
            result.append(f"{indent}  ...,")
        result.append(f"{indent}" + "}")
        return "\n".join(result)
    elif isinstance(data, list):
        result = []
        result.append("[")
        for item in data[:max_elements]:
            result.append(
                f'{indent}  {safe_serialize_arbitrary_for_logging(item, max_elements, indent + "  ")},'
            )
        if len(data) > max_elements:
            result.append(f"{indent}  ...,")
        result.append(f"{indent}" + "]")
        return "\n".join(result)
    elif isinstance(data, str):
        return repr(data[:max_elements] + ("..." if len(data) > max_elements else ""))
    elif data is None or isinstance(data, (int, float, bool)):
        return repr(data)
    else:
        return f"<<non-serializable: {type(data).__qualname__}>>"


def test_cases_simple():
    # Test with an integer
    test_case(123)

    # Test with a float
    test_case(123.456)

    # Test with a string
    test_case("abcdefghijklmnopqrstuvwxyz")

    # Test with a boolean True value
    test_case(True)

    # Test with a boolean False value
    test_case(False)

    # Test with None
    test_case(None)

    # Test with a list of integers
    test_case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    # Test with a dictionary
    dict_test = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
    }
    test_case(dict_test)

    # Test with a nested list
    test_case([1, [2, [3, 4], 5], 6])

    # Test with a nested dictionary
    dict_nested = {"a": {"b": {"c": {"d": {"e": 5}}}}}
    test_case(dict_nested)

    # Test with a mixed dictionary
    dict_mixed = {"a": 1, "b": [1, 2, 3], "c": {"x": 10, "y": 20}, "d": "hello"}
    test_case(dict_mixed)

    # Test with a non-serializable object
    non_serial_object = (1, 2, 3, [4, 5, 6], {"a": 10, "b": 20})
    test_case(non_serial_object)


async def main():
    # test_cases_simple()

    test_case(data_class_object)  # test with dataclasses.dataclass object
    test_case(pydantic_object)  # test with pydantic.BaseModel object, converted to dict

    # Test case with Ok
    ok_nested = Ok({"a": {"b": {"c": {"d": {"e": 5}}}}})
    test_case(ok_nested)

    # Test case with Err
    err_nested = Err({"a": {"b": {"c": {"d": {"e": 5}}}}})
    test_case(err_nested)


if __name__ == "__main__":
    asyncio.run(main())
