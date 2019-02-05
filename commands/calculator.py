import requests
import urllib


def calculate(expr):
    response = requests.get(f'http://api.mathjs.org/v4/?expr={urllib.parse.quote(expr)}')
    if response.status_code == 200:
        return f'Result: {response.text}'
    return 'Error happened. Use a valid expression'


if __name__ == '__main__':
    print(calculate('3*sqrt(4)+5^2*2'))  # 56
