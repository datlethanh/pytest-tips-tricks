from hello import more_hello, more_goodbye


def test_more_hello():
    assert "Hi" == more_hello()


def test_more_goodbye():
    assert "Bye" == more_goodbye()


# This is nonsense code that generates a warning
# var = 1
# var = var

# Bad syntax
# foo = bar
