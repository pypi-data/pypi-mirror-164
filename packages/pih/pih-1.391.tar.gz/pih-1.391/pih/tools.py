from dataclasses import dataclass
import re
import string
import random
import json
import os
import sys
from typing import Any, List, Tuple
#import subprocess

# sys.path.append("//pih/facade")
from pih.const import PASSWORD_GENERATION_ORDER
from pih.collection import FieldItem, FieldItemList, FullName, LoginPasswordPair


class DataTools:

    @staticmethod
    def represent(data: FieldItemList) -> str:
        return json.dumps(data, cls=PIHEncoder)

    @staticmethod
    def rpc_represent(data: dict) -> str:
        return json.dumps(data, cls=PIHEncoder) if data is not None else ""

    @staticmethod
    def rpc_unrepresent(value: str) -> dict:
        return json.loads(value) if value is not None and value != "" else {}

    @staticmethod
    def unrepresent(value: str) -> dict:
        object: dict = json.loads(value)
        fields = object["fields"]
        data = object["data"]
        field_list: List = []
        for field_item in fields:
            for field_name in field_item:
                field_item_data = field_item[field_name]
                field_list.append(FieldItem(field_item_data["name"], field_item_data["caption"], bool(
                    field_item_data["visible"])))
        return ResultPack.pack(FieldItemList(field_list), data)

    @staticmethod
    def to_string(obj: object, join_symbol: str = "") -> str:
        return join_symbol.join(obj.__dict__.values())

    @staticmethod
    def to_data(obj: object) -> dict:
        return obj.__dict__

    @staticmethod
    def from_data(dest: object, source: dict) -> object:
        for item in dest.__dataclass_fields__:
            if item in source:
                dest.__setattr__(item, source[item])
        return dest

    @staticmethod
    def get_first(value: List, default_value: Any = None) -> Any:
        return value[0] if value is not None and len(value) > 0 else default_value


class ParameterList:

    def __init__(self, list: Any):
        self.list = list if isinstance(
            list, List) or isinstance(self, Tuple) else [list]
        self.index = 0

    def next(self, object: Any = None) -> Any:
        value = self.list[self.index]
        self.index = self.index + 1
        if object is not None:
            value = DataTools.from_data(object, value)
        return value


@dataclass
class Result:
    fileds: FieldItemList
    data: dict


class ResultPack:

    @staticmethod
    def pack(fields: FieldItemList, data: dict) -> dict:
        return {"fields": fields, "data": data}


class ResultUnpack:

    @staticmethod
    def unpack(result: dict) -> Tuple[FieldItemList, Any]:
        return ResultUnpack.unpack_fields(result), ResultUnpack.unpack_data(result)

    @staticmethod
    def unpack_fields(result: dict) -> Any:
        return result["fields"]

    @staticmethod
    def unpack_data(result: dict) -> Any:
        return result["data"]

    @staticmethod
    def unpack_first_data(result: dict) -> Any:
        return DataTools.get_first(ResultUnpack.unpack_data(result))

    @staticmethod
    def data_is_empty(result: dict) -> bool:
        return result is None or len(ResultUnpack.unpack_data(result)) == 0


class PathTools:

    @staticmethod
    def get_current_full_path(file_name: str) -> str:
        return os.path.join(sys.path[0], file_name)


class PIHEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, FieldItem):
            return {f"{obj.name}": obj.__dict__}
        if isinstance(obj, FieldItemList):
            return obj.list
        if isinstance(obj, FullName) or isinstance(obj, LoginPasswordPair):
            return DataTools.to_data(obj)
        return json.JSONEncoder.default(self, obj)


class FullNameTool():

    @staticmethod
    def to_string(full_name: FullName, join_symbol: str = " ") -> str:
        return DataTools.to_string(full_name, join_symbol)

    @staticmethod
    def to_given_name_string(full_name: FullName, join_symbol: str = " ") -> str:
        return join_symbol.join([full_name.first_name, full_name.middle_name])

    @staticmethod
    def from_string(value: str, split_symbol: str = " ") -> FullName:
        full_name_string_list: List[str] = value.split(split_symbol)
        return FullName(full_name_string_list[0], full_name_string_list[1], full_name_string_list[2])

    def is_equal(a: FullName, b: FullName) -> bool:
        return a.first_name == b.first_name and a.middle_name == b.middle_name and a.last_name == b.last_name

class Clipboard:

    @staticmethod
    def copy(value: str):
        import pyperclip as pc
        pc.copy(value)

    '''
    @staticmethod
    def copy(value: str):
        cmd = 'echo '+value.strip()+'|clip'
        return subprocess.check_call(cmd, shell=True)
    '''


class PasswordTools:

    @staticmethod
    def check_password(value: str, length: int, special_characters: str) -> bool:
        regexp_string = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[" + special_characters + \
            "])[A-Za-z\d" + special_characters + "]{" + str(length) + ",}$"
        password_checker = re.compile(regexp_string)
        return re.fullmatch(password_checker, value) is not None

    @staticmethod
    def generate_random_password(length: int, special_characters: str, order_list: List[str], special_characters_count: int, alphabets_lowercase_count: int, alphabets_uppercase_count: int, digits_count: int, shuffled: bool):
        # characters to generate password from
        alphabets_lowercase = list(string.ascii_lowercase)
        alphabets_uppercase = list(string.ascii_uppercase)
        digits = list(string.digits)
        characters = list(string.ascii_letters +
                          string.digits + special_characters)
        characters_count = alphabets_lowercase_count + \
            alphabets_uppercase_count + digits_count + special_characters_count
        # check the total length with characters sum count
        # print not valid if the sum is greater than length
        if characters_count > length:
            print("Characters total count is greater than the password length")
            return
        # initializing the password
        password: List[str] = []
        for order_item in order_list:
            if order_item == PASSWORD_GENERATION_ORDER.SPECIAL_CHARACTER:
             # picking random alphabets
                for i in range(special_characters_count):
                    password.append(random.choice(special_characters))
            elif order_item == PASSWORD_GENERATION_ORDER.LOWERCASE_ALPHABET:
                # picking random lowercase alphabets
                for i in range(alphabets_lowercase_count):
                    password.append(random.choice(alphabets_lowercase))
            elif order_item == PASSWORD_GENERATION_ORDER.UPPERCASE_ALPHABET:
                # picking random lowercase alphabets
                for i in range(alphabets_uppercase_count):
                    password.append(random.choice(alphabets_uppercase))
            elif order_item == PASSWORD_GENERATION_ORDER.DIGIT:
                # picking random digits
                for i in range(digits_count):
                    password.append(random.choice(digits))
        # if the total characters count is less than the password length
        # add random characters to make it equal to the length
        if characters_count < length:
            random.shuffle(characters)
            for i in range(length - characters_count):
                password.append(random.choice(characters))
        # shuffling the resultant password
        if shuffled:
            random.shuffle(password)
        # converting the list to string
        # printing the list
        return "".join(password)
