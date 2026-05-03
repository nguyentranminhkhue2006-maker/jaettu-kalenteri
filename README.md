# shared-event-platform

## Application's features
* Users can create an account and log in to the application.
* Users can create events and act as the host of those events.
* Users can edit and delete their own events.
* Users can view events added to the application including their own and other users' events.
* Users can search for events by name, datetime, or other criteria.
* The application includes user profile pages that show statistics and events created by the user.
* Users can categorize events as work, study, leisure, networking.
* Users can comment on events created by other users.

## Installation
Clone the application:

```
$ git clone https://github.com/nguyentranminhkhue2006-maker/shared-event-platform.git
```

Create and activate the working environment:

```
$ cd shared-event-platform
$ python3 -m venv venv
$ source venv/bin/activate #Linux
$ venv/bin/activate #Mac
$ source venv/Scripts/activate #Windows
```

Install `flask`-library:

```
$ pip install flask
```

Create database tables and add initial data:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Run application:

```
$ flask run
```

## Testing the functionality of the application with a large amount of data

The seed.py file contains test code for a scenario where:
* The number of users is 1000
* The number of events is 100000
* The number of comments is 1000000
* A user_id and an event_id are selected randomly for each comment

To measure the runtime of the page requests, the following code can be added to app.py:

```
import time
from flask import g

...
@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    elapsed_time = round(time.time() - g.start_time, 2)
    print("elapsed time:", elapsed_time, "s")
    return response
```

After that, run these commands in the terminal:

```
$ python seed.py
$ flask run
```

When accessing the website, approximately 10000 pages should be available. The following results were observed when navigating between pages:

```
elapsed time: 0.05 s
127.0.0.1 - - [03/May/2026 16:44:57] "GET / HTTP/1.1" 200 -
elapsed time: 0.01 s
127.0.0.1 - - [03/May/2026 16:44:57] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.04 s
127.0.0.1 - - [03/May/2026 16:45:01] "GET /2 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 16:45:01] "GET /static/main.css HTTP/1.1" 304 -
elapsed time: 0.04 s
127.0.0.1 - - [03/May/2026 16:45:02] "GET /3 HTTP/1.1" 200 -
elapsed time: 0.0 s
127.0.0.1 - - [03/May/2026 16:45:02] "GET /static/main.css HTTP/1.1" 304 -
```

Under these conditions, with thousands of users and large numbers of events and comments, the application runs with an approximate response time of 0.00-0.05 seconds.
