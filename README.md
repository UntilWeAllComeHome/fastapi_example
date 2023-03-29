# fastapi_example
Simple example of a FastAPI app.

# Setup
Setup your environment using pyenv.

Install Python:

    pyenv install 3.11.1

Create a new pyenv environment:

    pyenv virtualenv 3.11.1 fastapi_example

Activate the new environment:

    pyenv activate fastapi_example

Install the required modules:

    pip install -r requirements.txt

Run the application

    uvicorn main:app --reload