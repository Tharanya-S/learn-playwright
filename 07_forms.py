"""
==========================================================
Lesson 07 - Forms & User Input
==========================================================

Topics Covered:
---------------
1. fill()
2. clear() using fill("")
3. press()
4. press_sequentially()
5. Keyboard Shortcuts
6. select_option()
7. check()
8. uncheck()
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

    # ----------------------------------------------------
    # SauceDemo Login Form
    # ----------------------------------------------------

    page.goto("https://www.saucedemo.com/")

    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")

    # ----------------------------------------
    # fill()
    # ----------------------------------------
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
    # ----------------------------------------
    username.press_sequentially("standard_user")
    password.press_sequentially("secret_sauce")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # Keyboard Actions
    # ----------------------------------------

    # Select all text
    username.press("Control+A")

    # macOS
    # username.press("Meta+A")

    # Delete selected text
    username.press("Backspace")

    username.fill("standard_user")

    # Move focus using TAB
    username.press("Tab")

    page.wait_for_timeout(1000)

    # ----------------------------------------
    # Press Enter to Login
    # ----------------------------------------
    password.press("Enter")

    # ----------------------------------------
    # Assertions
    # ----------------------------------------
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.locator(".inventory_item")
    ).to_have_count(6)

    page.wait_for_timeout(2000)

    # ====================================================
    # HTML Form Demo (Checkbox / Radio / Dropdown)
    # ====================================================

    html = """
    <!DOCTYPE html>
    <html>
    <body>

        <h2>Playwright Form Demo</h2>

        <input type="checkbox" id="newsletter">
        <label for="newsletter">Subscribe</label>

        <br><br>

        <input type="radio" id="male"
               name="gender">
        <label for="male">Male</label>

        <input type="radio" id="female"
               name="gender">
        <label for="female">Female</label>

        <br><br>

        <select id="country">
            <option value="">Select Country</option>
            <option value="india">India</option>
            <option value="usa">USA</option>
            <option value="uk">UK</option>
        </select>

    </body>
    </html>
    """

    page.set_content(html)

    # ----------------------------------------
    # Checkbox
    # ----------------------------------------

    checkbox = page.locator("#newsletter")

    checkbox.check()

    expect(checkbox).to_be_checked()

    page.wait_for_timeout(1000)

    checkbox.uncheck()

    expect(checkbox).not_to_be_checked()

    # ----------------------------------------
    # Radio Button
    # ----------------------------------------

    male = page.locator("#male")
    female = page.locator("#female")

    male.check()

    expect(male).to_be_checked()

    female.check()

    expect(female).to_be_checked()

    expect(male).not_to_be_checked()

    # ----------------------------------------
    # Dropdown
    # ----------------------------------------

    country = page.locator("#country")

    country.select_option("india")

    expect(country).to_have_value("india")

    page.wait_for_timeout(1000)

    country.select_option(label="USA")

    expect(country).to_have_value("usa")

    page.wait_for_timeout(1000)

    country.select_option(index=3)

    expect(country).to_have_value("uk")

    page.wait_for_timeout(3000)

    print("Forms Demo Completed Successfully!")

    browser.close()