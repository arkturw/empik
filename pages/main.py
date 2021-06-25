from selenium.webdriver.common.by import By


class MainPage:

    # Adres strony głównej
    URL = 'https://www.empikfoto.pl'

    # Lokatory obiektów
    LOGIN_BTN = (By.XPATH, '//li[@class="for-guest"]/a[text()="Zaloguj"]')
    USERNAME_TEXT = (By.CLASS_NAME, 'service-login-username')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        """
        Załadowanie strony głównej w przeglądarce
        """
        self.browser.get(self.URL)

    def go_to_login_page(self):
        """
        Przejście na stronę logowania
        """
        login_btn = self.browser.find_element(*self.LOGIN_BTN)
        login_btn.click()

    # Asercje
    def is_user_logged_in(self, expected_name):
        """
        Sprawdzenie czy wyświetlana nazwa użytkownika jest identyczna z oczekiwaną
        :param expected_name: string, oczekiwana nazwa użytkownika
        :return: Zwraca 'True' jeśli rezultat testu pozytywny i 'False' jeśli negatywny
        """
        username_text = self.browser.find_element(*self.USERNAME_TEXT)
        if username_text.text == expected_name:
            return True
        else:
            return False