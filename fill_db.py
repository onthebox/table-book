""" Fill the databse with test data."""
import os
import pathlib

import psycopg2

PARAMS = {
    'database': 'test_db',
    'user': 'test_user',
    'password': 'test_password',
    'host': '127.0.0.1',
    'port': '8080',
}

