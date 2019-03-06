# To Contribute:

## Install

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

## code

* to develop a new feature/fixbug (follow our workflow):
    1. fork the project
    2. clone your fork locally
    3. create a new branch (e.g new-feature-branch)
    4. add some code (following our coding-style) and commits with sensible messages that descirbe each commit clearly
    5. push your new-feature-branch to your fork on github (`$ git push origin new-feature-branch`)
    6. create a Pull Request (using github web interface)
        the source is your YourFork/new-feature-branch and the destination is myRepo/dev branch


## Coding-Style

* Follow [the zen of python](https://www.python.org/dev/peps/pep-0020/)
* Max line length 119
* Use `'` for strings and `"""` for docstrings. Only use `"` when you want to put `'` inside the string, or inside f-strings
* Please do not just copy code and put it here, make it pretty and consistent to our code
* Add verbose comments to your code. It's meant for educational purposes, mainly.

