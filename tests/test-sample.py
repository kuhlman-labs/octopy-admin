import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from dotenv import load_dotenv

load_dotenv()


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
