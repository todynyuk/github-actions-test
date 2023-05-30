import requests


def test_web():
    r = requests.get('https://solvdinternal.zebrunner.com')
    assert 200 == r.status_code
