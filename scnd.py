import json
import csv

with open("snms.json", encoding="UTF-8") as d:
    data = json.load(d)

with open("result.csv", mode="w") as file:
    writer = csv.DictWriter(
        file, fieldnames=list(data[0].keys()),
        delimiter=',')
    writer.writeheader()
    data.sort(key=lambda sl: sl["name"][0])
    print(data)
    for d in data:
        writer.writerow(d)
    # for index, row in enumerate(reader):
    #     if index > 10:
    #         break
    #     print(row)
