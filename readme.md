# Coffee Shop Backend
 - [https://capstone-udacity-flask.herokuapp.com/](https://capstone-udacity-flask.herokuapp.com/)

## Getting Started

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:movies`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`
    - `get:movies`
    - `post:movies`
    - `patch:movies`
    - `delete:movies`
6. Create new roles for:
    - Casting Assistant
        - can   - `get:actors`
                - `get:movies`
    - Casting Director
        - can   - `get:actors`
                - `post:actors`
                - `patch:actors`
                - `get:movies`
    - Executive Producer
        - can   - `get:actors`
                - `get:movies`
                - `post:actors`
                - `patch:actors`
                - `post:movies`
                - `delete:movies`
                - `patch:movies`
                - `delete:actors`
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users and assign them the three roles 
            User 1 - Casting Assistant
            User 2 - Casting Director
            User 3 - Executive Producer
    - Sign into each account and make note of the JWT.
    ```
        GET https://YOUR_DOMAIN/authorize?
            audience=YOUR_AUDIENCE&
            response_type=token&
            client_id=YOUR_CLIENT_ID&
            redirect_uri=https://callbackurl&

    ```
    - Import the postman collection ``
    - Right-clicking the collection folder for Casting Assistant, Casting Director, and Executive Producer
    - Navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).

### Create Database
```
    $ sudo su postgres
    $ psql`
    postgres=# CREATE DATABASE capstone;
    postgres=# CREATE DATABASE capstone_test;`
    postgres=# \q
    $ exit

```
## Start Project locally

Make sure you `cd` into the correct folder (with all app files) before following the setup steps.
Also, you need the latest version of [Python 3](https://www.python.org/downloads/)
and [postgres](https://www.postgresql.org/download/) installed on your machine.

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```bash
  $ virtualenv --no-site-packages env_capstone
  $ source env_capstone/scripts/activate
  ```

2. Install the dependencies:
```bash
$ pip install -r requirements.txt
```

Running this project locally means that it can´t access `Herokus` env variables.
To fix this, you need to edit a few informations in `config.py`, so it can
correctly connect to a local database

3. Change database config so it can connect to your local postgres database
- Open `config.py` with your editor of choice. 
- Here you can see this dict:
 ```python
database_setup = {
    "database_name_production" : "agency",
    "user_name" : "postgres", # default postgres user name
    "password" : "testpassword123", # if applicable. If no password, just type in None
    "port" : "localhost:5432" # default postgres port
}
```

 - Just change `user_name`, `password` and `port` to whatever you choose while installing postgres.
>_tip_: `user_name` usually defaults to `postgres` and `port` always defaults to `localhost:5432` while installing postgres, most of the time you just need to change the `password`.

4. Setup Auth0
If you only want to test the API (i.e. Project Reviewer), you can
simply take the existing bearer tokens in `config.py` or just export the postman collection and run it

If you already know your way around `Auth0`, just insert your data 
into `config.py` => auth0_config.

FYI: Here are the steps I followed to enable [authentitication](#authentitication).

5. Run the development server:
  ```bash 
  $ python app.py
  ```

6. (optional) To execute tests, run
```bash 
$ python test_app.py
```
If you choose to run all tests, it should give this response if everything went fine:

Endpoints

GET '/actors'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Parameters: None
- Returns: A list of categories with its type as values and a success value which indicates status of response.

```json5
{
  "actors": [
    {
      "age": 25,
      "gender": "Male",
      "id": 1,
      "name": "Meesi"
    }
  ],
  "success": true
}

```

GET '/movies'
- Fetches Paginated movies
- Request Parameters: None
- Returns 

```json5
{
  "movies": [
    {
      "id": 1,
      "release_date": "Sun, 16 Feb 2020 00:00:00 GMT",
      "title": "Matthew first Movie"
    }
  ],
  "success": true
}
```

DELETE '/actors<int:actor_id>'
- Delete's actor by id
- Request paramters: Requires ID to be passed in as a parameter
- Returns

```json5
{
    "deleted": 5,(where 5 is the ID of the actor)
    "success": true
}

```

DELETE '/movies<int:movies_id>'
- Delete's movie by id
- Request paramters: Requires ID to be passed in as a parameter
- Returns

```json5
{
    "deleted": 5,(where 5 is the ID of the movie)
    "success": true
}

```

POST '/actors'
- Create a new actor
- Request Parameters: actor body
- Returns

```json5
{
    "created": 5,
    "success": true
}

```


POST '/amovies'
- Create a new movie
- Request Parameters: movie body
- Returns

```json5
{
    "created": 5,
    "success": true
}
```

PATCH '/actors/1
- Edit an actor
- Request Parameters: actor ID
- Returns

```json5
{
    "actor": [
        {
            "age": 30,
            "gender": "Other",
            "id": 1,
            "name": "Test Actor"
        }
    ],
    "success": true,
    "updated": 1
}
```

PATCH '/movies/1
- Edit a movie
- Request Parameters: movie ID
- Returns

```json5
{
    "created": 1,
    "movie": [
        {
            "id": 1,
            "release_date": "Sun, 16 Feb 2020 00:00:00 GMT",
            "title": "Test Movie 123"
        }
    ],
    "success": true
}

```

## Errors

### Bad request (400)

```json5
{
  'success': false,
  'error': 400,
  'message': 'Bad request'
}
```

### Not found  (404)

```json5
{
  'success': false,
  'error': 404,
  'message': 'Resource Not Found'
}
```

### Unprocessable request (422)

```json5
{
  'success': false,
  'error': 422,
  'message': 'unprocessable'
}
```


### Internal server error (500)

```json5
{
  'success': false,
  'error': 500,
  'message': 'Internal server error'
}
```