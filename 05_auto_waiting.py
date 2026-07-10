"""
==========================================================
Lesson 05 - Auto Waiting
==========================================================

Topics Covered:
---------------
1. Auto Waiting
2. wait_for_timeout()
3. wait_for_url()
4. wait_for_load_state()
5. wait_for_selector()
6. wait_for_function()
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
    # Navigate
    # ----------------------------------------
    page.goto("https://www.saucedemo.com/")

    # ----------------------------------------
    # Auto Waiting
    # Playwright automatically waits for
    # elements to become actionable.
    # ----------------------------------------

    page.get_by_placeholder("Username").fill("standard_user")

    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    # ----------------------------------------
    # Wait for URL
    # ----------------------------------------
    page.wait_for_url("**/inventory.html")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # ----------------------------------------
    # Wait for Page Load
    # ----------------------------------------
    page.wait_for_load_state("load")

    # Other options:
    # page.wait_for_load_state("domcontentloaded")
    # page.wait_for_load_state("networkidle")

    # ----------------------------------------
    # Wait for Selector
    # ----------------------------------------
    page.wait_for_selector(".inventory_item")

    # ----------------------------------------
    # Wait for Function
    # Wait until JavaScript condition is true
    # ----------------------------------------
    page.wait_for_function(
        "() => document.title === 'Swag Labs'"
    )

    # ----------------------------------------
    # Verify Products Loaded
    # ----------------------------------------
    products = page.locator(".inventory_item")

    expect(products).to_have_count(6)

    # ----------------------------------------
    # Example of Fixed Wait
    # (Use only for debugging/learning)
    # ----------------------------------------
    page.wait_for_timeout(3000)

    print("Auto Waiting Example Completed Successfully!")

    browser.close()