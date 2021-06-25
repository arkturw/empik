import pytest
from selenium.webdriver import Firefox

from pages.main import MainPage
from pages.login import LoginPage
from test_data.login_data import Negative, Positive


# Pytestowy fixture przygotowujący obiekt drivera do testów
@pytest.fixture
def browser():
    driver = Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_positive(browser:object):
    """
    Logowanie do serwisu poprawnymi danymi
    :param browser: object, instancja drivera
    """

    # Dane logowania
    username = Positive['username']
    password = Positive['password']
    # Nazwa użytkownika oczekiwana w tekście powitalnym
    expected_name = Positive['expected_name']

    # Załadowanie strony głównej i przejście do strony logowania
    main_page = MainPage(browser)
    main_page.load()
    main_page.go_to_login_page()

    # Wypełnienie formatki poprawnymi danymi logowania i odznaczenie checkboxa "Zapamiętaj mnie"
    # oraz logowanie do serwisu
    login_page = LoginPage(browser)
    login_page.pass_user_data(username, password)
    login_page.uncheck_remember_me()
    login_page.login()

    # Sprawdzenie czy wyświetlana nazwa użytkownika jest identyczna z oczekiwaną
    assert main_page.is_user_logged_in(expected_name)


def test_login_negative(browser:object):
    """
    Logowanie do serwisu błędnymi danymi
    :param browser: object, instancja drivera
    """

    # Błędne dane logowania
    username_negative = Negative['username']
    password_negative = Negative['password']

    # Załadowanie strony głównej i przejście do strony logowania
    main_page = MainPage(browser)
    main_page.load()
    main_page.go_to_login_page()

    # Wypełnienie formatki błędnymi danymi logowania i odznaczenie checkboxa "Zapamiętaj mnie"
    # oraz logowanie do serwisu
    login_page = LoginPage(browser)
    login_page.pass_user_data(username_negative, password_negative)
    login_page.uncheck_remember_me()
    login_page.login()

    # Sprawdzenie czy wyświetlony został błąd logowania
    assert login_page.is_error_message_displayed()
