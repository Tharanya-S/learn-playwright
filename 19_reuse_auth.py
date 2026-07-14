from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context(

        storage_state="auth.json"

    )

    page = context.new_page()

    page.goto(
        "https://www.saucedemo.com/inventory.html"
    )

    page.wait_for_timeout(5000)

    browser.close()