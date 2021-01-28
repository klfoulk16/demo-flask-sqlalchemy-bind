"""Test that the correct errors show when package is not set up properly"""
import pytest
import application


def test_app_is_none(caplog):
    """Test intended behaviors occur if nothing passed into init_app()"""
    application.db.init_app()
    assert caplog.text == "ERROR    root:sqlalchemy_bind.py:58 SQLAlchemy was not set up properly.\nUsage:\nOutside app factory\n>> db = SQLAlchemy()\nInside app factory\n>> db.init_app(your_flask_app)\n"


def test_app_is_not_flask_app(caplog):
    """Test intended behaviors occur if something besides a flask app is passed into init_app()"""
    app = "random thing"
    application.db.init_app(app)
    assert caplog.text == "ERROR    root:sqlalchemy_bind.py:56 Error connecting database.\nPlease set app.config['DATABASE'] to your database connection string\n"


def test_improper_database_connection(caplog):
    """Test what behavior occurs if app database link is none or doesn't work."""
    application.create_app({
        'TESTING': True,
        'DATABASE': "",
    })
    assert caplog.text == "ERROR    root:sqlalchemy_bind.py:56 Error connecting database.\nPlease set app.config['DATABASE'] to your database connection string\n"
