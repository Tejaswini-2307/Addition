from AddTwoNumbers import add

# def test_add1():
#     print("Addition of 2 and 3 =", add(2, 3))
#     assert add(2, 3) == 5

# def test_add2():
#     print("Addition of 10 and 20 =", add(10, 20))
#     assert add(10, 20) == 30

# def test_add3():
#     print("Addition of 0 and 0 =", add(0, 0))
#     assert add(0, 0) == 0

from AddTwoNumbers import add

def test_add():
    print("2 + 3 =", add(2, 3))
    print("10 + 20 =", add(10, 20))
    print("0 + 0 =", add(0, 0))

    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(0, 0) == 0



