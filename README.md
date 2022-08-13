## The Trie Project

Exploring and optimizing search suggestions with Trie (Prefix Tree)

## Purpose

- Practice Test Driven Development (TDD)
- Gain experience optimizing search performance
- Learn the ins and outs of the Trie

## Instructions

Clone the repo then setup your Python environment:

```sh
$ python3.9 -m venv env
$ python3.9 -m pip install --upgrade pip
$ source env/bin/activate
$ pip install -r requirements.txt
```

Run the Flask app:

```sh
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ flask run
```

In order to run the functional tests you will need Google Chrome installed and a Chrome webdriver matching your Chrome browser version (If you update your browser, you will will need to update your chromedriver!). You can download the webdriver here:
[Chrome Webdrivers](https://chromedriver.chromium.org/downloads)

You will need to follow the installation instructions for your specific operating system. If you are using MacOS:

```sh
$ mv path/to/your/unzipped/chromedriver /usr/local/bin
$ xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```

Run the tests (the app will need to be running for functional tests):

```sh
$ coverage run -m unittest
```

Get a test coverage report:

```sh
$ coverage report -m
$ coverage html
```

## Acknowledgements

I got the idea for this project from System Design Interview by Alex Xu. I read the book to get a good overview of how highly scalable systems operate and was not disappointed.
