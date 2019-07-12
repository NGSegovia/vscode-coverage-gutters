"""testing coverage"""
from bar.a import func
from foo.a import identity


#def test_answer():
#    """test adding"""
#    assert func(4) == identity(5)

def test_fun():
    assert func(4) == 5

def test_identity():
    assert identity(5) == 5
