import requests

url = input("Введите URL: ")

try:
    response = requests.get(url, timeout=5)
    print("Status code:", response.status_code)
    print("Headers:", response.headers)

    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "Server",
        "X-Powered-By"
    ]

    for header in security_headers:
        value = response.headers.get(header)
        if value:
            print(f"{header}: {value}")
        else:
            print(f"{header} нет в запросе")

except requests.exceptions.ConnectionError:
    print("Нет соединения")
except requests.exceptions.Timeout:
    print("Превышено время ожидания")
except requests.exceptions.RequestException as e:
    print("Произошла ошибка:", e)
