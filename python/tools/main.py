import requests

TARGET_HEADERS = [
    "X-Frame-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "Server",
    "X-Powered-By",
    'User-Agent',
    'Content-Type'
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

results = {}

while True:
    url = input("Введите URL или exit: ")
    if url == 'exit':
        break

    try:
        response = requests.get(url, headers = headers, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f'Ошибка', e)
        continue

    results[url] = {}
    for header in TARGET_HEADERS:
        results[url][header] = response.headers.get(header, 'None')

for site, headers in results.items():
    print(f"\n{site}")
    for header, value in headers.items():
        print(f"  {header}: {value}")