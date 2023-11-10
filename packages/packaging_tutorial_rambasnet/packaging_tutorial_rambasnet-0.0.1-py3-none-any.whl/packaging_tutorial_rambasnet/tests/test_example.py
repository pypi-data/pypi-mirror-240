"""Test example module. 
"""

import packaging_tutorial_rambasnet.example as example

def test_add_one():
    assert example.add_one(1) == 2

def test_add_one_float():
    assert example.add_one(1.1) == 2.1  

def test_add_100():
    assert example.add_one(100) == 101

    