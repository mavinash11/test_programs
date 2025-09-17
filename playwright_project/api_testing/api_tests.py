from playwright.sync_api import sync_playwright


def test_api_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
        assert response.status == 200
        json_response = response.json()
        print(f"Json response: {json_response}")
        request_context.dispose()


def test_post_api_request():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        payload = {
            "Name": "avinash",
            "lasName": "am",
            "userId": 1000
        }
        response = request_context.post("https://jsonplaceholder.typicode.com/posts", data=payload)
        assert response.status == 201
        assert response.ok
        json_resp = response.json()
        print(f"Json response: {json_resp}")
        request_context.dispose()

