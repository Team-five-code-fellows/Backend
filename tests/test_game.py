import pytest
from app.game import mocker

def test_quit():
    with open("tests/open_quit.txt", 'r') as f:
        responses = ['q']
        actual = mocker(responses)
        expected = ''
        for line in f.readlines():
            expected += line
    assert actual == expected

# @pytest.mark.skip
def test_manual_same_path_win():
    with open("tests/manual_same_path_win.txt", 'r') as f:
        responses = ['p', 'h', 'm', 'chocolate', 'chocolate', 'q']
        actual = mocker(responses)
        expected = ''
        for line in f.readlines():
            expected += line
    assert actual == expected

# @pytest.mark.skip
def test_manual_different_path_win():
    with open("tests/manual_different_path_win.txt", 'r') as f:
        responses = ['p', 'm', 'm', 'tea', 'coffee', ' ', '503', 'q']
        actual = mocker(responses)
        expected = ''
        for line in f.readlines():
            expected += line
    assert actual == expected

@pytest.mark.skip
def test_manual_loss():
    with open("tests/open_quit.txt", 'r') as f:
        responses = ['q']
        actual = mocker(responses)
        expected = ''
        for line in f.readlines():
            expected += line
    assert actual == expected