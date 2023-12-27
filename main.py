import requests

class TestDemo:
    def test_demo(self):
        response = requests.get("https://google.com")
        assert response.status_code == 200