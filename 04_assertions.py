"""
==========================================================
Lesson 04 - Assertions
==========================================================

Topics Covered:
---------------
1. expect()
2. to_have_title()
3. to_have_url()
4. to_be_visible()
5. to_have_text()
6. to_have_count()
7. to_have_value()
8. to_be_enabled()
9. not_to_have_url()
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

    # ----------------------------------------
    # Open Website
    # ----------------------------------------
    page.goto("https://www.saucedemo.com/")

    # ----------------------------------------
    # Page Assertions
    # ----------------------------------------
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/")

    # ----------------------------------------
    # Element Visibility
    # ----------------------------------------
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    login_button = page.get_by_role("button", name="Login")

    expect(username).to_be_visible()
    expect(password).to_be_visible()
    expect(login_button).to_be_visible()

    # ----------------------------------------
    # Element State
    # ----------------------------------------
    expect(username).to_be_enabled()
    expect(password).to_be_enabled()
    expect(login_button).to_be_enabled()

    # ----------------------------------------
    # Fill Form
    # ----------------------------------------
    username.fill("standard_user")
    password.fill("secret_sauce")

    # ----------------------------------------
    # Verify Values
    # ----------------------------------------
    expect(username).to_have_value("standard_user")
    expect(password).to_have_value("secret_sauce")

    # ----------------------------------------
    # Login
    # ----------------------------------------
    login_button.click()

    # ----------------------------------------
    # Verify Successful Login
    # ----------------------------------------
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(page).not_to_have_url(
        "https://www.saucedemo.com/"
    )

    # ----------------------------------------
    # Verify Page Heading
    # ----------------------------------------
    heading = page.locator(".title")

    expect(heading).to_have_text("Products")
    expect(heading).to_be_visible()

    # ----------------------------------------
    # Verify Product Count
    # ----------------------------------------
    products = page.locator(".inventory_item")

    expect(products).to_have_count(6)

    print("All Assertions Passed Successfully!")

    page.wait_for_timeout(5000)

    browser.close()