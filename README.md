# sg_api

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Proposal can be found here: https://docs.google.com/presentation/d/170FCnsX52mZM7fxc1Adb3_Mpmsk1hG5YCVu-z001C5U/edit?usp=sharing

Goals:

- Port sg_data to FastAPI
- Continuous integration
- Semantic versioning
- OpenAPI compliant documentation
- Maximum type coverage
- GraphQL compatible
- RESTful design
- Fast
- Easy to use
- Extensible

## Requirements

- Python 3.8

## One-time setup

1. Setup up a python virtual environment for the repo
2. Run `pip install fastapi uvicorn` to install fastapi and uvicorn
3. Run `pip install -r requirements.txt -r requirements.development.txt` to install additional dependencies

## Running the application for development

Run `uvicorn main:app --reload`

API endpoints should be accessible at `localhost:8000/`
Documentation is accessible at `localhost:8000/docs` or `localhost:8000/redoc`
