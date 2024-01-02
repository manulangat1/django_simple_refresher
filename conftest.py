import pytest
from pytest_factoryboy import register

from tests.factories import ProfileFactory, UserFactory


register(ProfileFactory)
register(UserFactory)


@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pytest.fixture
def super_user(db, user_factory):
    new = user_factory.create(is_staff=True, is_superuser=True)
    return new


@pytest.fixture
def base_profile(db, profile_factory):
    return profile_factory.create()
