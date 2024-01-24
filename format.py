import json
with open("HellHub.json", "r") as f:
    data_json = json.loads(f.read())

data_final = '{'

for instance in data_json:
    key = instance['player_name']
    value = instance['last_ip']
    
    if value != None:
        data_final = data_final + f'    "{key}": "{value}", \n'
        # print(value)
    else:
        continue
data_final = data_final + '}'
print(data_final)
with open("HellHub.json", "w") as f:
    f.write(data_final)
