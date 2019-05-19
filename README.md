# TBot

A toy telegram-bot built using Python. Meant for educational purposes.

[Click here to try it](https://t.me/tearobot) -- *Might not work all the time*

================================

I created this project to help myself getting better in programming with Python in the first place. Secondly, it's a college mini-project. Lastly, I wanted to make a useful bot with a bunch of handful commands and some automated messages that help me remember what I have in college today, besides the important upcoming events.

**In the future**:
I want to make it very intelligent: It should be able to talk to me ordinarily, take commands just by understanding my natural language! Also it should be able to understand my voice messages and respond to them correctly.

**On the technical side**:
Abstractly, the project should be divided into 2 parts: libraries and business logic.

One library will be more of a framework (a wrapper) on top of the Telegram APIs, it should abstract everything with Python using OOP and good design patterns. The others will be built for their purpose, like a NLP library for example. A webhook should be implemented from scratch following the telegram API specs using Django (`Channels` if possible). Those libraries should be reusable and able to be used in other projects (most likely, they will be django apps).

The business logic is specific to this bot commands, automated messages and conversation scenarios.

**Current Approach**: use long polling and build the API abstraction layer incrementally.

I try to build most of it from scratch using pure python to learn as much as possible how a project goes from tiny to huge passing by whatever stage in between.

## Currently available commands & features

* `/help` - Show help message
* `/translate` - Translate message from english to arabic
* `/weather` - Weather in `Zagazig, Egypt` now
* `/calculate` - Calculate mathematical expression
* `/tweet` - Tweet to our Twitter account
* `/ocr_url`  - extract text from image using its url
* TBot will send all of its active users a new message everyday at *08:00 AM* with the college schedule of the day

[follow this to contribute](./CONTRIBUTING.md)

## TODO

* use `master` as `upstream` and `release` for the version to be live. New workflow:
  * branch from master, code, merge on master, push
  * when you hit a release, push it to `release` branch, and use it on the server
* handle future announcements inside the bot
* make a cli for the bot to send messages or edit db stuff
* update contribution guide
* for next-stage
  * Use Postgresql instead of SQLite
  * build the webhook using Django-channels, db models using django-orm and make everything around django
