from faker import Faker
import pytest


@pytest.fixture
def random_email():
    faker = Faker()
    return faker.email()


@pytest.fixture
def random_new_email():
    faker = Faker()
    return faker.email()


@pytest.fixture
def random_first_name():
    faker = Faker()
    return faker.first_name()


@pytest.fixture
def random_last_name():
    faker = Faker()
    return faker.last_name()


@pytest.fixture
def random_password():
    faker = Faker()
    return faker.password()
