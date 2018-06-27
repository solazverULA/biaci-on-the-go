# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Registerloging(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registerloging(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Login").click()
        time.sleep(0.5)
        driver.find_element_by_link_text("Sign Up").click()
        time.sleep(0.5)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("MiguelMendez")
        time.sleep(0.5)
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Miguel Arturo")
        time.sleep(0.5)
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Mendez Rosales")
        time.sleep(0.5)
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("V023555449")
        time.sleep(0.5)
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("miguel@ula.ve")
        time.sleep(0.5)
        driver.find_element_by_id("id_cod_area").clear()
        driver.find_element_by_id("id_cod_area").send_keys("0424")
        time.sleep(0.5)
        driver.find_element_by_id("id_num_telefono").clear()
        driver.find_element_by_id("id_num_telefono").send_keys("4234565")
        time.sleep(0.5)
        driver.find_element_by_id("id_sexo").click()
        Select(driver.find_element_by_id("id_sexo")).select_by_visible_text("Masculino")
        time.sleep(0.5)
        driver.find_element_by_xpath("//option[@value='M']").click()
        driver.find_element_by_id("id_direccion").clear()
        driver.find_element_by_id("id_direccion").send_keys("Bailadores")
        time.sleep(0.5)
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("1234qwer")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("1234qwer")
        time.sleep(0.5)
        driver.find_element_by_name("submit").click()
        time.sleep(4)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("MiguelMendez")
        time.sleep(0.5)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("1234qwer")
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Log Out").click()
        time.sleep(5)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
