import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get('/')
async def home():
    return "Redirect is Live Baby!"


@app.get('/r/{url}')
async def redirect(url: str):
    # eventually have this 'bot test' and collect device data @ todo
    return RedirectResponse('https://' + url)


if __name__ == "__main__":
    uvicorn.run("server.api:app", debug=True, port=10_000)