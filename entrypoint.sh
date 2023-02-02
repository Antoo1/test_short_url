#!/bin/bash

exec gunicorn asgi:app -n short_url -k uvicorn.workers.UvicornWorker -b 0.0.0.0:5000 --log-level=info
