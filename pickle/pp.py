import pickle
obj = {"id":1, "name":"wade", "age":30, "job_desc":{"addr":"China", "job_title":"SE" }}
pickle.dump(obj, open("wade.pickle","wb+"))

r_obj = pickle.load(open("wade.pickle", "rb"))
print(r_obj)
print(r_obj["id"], r_obj["age"], r_obj["job_desc"]["job_title"])
