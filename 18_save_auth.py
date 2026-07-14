from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://www.saucedemo.com")

    page.get_by_placeholder(
        "Username"
    ).fill("standard_user")

    page.get_by_placeholder(
        "Password"
    ).fill("secret_sauce")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    page.wait_for_url(
        "**/inventory.html"
    )

    # Save Authentication

    context.storage_state(
        path="auth.json"
    )

    print("Authentication Saved!")

    browser.close()