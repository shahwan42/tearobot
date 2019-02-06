# TBot
  A toy telegram bot using python. [Try it](https://t.me/tearobot)

## features:
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
- [x] calculator
- [x] CryptoCurrency Price
- [x] CryptoCurrency News
- [ ] financial tracking
- [ ] ToDo list manager
- [x] Tweet text
- [ ] Tweet images with captions
- [ ] Youtube search
- [ ] NLP-based commands
- [ ] how old? (predict the age of somebody from their photo)
- [ ] Morning quote/ quote of today
- [ ] Inspirational quotes (inspire_me)
- [ ] Reminder (date/appointment)
- [ ] Voice-based commands
- [ ] Form registrations (like mutex's)
- [ ] Pay my bills (teapay)
- [ ] What else?

## To Try/Contribute:

> On a Linux System (figure out how to do it on windows yourself):

* make sure you have `git`, `python(v3.7)` and `pipenv` installed on your system
* create a Bot on Telegram to test on. [see how](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* clone the repo `$git clone https://github.com/ahmed75320/tearobot/`
* go to project folder `$cd tearobot`
* `$pipenv install` install dependencies and create a virtualenv
* rename the `.env-sample` file to `.env` and provide your tokens inside it
* `$pipenv shell` launch the a virtual environment (this will source the .env variables into the virtual environment, so you don't have to export them yourself)
* `$python tea.py`
* see how it works
* open an issue with the feature you want to add
* open the project folder in your code editor (e.g VS Code)
* to develop a new command/edit a current one:
    - open `commands` folder
    - create new file `your-command-name.py` OR open a current command file you want to update
    - add your code
    - import it in the main `tea.py` file
    - follow the other command style (you should figure out this part from the code)
    - test if it's working on your test bot
    - add the command to the list above
    - make a pull request
