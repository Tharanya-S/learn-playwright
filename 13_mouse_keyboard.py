"""
==========================================================
Lesson 13 - Mouse & Keyboard
==========================================================

Topics Covered:
---------------
1. Hover
2. Double Click
3. Right Click
4. Drag and Drop
5. Mouse Move
6. Mouse Down
7. Mouse Up
8. Keyboard Press
9. Keyboard Type
10. Keyboard Shortcuts
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

    # =====================================================
    # Example 1 - Hover
    # =====================================================

    page.goto("https://demoqa.com/menu")

    page.get_by_text("Main Item 2").hover()

    print("Hover Performed")

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 2 - Double Click
    # =====================================================

    page.goto("https://demoqa.com/buttons")

    page.get_by_text("Double Click").dblclick()

    print("Double Click Completed")

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 3 - Right Click
    # =====================================================

    page.get_by_text("Right Click Me").click(
        button="right"
    )

    print("Right Click Completed")

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 4 - Keyboard
    # =====================================================

    page.goto("https://demoqa.com/text-box")

    name = page.locator("#userName")

    name.click()

    page.keyboard.type("Thara")

    page.keyboard.press("Tab")

    page.keyboard.type("thara@test.com")

    page.keyboard.press("Tab")

    page.keyboard.type("Chennai")

    page.keyboard.press("Tab")

    page.keyboard.type("Tamil Nadu")

    print("Keyboard Typing Completed")

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 5 - Keyboard Shortcut
    # =====================================================

    name.click()

    page.keyboard.press("Control+A")

    page.keyboard.press("Backspace")

    page.keyboard.type("Playwright")

    print("Keyboard Shortcut Completed")

    page.wait_for_timeout(2000)

    # =====================================================
    # Example 6 - Mouse Movement
    # =====================================================

    page.mouse.move(300, 300)

    page.wait_for_timeout(500)

    page.mouse.move(500, 300)

    page.wait_for_timeout(500)

    page.mouse.move(700, 300)

    print("Mouse Movement Completed")

    page.wait_for_timeout(2000)

    browser.close()