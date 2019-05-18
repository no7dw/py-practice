def gen_fun():
    for i in range(10):
        i
#        yield i

for item in gen_fun():
    print(item)
