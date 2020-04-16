import pytest
from student_db import student_db
@pytest.fixture

def db():
    print("This setup in conftest file")
    db = student_db()
    db.connect("data.json")
    yield db
    print("---- closing all connections-------")
    db.close_connections()