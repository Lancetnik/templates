from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class TestModel(Model):
    test = fields.CharField(max_length=70)

    class PydanticMeta:
        exclude = ["id"]

TestSchema = pydantic_model_creator(TestModel)