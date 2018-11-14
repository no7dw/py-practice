# -*- coding: UTF-8 -*-
# 定义一个dict 的情况，不想用b['a'], 而想用 b.a
# 场景： 不想用 class 定义成员变量来访问 b.a
# b = dict({'a':2})
# print(b['a'])
class Map(dict):
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.__dict__ = self

struct = Map(field1='foo', field2='bar', field3=42)
print(struct.field1)
print(struct.field2)
print(struct.field3)


class Storage(dict):
  def __getattr__(self, key):
    return self[key]
  def __setattr__(self, key, value):
    self[key] = value
  def __repr__(self):
    return '<Storage' + dict.__repr__(self) + '>'  

s = Storage({"a":2})

print(s.a)

