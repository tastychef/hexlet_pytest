def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'


