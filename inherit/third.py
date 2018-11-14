import base 

class third(base.BaseModel):
    def test(self):
        print("third.test")

print(third().test())