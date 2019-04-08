# To Contribute

## Install

> On a Linux System (figure out how to do it on windows yourself):

* you need the `telegram` app installed on your desktop/mobile, obviously!
* then make sure you have `git` and `python(v3.6+)` installed on your system
* create a Bot on Telegram to test on. [see how](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* clone the repo `$ git clone https://github.com/ash753/tearobot/`
* go to project folder `$ cd tearobot`
* `$ python -m venv venv` create a [virtualenv](https://virtualenv.pypa.io/en/latest/)
* rename the `.env-sample` file to `.env` and provide your tokens inside it
* `$ source venv/bin/activate` activate the a virtual environment
* `$ source .env` source the TOKENs to expose them
* run `$ python tea.py`
* try using the test bot you created earlier

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
  * push your code to github
  * make a pull request on my repo's `dev` branch

## Coding-Style

* Follow [the zen of python](https://www.python.org/dev/peps/pep-0020/)
* Max line length 119 characters
* Use `'` for strings and `"""` for docstrings. Only use `"` when you want to put `'` inside the string, or inside f-strings
* Please do not just copy code and put it here, make it pretty and consistent to our code
* we don't accept spaghetti code
* Add verbose comments to your code. It's meant for educational purposes, mainly.
