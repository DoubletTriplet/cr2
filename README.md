
# Translation Service Microservice

This is a microservice built with FastAPI for providing word definitions, translations, and related information using Google Translate. The service stores data in a NoSQL database and includes authentication via API key along with request throttling.

## Features

- Get details about a given word including definitions, synonyms, translations, and examples.
- Data fetched from Google Translate is saved in the database.
- List stored words with pagination, sorting, and filtering options.
- Delete a word from the database.
- API key authentication for secure access.
- Throttling to limit the number of requests per minute per API key.

## Technologies Used

- FastAPI (async mode)
- MongoDB (NoSQL Database)
- Docker and docker-compose
- API key authentication
- Request throttling with FastAPI's SimpleRateLimiter

## Getting Started

### Prerequisites

- Python
- Docker

### Running the Microservice

1. Clone the repository

2. [OPTIONAL]Configure the environment

```env
TSC_MONGODB_USER= tsc
TSC_MONGODB_HOST= localhost
TSC_MONGODB_PASSWORD= secret
TSC_MONGODB_DATABASE= tsc_db
TSC_MONGODB_PORT= 27017
TSC_MONGODB_COLLECTION= words
TSC_DEBUG= true
```

2. Build and run the Docker containers:

```bash
make build
make start
```

3. Run Unit tests:

*NOTE* - tests are not running properly due to an incompatibility between `httpx` and `googletrans` and TestClient from `fastapi`



```bash
make test
```


The API will be accessible at http://localhost:8000.

API Documentation
API documentation is generated automatically by FastAPI. Visit http://localhost:8000/docs for Swagger documentation and http://localhost:8000/redoc for ReDoc documentation.

### Known Flaws and Possible Improvements

- Problem using `googletrans` package. I Had to copy the main Translator Logic and adapt to make it work. Found this link https://stackoverflow.com/q/52455774 that could work for a new iteration
- Due problems i've faced with `googletrans`, which uses `httpx` package, the same as the TestClient from `fastapi.testing` I am not able to run unittesting properly.
- Since I also love Devops I would like to have more time to create HelmChart for the solution and also create an automated pipeline for CICD process. At least had time to add Prometheus metrics on `/metrics` endpoint

Contributing
Feel free to contribute by opening issues or submitting pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

