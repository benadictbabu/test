my_dict={
    "name":"sura",
    "age":30,
      "height" :5.5, 
      "married" :False,
        "city":"New York"
        }
print("my_dict:", my_dict)
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("Height:", my_dict["height"])
print("Married:", my_dict["married"])
print("City:", my_dict["city"])
my_dict["sex"]="Male"
print("sex:", my_dict["sex"])
my_dict.pop("sex")
print( my_dict)
my_dict["age"] = 31
print("Age:", my_dict["age"])