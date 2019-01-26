import requests
import urllib


def calc(expr):
    service_url = 'http://api.mathjs.org/v4/'
    expr_encoded = urllib.parse.quote(expr)
    url = service_url + '?expr=' + expr_encoded
    response = requests.get(url)
    result = ''
    if response.status_code == 200:
        result = f'Result: {response.text}'
    else:
        result = 'Error happened. Try using a valid expression'
    return result


if __name__ == '__main__':
    msg = '3*sqrt(4)+5^2*2'
    result = calc(msg)
    print(result)
