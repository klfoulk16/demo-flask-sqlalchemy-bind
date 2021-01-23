# Demo Flask App for Flask-SQLAlchemy-Bind

This app serves a demo for the [Flask-SQLAlchemy-Bind](https://pypi.org/project/flask-sqlalchemy-bind/) package, available on pypi.

## To Use:

Download the project files and then install requirements:

```bash
pip install flask-sqlalchemy-bind
```

## What is It?

The app is a simple flask app with a single route. Said route allows a user to 'register', which sends their username and password to the attached database using the power of Flask-SQLAlchemy-Bind.

There is also a small test suite that checks that Flask-SQLAlchemy-Bind is functioning according to the specifications defined by the [SQLAlchemy documentation.](https://docs.sqlalchemy.org/en/13/orm/contextual.html)

Have fun and poke around!

## Got Questions?

I wrote an article that explains the reasoning behind the Flask-SQLAlchemy-Bind module and teaches you how to hook Flask up with SQLAlchemy on your own. It answers all of the questions I had while building this in the hope that future curious folks don't have to spend as much time in the black whole of failed google searches.

[Find the article here.](https://kellylynnfoulk.medium.com/under-the-hood-of-flask-sqlalchemy-793f7b3f11c3)