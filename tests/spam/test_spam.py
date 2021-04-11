import pytest
from spammer.spam import spam_email

def test_spam():
    assert spam_email()=="this is a spam email"

