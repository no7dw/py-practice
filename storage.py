class Storage(dict):
  def __getattr__(self, key):
    return self[key]
  def __setattr__(self, key, value):
    self[key] = value
  def __repr__(self):
    return '<Storage ' + dict.__repr__(self) + '>'



#   def __getattr__(self, key):
#     return self[key]  
#  
#   def __setattr__(self, key, value):
#     self[key] = value  

#   def __repr__(self):
#     return '<Storage ' + dict.__repr__(self) + '>'  

s = Storage({"a":2})
print(s)
print(s.a)
