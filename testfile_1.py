from dataclasses import dataclass, astuple, asdict, field
from dataclasses_json import config, dataclass_json
import inspect
import pprint
import random
from typing import Dict, List, Optional


def random_num():
    return random.randrange(100, 100000)


@dataclass
class Person:
    name: str
    age: int
    place: Optional[str] = field(metadata=config(field_name="Placing"), default=None)
    is_active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id_num: int = field(init=False, default_factory=random_num)


class Person_2:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"name:{self.name}, age: {self.age}"

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"


def main() -> None:
    person = Person(name="test", age=21, email_addresses=["abcd@gmail.com", "xyz@yahoo.com"], place="BGL")
    print(person)


def main_1() -> None:
    person_2 = Person_2("TEST_2", 22)
    print(person_2)
    pprint.pprint(inspect.getmembers(person_2))


if __name__ == "__main__":
    main()
    # main_1()
