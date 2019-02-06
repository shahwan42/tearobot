# To Contribute:

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
* open an issue with the feature you want to add (if it is not listed above)
* open the project folder in your code editor (e.g VS Code)
* to develop a new command/edit a current one:
    - open `commands` folder
    - create new file `your-command-name.py` OR open a current command file you want to update
    - add your code [Follow our code style](#Coding-Style)
    - import it in the main `tea.py` file
    - follow the other commands style (you should figure out this part from the code)
    - test if it's working on your test bot
    - add the command to the list above
    - make a pull request


## Coding-Style

* Follow [the zen of python](https://www.python.org/dev/peps/pep-0020/)
* Max line length 119
* Use `'` for strings and `"""` for docstrings. Only use `"` when you want to put `'` inside the string, or inside f-strings
* Please do not just copy code and put it here, make it pretty and consistent to our code
* Add verbose comments to your code. It's meant for educational purposes, mainly.
