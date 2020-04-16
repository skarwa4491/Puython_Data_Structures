from student_db import student_db
import pytest

db= None
def setup_module(module):
    print("-----------setup---------------")
    global db
    db = student_db()
    db.connect("data.json")

def test_scott_data():
    print("-----------scott---------------")
    scott_data = db.get_Data("scott")
    assert scott_data['id']==1
    assert scott_data["name"]== "scott"

def test_mark_data():
    print("-----------mark---------------")
    mark_data=db.get_Data("Mark")
    assert mark_data['id'] == 2
    assert mark_data["name"]== "Mark"

def teardown_module(module):
    print("-----------tear down---------------")
    db.close_connections()

