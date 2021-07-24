"""
Thanks to @ludeeus for this script.
"""
import json
import os
import re
from datetime import datetime
from time import sleep

DATE = datetime.now()

OUT = """\"\"\"
Class object for {classname}
Documentation: {documentation}
\"\"\"
from .base import BridgeBase

{inherit}
"""

CLASS = """
class {classname}(BridgeBase):
{properties}
"""

PROP = """
    @property
    def {key}(self):
        return self.attributes.get("{key}", {default})
"""
PROPCLASS = """
    @property
    def {key}(self):
        return {name}(self.attributes.get("{key}", {default}))
"""
PROPLISTCLASS = """
    @property
    def {key}(self):
        return [{name}(x) for x in self.attributes.get("{key}", [])]
"""

INHERIT = []


def get_input():
    with open("generator/input.json", "r") as inputdata:
        return json.loads(inputdata.read())


def generateclass(name, data, primary=False):
    properties = []
    for key in data:
        if key.startswith("_"):
            continue
        if isinstance(data[key], list):
            if not isinstance(data[key][0], dict) and not isinstance(
                data[key][0], list
            ):
                properties.append(PROP.format(key=key, default=[]))
                continue
            _name = key.split("_")
            _name = "".join([x.title() for x in _name])
            _name = f"{_name}"
            INHERIT.append(generateclass(_name, data[key][0]))
            properties.append(PROPLISTCLASS.format(name=_name, key=key))
            continue
        if isinstance(data[key], dict):
            _name = key.split("_")
            _name = "".join([x.title() for x in _name])
            _name = f"{name}{_name}"
            INHERIT.append(generateclass(_name, data[key]))
            properties.append(PROPCLASS.format(name=_name, key=key, default={}))
            continue
        if isinstance(data[key], bool):
            properties.append(PROP.format(key=key, default=data[key]))
            continue
        if isinstance(data[key], str):
            properties.append(PROP.format(key=key, default='""'))
            continue
        properties.append(PROP.format(key=key, default=None))

    if not primary:
        return CLASS.format(classname=name, properties="".join(properties))
    docs = input("Documentation URL: ")
    classname = input("Main Classname: ")
    INHERIT.append(
        CLASS.format(classname=f"{classname}", properties="".join(properties))
    )

    objectfilename = f"systembridge/objects/{'/'.join([x.lower() for x in re.findall('[A-Z][a-z]*', classname)])}.py"
    if not os.path.exists(os.path.dirname(objectfilename)):
        os.makedirs(os.path.dirname(objectfilename))
        sleep(1)
        with open(os.path.join(os.path.dirname(objectfilename), "__init__.py")) as f:
            f.write()

    with open(
        objectfilename,
        "w",
    ) as objfile:
        objfile.write(
            OUT.format(
                classname=f"{classname}",
                properties=properties,
                documentation=docs,
                inherit="".join(INHERIT),
                date=DATE,
            )
        )


def add_object():
    data = get_input()
    generateclass("", data, True)


add_object()
