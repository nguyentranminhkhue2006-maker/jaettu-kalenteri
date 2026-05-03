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

## Testing the functionality of the application with big amount of data

The seed.py shows the test code for the situation, in which:
* Number of users is a thousand
* Number of events is a hundred of thousands
* Number of comments is a million
* A user_id and an event_id are selected randomly for each comment

To test the runtime of the page requests, we can paste this prompt into the app.py:

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

And then running the seed.py -file in the terminal:

```
$ python seed.py
$ flask run
```

When accessing the website, we should see a total of 10000 pages. This is the results we got when going to the next pages:

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

Under the circumstances in which there are thousands of users and thousands of events and comments, the application still runs with the approximate time of 0-0.05s.