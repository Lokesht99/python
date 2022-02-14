# import json
# class Base:
#     def openfile(self):
#         self.fname=open("data.json","r+")
# class Derived(Base):
#     def read(self):
#         self.data=json.load(self.fname)
#     def write(self,content):
#         self.data["employee"].append(content)
#         self.fname.seek(0)
#         json.dump(self.data,self.fname,indent=4)
# content={
#     "id":9,
#     "name":"alok",
#     "department":"ceo"
# }
# d=Derived()
# d.openfile()
# d.read()
# d.write(content)
# --------------------------------------------------



