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

Run the Flask app for testing:

```sh
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ flask run
```

Setup your Javascript testing environment (note this is not necessary for the application to work):

```sh
$ npm install
```

You will need to uncomment the "require" and "module.exports" lines in your script.js file for the unittests to run (the actual app will not work with these uncommented!).
Run the Javascript unittests:

```sh
$ npm test
```

In order to run the functional tests you will need Google Chrome installed and a Chrome webdriver matching your Chrome browser version (If you update your browser, you will will need to update your chromedriver!). You can download the webdriver here:
[Chrome Webdrivers](https://chromedriver.chromium.org/downloads)

You will need to follow the installation instructions for your specific operating system. If you are using MacOS:

```sh
$ mv path/to/your/unzipped/chromedriver /usr/local/bin
$ xattr -d com.apple.quarantine /usr/local/bin/chromedriver
```

You will need to comment the "require" and "module.exports" lines in your script.js file for the functional tests to run. The Flask app will also need to be running for the functional tests to work.
Run the Python tests:

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
