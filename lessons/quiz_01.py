original: dict[str, str] = {"marc": "yellow", "kris": "blue", "ezri": "blue", "john": "green", "steve": "yellow"}
new_list: list[str] = list()
new_key: str = ""
for key in original:
    new_key = original[key]
    new_list.append(new_key)
new_dict = {}
for item in new_list:
    if item in new_dict:
        new_dict[item] += 1
    else:
        new_dict[item] = 1
value_list: list[int] = list()
value: int = 0
for key in new_dict:
    value = new_dict[key]
    value_list.append(value)
last_list: list[str] = list()
for key in new_dict:
    if new_dict[key] >= max(value_list):
        last_list.append(key)
last_str: str = last_list[0]
print(last_str)