"""
==========================================================
Lesson 06 - Browser Navigation
==========================================================

Topics Covered:
---------------
1. page.goto()
2. page.go_back()
3. page.go_forward()
4. page.reload()
5. page.wait_for_load_state()
6. page.url
7. page.title()
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
    # Open Login Page
    # ----------------------------------------
    page.goto("https://www.saucedemo.com/")

    print(f"Current URL : {page.url}")
    print(f"Page Title  : {page.title()}")

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

    # ----------------------------------------
    # Login
    # ----------------------------------------
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # ----------------------------------------
    # Wait Until Inventory Page Loads
    # ----------------------------------------
    page.wait_for_url("**/inventory.html")
    page.wait_for_load_state("load")

    print("\nAfter Login")
    print(f"Current URL : {page.url}")
    print(f"Page Title  : {page.title()}")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # ----------------------------------------
    # Reload Current Page
    # ----------------------------------------
    print("\nReloading Page...")
    page.reload()

    page.wait_for_load_state("load")

    print("Reload Completed")

    # ----------------------------------------
    # Go Back
    # ----------------------------------------
    print("\nGoing Back...")
    page.go_back()

    page.wait_for_load_state("load")

    print(f"Current URL : {page.url}")

    # On SauceDemo, going back returns to login page
    expect(page).to_have_url("https://www.saucedemo.com/")

    # ----------------------------------------
    # Go Forward
    # ----------------------------------------
    print("\nGoing Forward...")
    page.go_forward()

    page.wait_for_load_state("load")

    print(f"Current URL : {page.url}")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # ----------------------------------------
    # Refresh Again
    # ----------------------------------------
    print("\nRefreshing Again...")
    page.reload()

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)

    print("\nNavigation Demo Completed Successfully!")

    page.wait_for_timeout(5000)

    browser.close()