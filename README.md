# Data Processor

## Description

This project is a Django-based web application designed to manage and track data from Excel files. The application processes data by importing it from Excel files into a database. It also provides APIs for accessing and viewing the processed data, enabling users to efficiently interact with and utilize the information extracted from the files.

## Features

- Import data from Excel files into a database.
- Access processed data via APIs.
- Robust data validation and error handling.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/gishwinantony/data-processor.git
    ```

2. Navigate to the project directory:
    ```bash
    cd data-processor
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations to set up the database:
    ```bash
    python3 manage.py migrate
    ```

6. Run the development server:
    ```bash
    python3 main.py
    ```

7. Open your browser and go to `http://localhost:8080` to access the application.


## Acknowledgements

Special thanks to the Django community for their invaluable support and resources.
