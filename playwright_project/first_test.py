from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        print("Page title:", page.title())
        browser.close()
        return True


if __name__ == "__main__":
    run()



