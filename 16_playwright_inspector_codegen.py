"""
==========================================================
Lesson 16 - Playwright Inspector & Codegen
==========================================================

Topics Covered:
---------------
1. page.pause()
2. Playwright Inspector
3. Locator Debugging
4. Action Log
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

    # ---------------------------------------------
    # Open SauceDemo
    # ---------------------------------------------

    page.goto("https://www.saucedemo.com")

    # ---------------------------------------------
    # Pause Execution
    # ---------------------------------------------

    page.pause()

    # After clicking Resume in the Inspector,
    # the code below will execute.

    page.get_by_placeholder(
        "Username"
    ).fill("standard_user")

    page.pause()

    page.get_by_placeholder(
        "Password"
    ).fill("secret_sauce")

    page.pause()

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    page.pause()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    page.pause()

    page.locator(".inventory_item").first.click()

    page.pause()

    expect(
        page.locator(".inventory_details_name")
    ).to_be_visible()

    print("Inspector Demo Completed Successfully!")

    page.wait_for_timeout(5000)

    browser.close()