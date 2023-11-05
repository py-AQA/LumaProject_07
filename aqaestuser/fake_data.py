import pytest
from faker import Faker


@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def email():
    return Faker().email()


@pytest.fixture
def password():
    return Faker().password()


class TestDriver:
    my_login = None
    my_password = None
    driver = None

    @property
    def first_name(self):
        return Faker().first_name()

    @property
    def last_name(self):
        return Faker().last_name()

    @property
    def email(self):
        return Faker().email()

    @property
    def password(self):
        return Faker().password()

    @property
    def company(self):
        return Faker().company()

    @property
    def phone_number(self):
        return Faker().phone_number()

    @property
    def postcode(self):
        return Faker().postcode()

    @property
    def secondary_address(self):
        return Faker().secondary_address()

    @property
    def street_address(self):
        return Faker().street_address()

    @property
    def city(self):
        return Faker().city()

    @property
    def state(self):
        return Faker().state()
