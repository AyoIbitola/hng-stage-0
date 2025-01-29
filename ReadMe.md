## HNG-stage-0

This is a  FastAPI project that provides a single endpoint to retrieve user information.

## Requirements

To install the required dependencies, run:


```sh
pip install -r requirements.txt
```

## How to Run

To start the FastAPI server, run:

```sh
uvicorn main:app --reload
```

## Endpoints
GET /
Returns user information including email, current datetime in UTC, and GitHub URL.

## Endpoint URL

```sh
   https://hng-stage-0-production-5e52.up.railway.app/

```

Example response:

```sh
{
    "email": "mremmatola@gmail.com",
    "current_datetime": "2023-10-05T14:48:00Z",
    "github_url": "https://github.com/AyoIbitola/hng-stage-0"
}
```

## backlink
[https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)