# Tutorial for FASTapi

## Install

```sh
pip install 'fastapi[all]'
```

## Clone module

```sh
git clone --recursive https://github.com/maple24/fastapi.git/
```

For already cloned repos, use:

```sh
cd CRQM
git submodule update --init --recursive
```

## Quick Start

```sh
uvicorn main:app --reload
```


## CORS
```sh
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

tip: localhost and 127.0.0.1 are different origins


## middleware
> A "middleware" is a function that works with every request before it is processed by any specific path operation. And also with every response before returning it.

tip: middleware functions just like axios intercepetions