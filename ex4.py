import json

x = {"name":"John", "age":30, "city":"New York"}

y = json.dumps(x, indent=4, sort_keys=True, separators=('.', '='))

print(y)

#for k, y in y.items():
#	print(k,':\t',y,)