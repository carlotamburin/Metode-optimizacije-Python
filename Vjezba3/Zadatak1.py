import json

f = open('08_IO_datoteke.ipynb', encoding='utf-8')
reader = json.load(f)
# print(reader)

f2 = open("09_iznimke.ipynb", encoding="utf-8")
reader2 = json.load(f2)

result_dict = {}
dicts = [reader, reader2]

for d in dicts:
    for k, v in d.items():
        try:
            result_dict.setdefault(k, []).extend(v)
        except TypeError:
            result_dict[k].append(v)

with open('output.ipynb', 'w') as f:
    writer = json.dump(result_dict, f)

print(result_dict)


f.close
f2.close
