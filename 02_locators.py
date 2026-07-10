"""
==========================================================
Lesson 02 - Locators
==========================================================

Topics Covered:
---------------
1. get_by_placeholder()
2. get_by_role()
3. get_by_text()
4. locator()
5. CSS Selectors
6. XPath
==========================================================
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()
    page = context.new_page()

    # Navigate to SauceDemo
    page.goto("https://www.saucedemo.com/")

    # --------------------------------------------------
    # get_by_placeholder()
    # --------------------------------------------------
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")

    print("Username Locator:", username)
    print("Password Locator:", password)

    # --------------------------------------------------
    # get_by_role()
    # --------------------------------------------------
    login_button = page.get_by_role(
        "button",
        name="Login"
    )

    print("Login Button:", login_button)

    # --------------------------------------------------
    # get_by_text()
    # --------------------------------------------------
    login_text = page.get_by_text("Login")

    print("Login Text:", login_text)

    # --------------------------------------------------
    # CSS Selector using locator()
    # --------------------------------------------------
    username_css = page.locator("#user-name")
    password_css = page.locator("#password")
    login_css = page.locator("#login-button")

    print("Username CSS:", username_css)
    print("Password CSS:", password_css)
    print("Login CSS:", login_css)

    # --------------------------------------------------
    # XPath
    # --------------------------------------------------
    username_xpath = page.locator("//input[@id='user-name']")
    password_xpath = page.locator("//input[@id='password']")
    login_xpath = page.locator("//input[@id='login-button']")

    print("Username XPath:", username_xpath)
    print("Password XPath:", password_xpath)
    print("Login XPath:", login_xpath)

    # --------------------------------------------------
    # Highlight Elements (Optional)
    # --------------------------------------------------
    username.highlight()
    password.highlight()
    login_button.highlight()

    page.wait_for_timeout(5000)

    browser.close()