def all_thing_is_obj(obj):
    if isinstance(obj, str):
        print(obj, "is in the kitchen :", type(obj))
    elif isinstance(obj, int):
        print("Type not found")
        return (42)
    else:
        data_type_name = type(obj).__name__
        print(f"{data_type_name.capitalize()}", ":", type(obj))
