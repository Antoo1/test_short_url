import uvicorn
from fastapi import FastAPI
from short_url.app.fast_api import create_app

app: FastAPI = create_app()

if __name__ == '__main__':
    uvicorn.run('asgi:app', host='127.0.0.1', port=5000, log_level='debug', reload=True)
