"""
==========================================================
Lesson 09 - Advanced Locators
==========================================================

Topics Covered:
---------------
1. locator()
2. locator.locator()
3. filter()
4. has_text
5. has
6. Locator Chaining
7. Parent -> Child
8. Dynamic Locators
9. Strict Mode
==========================================================
"""

from playwright.sync_api import sync_playwright, expect


def login(page):
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


def add_to_cart(page, product_name):

    (
        page.locator(".inventory_item")
        .filter(has_text=product_name)
        .get_by_role("button", name="Add to cart")
        .click()
    )


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    login(page)

    # --------------------------------------------
    # locator()
    # --------------------------------------------

    products = page.locator(".inventory_item")

    expect(products).to_have_count(6)

    print("Total Products:", products.count())

    # --------------------------------------------
    # locator.locator()
    # Parent -> Child
    # --------------------------------------------

    product_names = products.locator(
        ".inventory_item_name"
    )

    print("\nProduct Names")

    for i in range(product_names.count()):
        print(product_names.nth(i).text_content())

    # --------------------------------------------
    # filter(has_text)
    # --------------------------------------------

    backpack = products.filter(
        has_text="Sauce Labs Backpack"
    )

    expect(backpack).to_have_count(1)

    print("\nBackpack Found")

    # --------------------------------------------
    # Locator Chaining
    # --------------------------------------------

    backpack.get_by_role(
        "button",
        name="Add to cart"
    ).click()

    expect(
        backpack.get_by_role(
            "button",
            name="Remove"
        )
    ).to_be_visible()

    print("Backpack Added")

    # --------------------------------------------
    # filter(has=locator)
    # --------------------------------------------

    remove_button = page.get_by_role(
        "button",
        name="Remove"
    )

    added_product = products.filter(
        has=remove_button
    )

    expect(added_product).to_have_count(1)

    print("\nProduct Having Remove Button")

    print(
        added_product.locator(
            ".inventory_item_name"
        ).text_content()
    )

    # --------------------------------------------
    # Dynamic Locator Function
    # --------------------------------------------

    add_to_cart(
        page,
        "Sauce Labs Bike Light"
    )

    bike_light = products.filter(
        has_text="Sauce Labs Bike Light"
    )

    expect(
        bike_light.get_by_role(
            "button",
            name="Remove"
        )
    ).to_be_visible()

    print("Bike Light Added")

    # --------------------------------------------
    # Multiple filter()
    # --------------------------------------------

    backpack_again = (
        page.locator(".inventory_item")
        .filter(has_text="Backpack")
    )

    expect(backpack_again).to_have_count(1)

    # --------------------------------------------
    # first
    # --------------------------------------------

    print("\nFirst Product")

    print(
        products.first.locator(
            ".inventory_item_name"
        ).text_content()
    )

    # --------------------------------------------
    # last
    # --------------------------------------------

    print("\nLast Product")

    print(
        products.last.locator(
            ".inventory_item_name"
        ).text_content()
    )

    # --------------------------------------------
    # nth
    # --------------------------------------------

    print("\nThird Product")

    print(
        products.nth(2).locator(
            ".inventory_item_name"
        ).text_content()
    )

    # --------------------------------------------
    # Open Backpack Details
    # --------------------------------------------

    backpack.locator(
        ".inventory_item_name"
    ).click()

    expect(
        page.locator(".inventory_details_name")
    ).to_have_text(
        "Sauce Labs Backpack"
    )

    print("\nProduct Details Page Opened")

    page.go_back()

    # --------------------------------------------
    # Verify Products Again
    # --------------------------------------------

    expect(products).to_have_count(6)

    page.wait_for_timeout(5000)

    browser.close()