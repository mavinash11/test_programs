from dataclasses import dataclass
from typing import Dict, List, Optional
from playwright.sync_api import Page, expect

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


class OrangeHRMLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.USERNAME_INPUT = page.get_by_role("textbox", name="Username")
        self.PASSWORD_INPUT = page.get_by_role("textbox", name="Password")
        self.LOGIN_BUTTON = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(URL)
        self.page.wait_for_load_state("load")
        return self

    def enter_username(self, username: str):
        self.USERNAME_INPUT.fill(username)
        return self

    def enter_password(self, password: str):
        self.PASSWORD_INPUT.fill(password)
        return self

    def click_login(self):
        self.LOGIN_BUTTON.click()
        return self

    def login(self, username: str, password: str):
        self.navigate()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def verify_login_successful(self):
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
        return self

    def logout(self):
        self.page.get_by_role("listitem").filter(has_text="Ahmed Elian").locator("i").click()
        self.page.get_by_role("menuitem", name="Logout").click()
        return self


class OrangeHRMHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.DASHBOARD_HEADING = page.get_by_role("heading", name="Dashboard")
        self.USER_MENU = page.get_by_role("listitem").filter(has_text="Ahmed Elian")
        self.LOGOUT_MENU_ITEM = page.get_by_role("menuitem", name="Logout")

    def verify_dashboard_visible(self):
        expect(self.DASHBOARD_HEADING).to_be_visible()
        return self

    def verify_user_menu_visible(self):
        expect(self.USER_MENU).to_be_visible()
        return self

    def verify_logout_menu_is_visible(self):
        self.USER_MENU.locator("i").click()
        expect(self.LOGOUT_MENU_ITEM).to_be_visible()
        return self

    def logout_is_successful(self):
        self.verify_logout_menu_is_visible()
        self.LOGOUT_MENU_ITEM.click()
        expect(self.page.get_by_role("button", name="Login")).to_be_visible()
        return self

