# To Contribute

## Install

> On a Linux System (figure out how to do it on windows yourself):

* you need the `telegram` app installed on your desktop/mobile, obviously!
* then make sure you have `git`, `python(v3.6+)` and (Optionally) [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/) installed on your system
* create a Bot on Telegram to test on. [see how](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* Go to your projects folder (e.g `~/Projects`)
* clone the repo `$ git clone https://github.com/ash753/tearobot/`
* go to the project folder `$ cd tearobot`
* if you installed `virtualenvwrapper`, issue this command `$ mkvirtualenv tearobot` to create a new virtual environment
* then `$ workon tearobot` to use that virtual environment and skip the following 2 steps
* OR, if you haven't installed it, run `$ python -m venv venv` create a [virtualenv](https://virtualenv.pypa.io/en/latest/) to create a new virtual environment using the `venv` built-in module
* then `$ source venv/bin/activate` to activate the virtual environment
* install requirements `$ pip install -r requirements.txt`
* install dev requirements `$pip install -r requirements-dev.txt`
* after that issue: `$ cp .env-sample .env` to copy `.env-sample` file to `.env` in the same directory (we're still in the project folder)
* edit the `.env` and provide your tokens inside it
* `$ source .env` source the TOKENs to expose them inside the shell, so that our bot can see them
* run `$ python tea.py`, voila the bot is working
* try using the test bot you created earlier from inside the telegram app, send some messages to it, and see how it works

## Code

* to develop a new feature/bugfix (follow our workflow):
  * fork the project to your github account
  * clone your fork locally (e.g `$git clone https://github.com/{YOUR_USER_NAME}/tearobot/`)
  * create a new branch for the feature to add / bug to fix (`$ git checkout -b new-feature_bug-branch`)
  * add your code (following our [coding-style](#Coding-Style))
  * test if it works (test on your bot you created earlier)
  * add commits with sensible messages that describe each commit clearly
  * merge your `new-feature_bug-branch` to the `dev` branch
    * make sure you're in `dev` using `$ git checkout dev`
    * then merge using `$ git merge new-feature_bug-branch`
  * push your code to github `$ git push origin dev`
  * make a pull request on my repo's `dev` branch from your `dev`

## Coding-Style

* Follow [the zen of python](https://www.python.org/dev/peps/pep-0020/)
* Max line length 119 characters
* Use `"` for strings and `"""` for docstrings. Only use `'` when you want to put `"` inside the string, or inside f-strings
* Please do not just copy code and put it here, make it pretty and consistent to our code
* we don't accept spaghetti code
* Add verbose comments to your code. It's meant for educational purposes, mainly.
