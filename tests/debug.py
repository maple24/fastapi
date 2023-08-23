from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


print(ModelName.alexnet.name, ModelName.alexnet.value)
for name in ModelName:
    print(name.value, "-", name)
