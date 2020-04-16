from student_db import student_db
import pytest

def test_scott_data(db):

    scott_data = db.get_Data("scott")
    assert scott_data['id']==1
    assert scott_data["name"]== "scott"
    assert 0

def test_mark_data(db):

    mark_data=db.get_Data("Mark")
    assert mark_data['id'] == 2
    assert mark_data["name"]== "Mark"
