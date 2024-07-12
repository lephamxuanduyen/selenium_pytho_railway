from base.base_page import BasePage
from locators.locator import MailPage as MailPageLocator
from utils.actions import Action

class MailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_mail(self):
        if not Action(self.driver).is_select(MailPageLocator.cbx_scramble_address):
            Action(self.driver).click(MailPageLocator.cbx_scramble_address)
        return Action(self.driver).get_text(MailPageLocator.email)

    def confirm_acc(self, mail_confirm_instruction):
        self.refresh()
        self.wait_element_to_visibility(MailPageLocator.email_confirm % mail_confirm_instruction, 30).click()
        self.wait_element_to_visibility(MailPageLocator.link_confirm, 5).click()
