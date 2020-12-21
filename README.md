# appointment-service

## Table of Contents

- [appointment-service](#appointment-service)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Style](#style)
  - [Quick Start](#quick-start)
  - [API Documentation](#api-documentation)
      - [End Points](#end-points)
        - [GET /timeSlots/availability](#get-timeslotsavailability)
        - [POST /timeSlots](#post-timeslots)
        - [PUT /timeSlots](#put-timeslots)
  - [Todo](#todo)

## Requirements

- Python 3.7
- MySQL
## Style

- [PEP 8](https://www.python.org/dev/peps/pep-0008/)

## Quick Start

1. Clone the repo

```
$ git clone git@github.com:sukm/appointment-service.git
$ cd appointment-service
```

2. Initialize and activate a virtualenv:

```
$ python3.7 -m venv env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```
4. Change `SQLALCHEMY_DATABASE_URI` in the `config.py`


5. Run database migration
```
$ sh scripts/migration.sh
```

6. Run the development server:

```
$ python app.py
```

Leaving the virtual environment

```
$ deactivate
```

## API Documentation

#### End Points

| Description                                                      | Endpoint                    |       
| -----------------------------------------------------------------| ----------------------------|
| [Check availability of time slot](#get-timeslotsavailability)    | GET /timeSlots/availability |
| [Create a time slot](##post-timeslots)                           | POST /timeSlots             |
| [Update time slot to expired](#put-timeslots)                    | PUT /timeSlots              |

##### GET /timeSlots/availability

- **Method:**
  `GET`

- **Required:**

  `start_timestamp`
  `duration` 

- **Data Params**

  ```
  {
      "start_timestamp": "2020-12-19 00:00:00",
      "duration":70
  }
  ```


##### POST /timeSlots

- **Method:**
  `GET`

- **Required:**

  `start_timestamp`
  `duration`

- **Data Params**

  ```
  {
      "start_timestamp": "2020-12-19 00:00:00",
      "duration":70
  }
  ```


##### PUT /timeSlots

- **Method:**
  `PUT`

- **Required:**

  `start_timestamp`
  `duration`

- **Data Params**

  ```
  {
      "start_timestamp": "2020-12-19 00:00:00",
      "duration":70
  }
  ```
  
## Todo 
- Add User user friendly logging messages
- Add API versioning
- Handle scheduling conflict
- Move config file to object storage
