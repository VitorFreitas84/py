"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest

def test_prefix():
    """Verify that the prefix function works correctly."""
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function and use assert statements to verify
    # that the string returned by the prefix function is correct.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"

def test_suffix():
    """Verify that the suffix function works correctly."""
    # Call the suffix function and verify that it returns a string.
    suf = suffix("upbeat", "upgrade")
    assert isinstance(suf, str), "suffix function must return a string"

    # Call the suffix function and use assert statements to verify
    # that the string returned by the suffix function is correct.
    assert suffix("cat", "catalog") == "at"
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("happy", "funny") == ""
    assert suffix("cat", "catalog") == "at"
    assert suffix("dogmatic", "dog") == "dog"
    assert suffix("jump", "joyous") == "ous"
    assert suffix("upbeat", "upgrade") == "grade"
    assert suffix("Disable", "dIstasteful") == "tasteful"

# Call the main function that is part of pytest to execute the test functions.
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])

