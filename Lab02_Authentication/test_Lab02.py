import pytest
from Lab02 import authentication


def test_authentication():
    # incorrect username
    assert authentication(
        'John Cheese', 'None shall pass') == 'Not authenticated'

    # incorrect password
    assert authentication(
        'Black Knight', 'Tis but a scratch.') == 'Not authenticated'

    # Both incorrect
    assert authentication(
        'John Cheese', 'Tis but a scratch.') == 'Not authenticated'

    # Wrong index
    assert authentication(
        'King Arthur', 'Bring out your dead!') == 'Not authenticated'

    # Valid Black Knight
    assert authentication('Black Knight', 'None shall pass') == 'Authenticated'

    # Valid King Arthur
    assert authentication('King Arthur', 'Run away!') == 'Authenticated'

    # Valid French Soldier
    assert authentication(
        'French Soldier', 'I fart in your general direction') == 'Authenticated'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
