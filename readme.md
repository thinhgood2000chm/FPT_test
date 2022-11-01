
<div align="center"><br />
<p align="center" style="width: 100%">

<h3 align="center">FPT TEST</h3>
</p>
</div>

## I. Requirements:
    - python >= 3.8.10
    - mysql

## II. Setup environment:
- How to set up environment:
  1. Setup Python virtual environment:

        For Linux:
        ```sh
        cd testFPT
        virtualenv env -p python3
        source env/bin/activate
        pip install -r requirements.txt
        ```

        For Windows:
        ```powershell
        cd testFPT
        virtualenv --python C:\Path\To\Python\python.exe venv
        .\venv\Scripts\activate
        pip install -r requirement.txt
        ```
     
        Note: some packed on Linux is difference from windows,  

    2. Copy data of `.env.example` to `.env` and config (system uses local database) 
    3. Run
        - For local development: type command `python manage.py runserver <host>:<port>`
            ```sh
            python manage.py runserver 127.0.0.1:8000
            ```

    4. Documentation
        - Redoc: `http://127.0.0.1:8000/api/v1/redoc/`
