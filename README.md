
# Weekly Evaluation Task for Interns

A web application that fetches data from a Weather API, processes this data, stores it in a database, and displays it through a Django backend and React frontend.

## Prerequisites

- Python 3.x
- Django 3.x or later
- pip (Python package installer)
- Node.js (v14.18.0 or later)
- npm (v6.14.15 or later) or yarn (v1.22.0 or later)

## Installation

Clone the repository

```bash
    git clone https://github.com/AryaShakya1/Intern-Task.git
    cd Intern-Task
```


### Backend Installation

Create a virtual environment

```bash
    cd backend
    python -m venv env
```

Activate the virtual environment

```bash
  .\env\Scripts\activate  # On Linux use source env/bin/activate
```

Install the required packages
```bash
    pip install -r requirements.txt
```
#### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Create a .env file in the root directory of the project and add the following environment variables:

```
WEATHER_API_KEY=your_api_key
POSTGRES_DB=database_name
POSTGRES_USER=db_user_name
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db_host
POSTGRES_PORT=db_port
```

Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the Development Server:
```bash
python manage.py runserver
```

The application can be accessed at http://localhost:8000/

### Frontend Installation

Navigate to the folder

```bash
cd frontend
```

Install the dependencies

```bash
npm install
```

Run the application server

```bash
npm run dev
```
The application can be accessed at http://localhost:5173/
