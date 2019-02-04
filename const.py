'''Constants File
Tokens and such'''

import os
import sys

# provide bot token from TOKEN envVar or config file
TOKEN = os.environ.get('TOKEN')
# other services tokens
YANDEX = os.environ.get('YANDEX')
CAP = os.environ.get('CAP')  # cryptocompare token
# twitter API stuff
T_API = os.environ.get('T_API')
T_API_SECRET = os.environ.get('T_API_SECRET')
T_TOKEN = os.environ.get('T_TOKEN')
T_TOKEN_SECRET = os.environ.get('T_TOKEN_SECRET')


if __name__ == '__main__':
    if not TOKEN or not YANDEX or not CAP or not T_API or not T_API_SECRET or not T_TOKEN or not T_TOKEN_SECRET:
        print('WARNING: Some tokens are not set in your environment')
        sys.exit(1)
    print('TOKENS are set.')
    sys.exit(0)
