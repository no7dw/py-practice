class Map(dict):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.__dict__ = self

struct = Map(field1='foo', field2='bar', field3=42)
print(struct.field1)
print(struct.field2)
print(struct.field3)
