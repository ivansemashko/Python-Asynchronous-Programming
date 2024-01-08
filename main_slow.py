import requests
import time

start_time = time.time()

for i in range(1, 151):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(i)
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])
end_time = time.time()
print('Execution in seconds: ', int(end_time - start_time))
# Execution in seconds:  138
