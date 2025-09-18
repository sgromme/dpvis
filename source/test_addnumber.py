# import sys
# import os
# sys.path.insert(0, os.path.dirname(__file__))


from  addnumbers1_to_n import addnumbers1_to_n_recursive, addnumbers1_to_n_dynamic, addnumbers1_to_n_dynamic_andrey


def test_addnumbers1_to_n_r1():
    assert addnumbers1_to_n_recursive(5) == 15
def test_addnumbers1_to_n_d1():
    assert addnumbers1_to_n_dynamic(5) == 15
def test_addnumbers1_to_n_da1():
    assert addnumbers1_to_n_dynamic_andrey(5) == 15
def test_addnumbers1_to_n_edge_cases_recursive():
    assert addnumbers1_to_n_recursive(0) == 0
def test_addnumbers1_to_n_edge_cases_dynamic():
    assert addnumbers1_to_n_dynamic(0) == 0
def test_addnumbers1_to_n_edge_cases_dynamic_andrey():
    assert addnumbers1_to_n_dynamic_andrey(0) == 0
def test_addnumbers1_to_n_negative_recursive():
    assert addnumbers1_to_n_recursive(-5) == 0
def test_addnumbers1_to_n_negative_dynamic():
    assert addnumbers1_to_n_dynamic(-5) == 0
def test_addnumbers1_to_n_negative_dynamic_andrey():
    assert addnumbers1_to_n_dynamic_andrey(-5) == 0

    

