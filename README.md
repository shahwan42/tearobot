# TBot
  A toy telegram bot using python. [Try it](https://t.me/tearobot)

## Services:
- [x] En-Ar word Translator
- [x] En-Ar sentence translation
- [ ] lang-lang translation
- [ ] Conversational Bot
- [ ] Recognise and Translate (translate from image)
- [ ] Extract Text from Image (OCR)
- [ ] Text-to-Speech
- [ ] speech-to-Text
- [x] google search
- [x] latest news
- [x] Weather Today in Zagazig
- [ ] pastebin this code
- [ ] publicly-upload photo and return its link
- [ ] publicly-upload video and return its link
- [ ] publicly-upload file and return its link
- [ ] calculator
- [x] CryptoCurrency Price
- [x] CryptoCurrency News
- [ ] financial tracking
- [ ] ToDo list manager
- [x] Tweet text
- [ ] Tweet images with captions
- [ ] Youtube search
- [ ] NLP-based commands
- [ ] What else?

## To Contribute:
* make sure you have `git`, `python(v3.6+)` and `pipenv` installed on your system
* create a Bot on Telegram to test on. [see how](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* clone the repo `$git clone https://github.com/ahmed75320/tearobot/`
* go to project folder `$cd tearobot`
* `$pipenv install` install dependencies and create a virtualenv
* `$pipenv shell` launch the a virtualenv
* `$export TOKEN=<your-bot-token>`
* `$export YANDEX=<yandex-translate-token>`
* `$export CAP=<crypto-compare-token>`
* `export T_API=<twitter-api-key>`
* `export T_API_SECRET=<twitter-api-secret-key>`
* `export T_TOKEN=<twitter-access-token>`
* `export T_TOKEN_SECRET=<twitter-secret-token>`
* `$python tea.py`
* see how it works
* open an issue with the feature you want to add
* open the project folder in your code editor (e.g VS Code)
* to develop a new service:
    - open `services` folder
    - create new file `your-service-name.py`
    - add you code
    - import it in the main `tea.py` file
    - follow the other services style (you should figure out this part from the code)
    - test if it's working on your test bot
    - make a pull request

