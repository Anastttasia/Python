import json
  
try:
    with open("data.json", "r", encoding="utf-8") as file:
        json_data = json.loads(file.read())
        print(json_data)
    output = ','.join([*json_data[0]])
    print(output)
    for obj in json_data:
        output += f'\n{obj["name"]}, {obj["age"]}, {obj["profession"]}, {obj["city"]}'
    with open("data.txt", "w") as f:
        f.write(output)
        print('OUTPUT', output)
except Exception as ex:
    print(f'Error {str(ex)}')
