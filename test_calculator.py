from calculator import multiply, divide

def test_multiply():
    assert multiply(3, 4) == 12
    print("multiply test passed!")

def test_divide():
    assert divide(10, 2) == 5.0
    print("divide test passed!")

def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"
    print("divide by zero test passed!")
