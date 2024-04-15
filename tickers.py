import requests

def test_response(search_text):
    headers = {
            'Content-Type': 'application/json',
            'Authorization' : 'Token c2f2aa3024fb7027f3d7ca69f586edb60761661f'
            }
    requestResponse = requests.get(f"https://api.tiingo.com/tiingo/utilities/search?query={search_text}",
                                        headers=headers).json()
    return requestResponse