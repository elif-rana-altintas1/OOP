
#!creat-read-update-delete(CRUID)
# ?Cetegory objesi için CRUID yapacağız 
# from uuid import uuid4
# from pprint import pprint

# categories = {
#     "dacfb6c5-f1a9-4180-b6d6-a7a05983b90e":{
#         " name":"boxing gloves",
#         "description":"boxing gloves"
#     }
# }
# print(uuid4())

#*kategori nesnesini temsil edecek bir kategory sınıfı yaratalım

# class Category:
#     def __init__(self, name:str,description:str) :
#         self.name=name
#         self.description=description
#         self.id =str(uuid4())

# class Category_service:
#     def create(self,category_obj:Category):
#         categories[category_obj.id]={
#             "category name":category_obj.name,
#             "description":category_obj.description
#         }
        
#         print(f"{category_obj.name} has been created..!")
#         pprint(categories)

#     def get_all(self):
#         pprint(categories)
#     def get_by_id(self,id:str)->dict:
#         for key in categories.keys():
#             if key.__eq__(id):
#                 return categories.get(key)
        
#     def update(self,id:str,name:str,description:str):
#         current_category=self.get_by_id(id=id)

#         current_category.update((
#             "name":name,
#             "description":description
#         ))
#         print(f"{id} category has been editied..!")
#         pprint(categories)
        
#     def delete(self):
#         current_category=self.get_by_id(id=id)

#         if current_category is not None 
#             del categories[id]

#             print(f"{id} category has been removed")

#         else:
#             print("there is no such a category") 
        

# def main():
#     service=Category_service()

#     while True:
#         process=input("type process name:")

#         match process:
#             case"create":
#                 category=Category(name="UFC Gloves", description="UFC Gloves")
#                 service.create(category_obj=category)

#             case "get by id":
#                 result=service.get_by_id(
#                    id=input("please type a id:")
#                )     
#                 pprint(result)

#             case "get all":
#                 service.get_all()

#             case "update" :
#                 service.update(
#                     id=input("please type a id:"),
#                     name=input("name:"),
#                     description=input("description")
#                 )
#             case "delete": 
#                 service.delete(
#                     id=input("please type a id :")
#                 )

#             case _:
#                 print("please type a valid process name..!")


# main()  


