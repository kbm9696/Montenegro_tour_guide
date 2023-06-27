import json
from api.health_tour_guides import HospitalsApis, HealthTourismApis, health_tour_spot
# from ipfs_apis import IPFS
import os
import pandas as pd

# ipfs = IPFS()
key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9' \
      '.eyJzdWIiOiJkaWQ6ZXRocjoweDZBNjU2NjE1OWMxNzFiMUFhNGJiMDYwODA3ZUE0QUQxYTEzY2ZDNkUiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY4NzYxMjcyOTUyOCwibmFtZSI6ImtibSJ9.eS4Mfts4dEzYNYIuzCHi7Ak3ADwFClYkB5pQRXnUJd0'
t = HealthTourismApis()
cites_names = t.get_health_tour_spots()
print(cites_names)

for cite in cites_names:
    pwd = os.getcwd()
    print("processing for", cite.split())
    if cite.split()[0] not in ['Spa','Herceg']:
        continue
    for i in range(1, 6):
        file_name = os.path.join('D:\Montenegro_health_tour\Tourism_spots_images', f'{cite.split()[0]}{i}.jpg')
        print(file_name)
        if not os.path.exists(file_name):
            file_name = os.path.join('D:\Montenegro_health_tour\Tourism_spots_images', f'{cite.split()[0]}{i}.jpeg')
        # res = ipfs.upload_nft_storage(key, file_name)
        # with open(health_tour_spot,'r+',)
        # print(res.get('value').get('cid'))


# data_frame = pd.read_csv('private.csv')
# data_list = data_frame.to_dict(orient='records')
# json_data = json.dumps(data_list, indent=4)
# with open('private_hospital.json', 'w') as f:
#     f.write(json_data)

# t = HospitalsApis('public')
# print(t.get_hospital_list())
