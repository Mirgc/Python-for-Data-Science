ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

y = list(ft_tuple)
y[1] = "Spain!"
ft_tuple = tuple(y)

ft_set.add("Urduliz!")
ft_set.remove("tutu!")

ft_dict["Hello"] = "42Urduliz!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)