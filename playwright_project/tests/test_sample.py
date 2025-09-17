import re
from playwright.sync_api import sync_playwright, expect


def test_demo_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.wait_for_load_state("load")
        assert "Google" in page.title()
        browser.close()


def test_demo_page_2(page):
    page.wait_for_timeout(5000)
    page.goto("https://google.com/ncr", wait_until="load")
    try:
        page.get_by_role("button", name="Stay signed out").click(timeout=5000)
    except Exception as e:
        print("No cookie banner")
    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    page.wait_for_timeout(10000)
    page.close()




