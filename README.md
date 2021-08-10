# API automation using Python

## Introduction:
This repository contains an example of an API testing using an automate workflow for test reports. I used the pytest framework to develop the test cases and i integrated allure report features in order to give more useful, tidy and interactive test report.

## API information
The API used for this project is **Jikan**, an **Unofficial** open-source REST API of [MyAnimeList](https://myanimelist.net/). This API serves as a purpose for apps/projects that are user based and make a nominal amount of requests. 

In general, in this API you can find useful information about anime and manga, such as community scores, release dates, number of episodes / seasons, and more useful information.  

For more information visit the [official site](https://jikan.moe/) and the [API documentation](https://jikan.docs.apiary.io/#). 

## Installation
This section is focus on describe how to install the dependencies and resources to put this project to work! First of all, you need to clone this project on your own machine:  

On your terminal/Command Prompt open a folder and clone the repository:
```
$ git clone https://github.com/JhonattanReales21/API_Automation_Python.git
```

You need to install certain dependencies and packages on your machine **depending on your OS**, which are:
* Python - [Download documentation](https://www.python.org/downloads/)
* Pytest - [Installation via python](https://docs.pytest.org/en/6.2.x/getting-started.html)
* Allure - [Installation via command line](https://docs.qameta.io/allure/#_installing_a_commandline)
* Python packages such as: Jsonpath, allure, time, assertpy, requests, re.

With this resources and the repository documents, you are ready to play with the project.

## Usage

### Open the report

First, in order to take a look to the current version of the allure report, you can use the open command to see the report in a window of your browser. Execute the comand below on your terminal:

```
$ allure open {dir of the repository cloned}/Tests/allure-report
```
*Don't forget to turn off the server with ctrl + c on your terminal.*

### Add new tests and update the report

If you want to create new test suites, or even delete the tests and create new ones by you own to finally generate a new allure report, you need to take in consideration the next:
1. All your tests must follow the [guidelines](https://docs.pytest.org/en/6.2.x/getting-started.html#create-your-first-test) of pytest framework in order to be recognized as tests.
2. The results of pytest in a format that allure can interpreted, must go to a folder called allure-results.  

You can do this using the next command:

```
$ pytest --alluredir={dir of the repository cloned}/Tests/allure-results
```

3. You must generate and allure report folder using the "generate" command of allure. Everytime you create a new folder, you must clean the previous results.

```
$ allure generate allure-results -c
```
this command will generate a allure-report folder automatically. The -c Flag will clear the previous report results

4. Now, you need to open the allure report on your browser like before with:

```
$ allure open {dir of the repository cloned}/Tests/allure-report
```

5. If you want to generate trend grahps, you must follow additional steps:  
 
* The allure-report folder have a history subfolder, this one must be in the allure-results folder before generate the new allure report folder.  
* Before run the allure generate command, the allure-results folder must have **ONLY** the results of the current iteration of the tests and the history subfolder of the previous allure-report folder.

If you already have a allure-report/history subfolder, the whole flow would look like:

```
$ rm -r {dir of the repository cloned}/Tests/allure-results   #Delete the allure-results folder
$ pytest --alluredir={dir of the repository cloned}/Tests/allure-results      #Generate new allure-results
$ cp -R {dir of the repository cloned}/Tests/allure-report/history  {dir of the repository cloned}/Tests/allure-results/   #Move the history subfolder to the allure-results folder
$ allure generate allure-results -c     
$ allure open {dir of the repository cloned}/Tests/allure-report
```

# Test cases
If you want more information about the test cases, open the Tests folder.


# Resources
* https://docs.qameta.io/allure/#_get_started
* https://github.com/allure-framework/allure-python
* https://github.com/assertpy/assertpy
* https://github.com/ghoshasish99/API-Testing-Pytest




