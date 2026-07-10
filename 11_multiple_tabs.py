from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    context = browser.new_context()

    page = context.new_page()

    page.goto(
        "https://the-internet.herokuapp.com/windows"
    )

    expect(
        page.get_by_text("Opening a new window")
    ).to_be_visible()

    print("Original Tab")
    print(page.title())
    print(page.url)

    # ------------------------------------
    # Wait for New Tab
    # ------------------------------------

    with context.expect_page() as new_page_info:

        page.get_by_role(
            "link",
            name="Click Here"
        ).click()

    new_page = new_page_info.value

    new_page.wait_for_load_state()

    print("\nNew Tab")

    print(new_page.title())
    print(new_page.url)

    expect(
        new_page.get_by_text("New Window")
    ).to_be_visible()

    # ------------------------------------
    # Total Tabs
    # ------------------------------------

    print("\nOpen Tabs")

    print(len(context.pages))

    for i, tab in enumerate(context.pages, start=1):

        print(f"Tab {i}")

        print(tab.title())

    # ------------------------------------
    # Bring New Tab to Front
    # ------------------------------------

    new_page.bring_to_front()

    page.wait_for_timeout(2000)

    # ------------------------------------
    # Close New Tab
    # ------------------------------------

    new_page.close()

    print("\nNew Tab Closed")

    print("Remaining Tabs:", len(context.pages))

    page.bring_to_front()

    page.wait_for_timeout(5000)

    browser.close()

#   Best Practices

#.   ✅ Use context.expect_page() when an action opens a new tab.

#.   ✅ Call new_page.wait_for_load_state() before interacting with the new page.

#.   ✅ Use context.pages if you need to inspect all currently open tabs.

#.   ✅ Close tabs that are no longer needed to keep your tests clean.