import time

import pytest

from pages.create_account import CreateAccountForm


@pytest.mark.parametrize('locator, expected', [('firstname', 'First Name *'),
                                               ('lastname', 'Last Name *'),
                                               ('email_address', 'Email *'),
                                               ('password', 'Password *'),
                                               ('password-confirmation', 'Confirm Password *')])
def test_account_form_label(driver, locator, expected):
    page = CreateAccountForm(driver)
    assert page.element_label(locator) == expected




