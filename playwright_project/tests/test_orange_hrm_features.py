"""
Use below command to run a particular test case from the file in the terminal:
pytest test_orange_hrm_features.py::test_login_using_url

Use below command to run a particular test case with tracing from the file in the terminal:
pytest test_orange_hrm_features.py::test_login_using_url --tracing=on
This should create trace.zip file in the root directory of the project. This is not working at the moment.

Use below command to run all the test cases from the file in the terminal:
pytest test_orange_hrm_features.py
"""

from playwright.sync_api import expect, Page
from playwright_project.conftest import page
from playwright_project.pages.oragehrm_login_page import OrangeHRMLoginPage, OrangeHRMHomePage
import pytest, csv


def get_test_data_from_csv(file_path: str = "./test_data/test_data.csv") -> list:
    test_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if present
        for row in csv_reader:
            if len(row) >= 2:
                test_data.append((row[0], row[1]))
    return test_data



def test_login(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("listitem").filter(has_text="Ahmed Elian").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()


def test_main_page_and_dashboard_components(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.locator("form")).to_contain_text("Username")
    expect(page.locator("form")).to_contain_text("Password")
    expect(page.get_by_role("button")).to_contain_text("Login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.get_by_role("listitem").filter(has_text="manda userDoe").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()


def test_login_using_page_object_model(page: Page) -> None:
    orange_hrm_login_page = OrangeHRMLoginPage(page)
    orange_hrm_login_page.login("Admin", "admin123")
    orange_hrm_login_page.verify_login_successful()
    orange_hrm_login_page.logout()


@pytest.mark.parametrize("username,password", get_test_data_from_csv())
def test_login_using_url(page: Page, username: str, password: str) -> None:
    orange_hrm_login_page = OrangeHRMLoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    orange_hrm_login_page.enter_username(username)
    orange_hrm_login_page.enter_password(password)
    orange_hrm_login_page.click_login()
    orange_hrm_login_page.verify_login_successful()


def test_home_page_is_visible_and_logout_is_successful(page: Page, username: str, password:str) -> None:
    orange_hrm_login_page = OrangeHRMLoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    orange_hrm_login_page.enter_username("Admin")
    orange_hrm_login_page.enter_password("admin123")
    orange_hrm_login_page.click_login()
    orange_hrm_login_page.verify_login_successful()
    orange_hrm_home_page = OrangeHRMHomePage(page)
    orange_hrm_home_page.verify_dashboard_visible()
    orange_hrm_home_page.verify_user_menu_visible()
    orange_hrm_home_page.verify_logout_menu_is_visible()
    orange_hrm_home_page.logout_is_successful()


