import pytest


def test_user_fn_str(base_user):
    """
    Test custom user model string repre"""
    assert base_user.__str__() == f"{base_user.username}"


def test_full_name(base_user):
    assert (
        base_user.get_full_name
        == f"{base_user.first_name.title()} {base_user.last_name.title()}"
    )


def test_short_name(base_user):
    assert base_user.get_short_name == f"{base_user.username}"
