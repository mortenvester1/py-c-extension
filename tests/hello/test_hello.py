import pytest
from spammer.hello import helloworld, greeting


@pytest.mark.parametrize(
    "expected_output",
    [
        "Hello World from C extension!"
    ]
)
def test_helloworld(expected_output):
    assert helloworld()==expected_output


@pytest.mark.parametrize(
    "name,number",
    [
        ("gurpgork", 5),
        ("gurpgork", 10)
    ]
)
def test_greeting(name, number):
    assert greeting(name, number)==f"Hello {name}! You gave me the number {number}."
