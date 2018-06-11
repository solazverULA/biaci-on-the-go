from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium

        # Abrir la pagina deseada
        selenium.get('http://127.0.0.1:8000/users/signup/')
        # Buscar los elementos del formulario
        username = selenium.find_element_by_id('id_username')
        first_name = selenium.find_element_by_id('id_first_name')
        last_name = selenium.find_element_by_id('id_last_name')
        cedula = selenium.find_element_by_id('id_cedula')
        email = selenium.find_element_by_id('id_email')
        cod_area = selenium.find_element_by_id('id_cod_area')
        num_telefono = selenium.find_element_by_id('id_num_telefono')
        sexo = selenium.find_element_by_id('id_sexo')
        direccion = selenium.find_element_by_id('id_direccion')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')

        submit = selenium.find_element_by_name('submit')

        # Llenar los campos con data
        username.send_keys('yeniferr')
        first_name.send_keys('Yenifer')
        last_name.send_keys('Ramirez')
        cedula.send_keys('V022538371')
        email.send_keys('yeniferramirez11@gmail.com')
        cod_area.send_keys('0414')
        num_telefono.send_keys('0174511')
        sexo.send_keys('F')
        direccion.send_keys('Merida')
        password1.send_keys('123456')
        password2.send_keys('123456')

        # Enviar el formulario
        submit.send_keys(Keys.RETURN)