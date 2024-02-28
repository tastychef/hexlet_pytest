def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'
