"""
==========================================================
Lesson 03 - User Actions
==========================================================

Topics Covered:
---------------
1. fill()
2. click()
3. press()
4. press_sequentially()
5. clear using fill("")
6. Login
==========================================================
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()
    page = context.new_page()

    # Open Website
    page.goto("https://www.saucedemo.com/")

    # ----------------------------------------
    # fill()
    # ----------------------------------------
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")

    username.fill("standard_user")
    password.fill("secret_sauce")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # Clear Text
    # ----------------------------------------
    username.fill("")
    password.fill("")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # press_sequentially()
    # Types one character at a time
    # ----------------------------------------
    username.press_sequentially("standard_user")
    password.press_sequentially("secret_sauce")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # Keyboard Actions
    # ----------------------------------------

    # Select all text (Windows/Linux)
    username.press("Control+A")

    # macOS users can use:
    # username.press("Meta+A")

    # Replace selected text
    username.fill("standard_user")

    # Move to password field using Tab
    username.press("Tab")

    # Press Enter on password field (doesn't submit yet)
    password.press("Enter")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # Click Login Button
    # ----------------------------------------
    page.get_by_role(
        "button",
        name="Login"
    ).click()

    # ----------------------------------------
    # Verify Login Successful
    # ----------------------------------------
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    print("Login Successful!")

    page.wait_for_timeout(5000)

    browser.close()