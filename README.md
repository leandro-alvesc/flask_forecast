# Flask Forecast

> Flask API to consume forecast and save data.

## 🧬 Built with

* Python 3.9
* Flask
* SQLite

## 💻 Requirements

Before you start, make sure you have the following resources:

* Python 3.9
* SQLite
* A virtual environment to run the application
* A SQLite database
* Docker and Docker Compose

You can run it manually or with Docker.

## 🚀 Setting up to run manually

Run the following commands:

- Creating virtual environment
```
python3.9 -m venv env
```

- Install dependencies:
```
pip install -r requirements.txt
```

- Create a .env file with your settings, e.g.:
```
FLASK_ENV=development
CLIMA_TEMPO_TOKEN=<your-climatempo-token>
```

- Migration commands:
```
flask db init
flask db migrate
flask db upgrade
```

## 🗃 Initializing manually

To run the API, run the command:

```
flask run
```

## 🐳 Docker

- Create a .env file with your Clima Tempo Token::
```
CLIMA_TEMPO_TOKEN=<your-climatempo-token>
```

- Build Docker:
```
docker-compose build
```

- Run Docker:
```
docker-compose up
```

## 🛴 API

Check the API reference [here](API.md).
