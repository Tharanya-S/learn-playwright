"""
==========================================================
Lesson 08 - Collections & Lists
==========================================================

Topics Covered:
---------------
1. locator()
2. count()
3. first
4. last
5. nth()
6. all_text_contents()
7. Loop through elements
8. Click a specific product
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
    # Login
    # ----------------------------------------

    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # ----------------------------------------
    # Collection of Products
    # ----------------------------------------

    products = page.locator(".inventory_item")

    print(f"\nTotal Products: {products.count()}")

    expect(products).to_have_count(6)

    # ----------------------------------------
    # First Product
    # ----------------------------------------

    first_product = products.first

    print("\nFirst Product:")
    print(
        first_product.locator(".inventory_item_name").text_content()
    )

    # ----------------------------------------
    # Last Product
    # ----------------------------------------

    last_product = products.last

    print("\nLast Product:")
    print(
        last_product.locator(".inventory_item_name").text_content()
    )

    # ----------------------------------------
    # nth Product
    # ----------------------------------------

    third_product = products.nth(2)

    print("\nThird Product:")
    print(
        third_product.locator(".inventory_item_name").text_content()
    )

    # ----------------------------------------
    # Get All Product Names
    # ----------------------------------------

    product_names = page.locator(".inventory_item_name")

    print("\nProduct Names:")

    names = product_names.all_text_contents()

    for name in names:
        print(name)

    # ----------------------------------------
    # Loop Using count()
    # ----------------------------------------

    print("\nProducts using count():")

    for i in range(product_names.count()):

        print(
            f"{i+1}.",
            product_names.nth(i).text_content()
        )

    # ----------------------------------------
    # Find Specific Product
    # ----------------------------------------

    print("\nSearching for Backpack...")

    for i in range(product_names.count()):

        name = product_names.nth(i).text_content()

        if name == "Sauce Labs Backpack":

            print("Found:", name)

            product_names.nth(i).click()

            break

    # ----------------------------------------
    # Verify Product Details Page
    # ----------------------------------------

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory-item.html?id=4"
    )

    expect(
        page.locator(".inventory_details_name")
    ).to_have_text("Sauce Labs Backpack")

    print("\nSuccessfully Opened Backpack Details Page!")

    # ----------------------------------------
    # Go Back
    # ----------------------------------------

    page.go_back()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # ----------------------------------------
    # Verify Collection Again
    # ----------------------------------------

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)

    page.wait_for_timeout(5000)

    browser.close()