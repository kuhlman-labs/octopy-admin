import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from octopy.graph_query import GraphQueryProvider, GraphQueryError
from dotenv import load_dotenv
load_dotenv()


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
