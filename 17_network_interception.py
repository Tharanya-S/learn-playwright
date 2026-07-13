"""
==========================================================
Lesson 17 - Network Interception
==========================================================

Topics Covered:
---------------
1. page.route()
2. route.request
3. route.continue_()
4. route.abort()
5. route.fulfill()
6. Block Images
7. Log Requests
8. Mock API Response
==========================================================
"""

from playwright.sync_api import sync_playwright


# ==========================================================
# Example 1 : Log Every Request
# ==========================================================

def log_requests(route):

    request = route.request

    print("--------------------------------")

    print("Method        :", request.method)
    print("URL           :", request.url)
    print("Resource Type :", request.resource_type)

    route.continue_()


# ==========================================================
# Example 2 : Block Images
# ==========================================================

def block_images(route):

    if route.request.resource_type == "image":

        print("Blocked Image :", route.request.url)

        route.abort()

    else:

        route.continue_()


# ==========================================================
# Example 3 : Modify Headers
# ==========================================================

def modify_headers(route):

    headers = route.request.headers.copy()

    headers["X-Test-Automation"] = "Playwright"

    route.continue_(headers=headers)


# ==========================================================
# Example 4 : Mock API Response
# ==========================================================

def mock_api(route):

    print("Mocking API...")

    route.fulfill(

        status=200,

        content_type="application/json",

        body="""
        {
            "page":1,
            "data":[
                {
                    "id":101,
                    "email":"playwright@test.com",
                    "first_name":"Playwright",
                    "last_name":"Automation"
                }
            ]
        }
        """
    )


with sync_playwright() as p:

    browser = p.chromium.launch(

        headless=False,

        slow_mo=500

    )

    context = browser.new_context()

    page = context.new_page()

    # ======================================================
    # Example 1 : Log Every Request
    # ======================================================

    print("\n========== LOG REQUESTS ==========\n")

    page.route(

        "**/*",

        log_requests

    )

    page.goto("https://www.saucedemo.com")

    page.unroute("**/*", log_requests)

    page.wait_for_timeout(2000)

    # ======================================================
    # Example 2 : Block Images
    # ======================================================

    print("\n========== BLOCK IMAGES ==========\n")

    page.route(

        "**/*",

        block_images

    )

    page.reload()

    page.unroute("**/*", block_images)

    page.wait_for_timeout(2000)

    # ======================================================
    # Example 3 : Modify Request Headers
    # ======================================================

    print("\n========== MODIFY HEADERS ==========\n")

    page.route(

        "**/*",

        modify_headers

    )

    page.reload()

    page.unroute("**/*", modify_headers)

    page.wait_for_timeout(2000)

    # ======================================================
    # Example 4 : Mock API
    # ======================================================

    print("\n========== MOCK API ==========\n")

    page.route(

        "https://reqres.in/api/users?page=2",

        mock_api

    )

    page.goto(

        "https://reqres.in/api/users?page=2"
    )

    print(page.text_content("body"))

    page.unroute(

        "https://reqres.in/api/users?page=2",

        mock_api

    )

    page.wait_for_timeout(3000)

    browser.close()