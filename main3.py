from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

app = FastAPI()


@app.get('/')
def main():
    return FileResponse('public/index.html')


@app.post('/translate')
def translate(data=Body()):
    value = data['value']
    language = data['language']
    value = str(value)
    value = value.lower()
    world = ''
    with open('values.txt', 'r', encoding='UTF-8') as file:
        for i in file:
            world += i
    world = world.lower()
    world = world.replace('-', ' ')
    world = world.split()
    if value in world and language == 'en':
        result = world[world.index(value) + 1]
        return {'message': result}
    elif value in world and language == 'ru':
        result = world[world.index(value) - 1]
        return {'message': result}
    else:
        return {'message': 'not found'}
