"""
==========================================================
Lesson 12 - Dialogs & Popups
==========================================================

Topics Covered:
---------------
1. Alert Dialog
2. Confirm Dialog
3. Prompt Dialog
4. dialog.accept()
5. dialog.dismiss()
6. dialog.message
7. dialog.type
==========================================================
"""

from playwright.sync_api import sync_playwright, expect


def handle_alert(dialog):

    print("\n========== ALERT ==========")
    print("Type    :", dialog.type)
    print("Message :", dialog.message)

    dialog.accept()


def handle_confirm_accept(dialog):

    print("\n========== CONFIRM ==========")
    print("Type    :", dialog.type)
    print("Message :", dialog.message)

    dialog.accept()


def handle_confirm_dismiss(dialog):

    print("\n========== CONFIRM ==========")
    print("Type    :", dialog.type)
    print("Message :", dialog.message)

    dialog.dismiss()


def handle_prompt(dialog):

    print("\n========== PROMPT ==========")
    print("Type    :", dialog.type)
    print("Message :", dialog.message)

    dialog.accept("Thara")


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto(
        "https://the-internet.herokuapp.com/javascript_alerts"
    )

    # =====================================================
    # Example 1 - Alert
    # =====================================================

    page.on("dialog", handle_alert)

    page.get_by_role(
        "button",
        name="Click for JS Alert"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text(
        "You successfully clicked an alert"
    )

    page.remove_listener("dialog", handle_alert)

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 2 - Confirm (Accept)
    # =====================================================

    page.on("dialog", handle_confirm_accept)

    page.get_by_role(
        "button",
        name="Click for JS Confirm"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text(
        "You clicked: Ok"
    )

    page.remove_listener(
        "dialog",
        handle_confirm_accept
    )

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 3 - Confirm (Dismiss)
    # =====================================================

    page.on("dialog", handle_confirm_dismiss)

    page.get_by_role(
        "button",
        name="Click for JS Confirm"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text(
        "You clicked: Cancel"
    )

    page.remove_listener(
        "dialog",
        handle_confirm_dismiss
    )

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 4 - Prompt
    # =====================================================

    page.on("dialog", handle_prompt)

    page.get_by_role(
        "button",
        name="Click for JS Prompt"
    ).click()

    expect(
        page.locator("#result")
    ).to_have_text(
        "You entered: Thara"
    )

    page.remove_listener(
        "dialog",
        handle_prompt
    )

    print("\nAll Dialog Examples Passed Successfully!")

    page.wait_for_timeout(5000)

    browser.close()