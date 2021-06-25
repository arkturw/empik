from selenium.webdriver.common.by import By


class LoginPage:

    # Lokatory obiektów
    USER_INPUT = (By.NAME, '_username')
    PASS_INPUT = (By.NAME, '_password')
    REMEMBER_ME_CHECKBOX = (By.NAME, '_remember_me')
    LOGIN_BTN = (By.ID, 'loginForm')
    ERROR_MSG = (By.XPATH, '//span[text()="Błędny użytkownik lub hasło."]')

    def __init__(self, browser):
        self.browser = browser

    def pass_user_data(self, username, password):
        """
        Wypełnianie formatki logowania danymi
        :param username: string, nazwa użytkownika
        :param password: string, hasło użytkownika
        """
        user_input = self.browser.find_element(*self.USER_INPUT)
        user_input.send_keys(username)
        pass_input = self.browser.find_element(*self.PASS_INPUT)
        pass_input.send_keys(password)

    def uncheck_remember_me(self):
        """
        Kliknięcie na checkboksie "Zapamiętaj mnie"
        """
        remember_me_checkbox = self.browser.find_element(*self.REMEMBER_ME_CHECKBOX)
        remember_me_checkbox.click()

    def login(self):
        """
        Kliknięcie na przycisku logowania
        """
        login_button = self.browser.find_element(*self.LOGIN_BTN)
        login_button.click()

    # Asercje
    def is_error_message_displayed(self):
        """
        Sprawdzenie czy na ekranie wyświetlony zostaje komunikat błędu logowania
        :return: Zwraca 'True' jeśli rezultat testu pozytywny i 'False' jeśli negatywny
        """
        try:
            error_message = self.browser.find_element(*self.ERROR_MSG)
            if error_message.is_displayed():
                return True
            else:
                return False
        except Exception as err:
            print('Wystąpił wyjątek:', err)
            return False