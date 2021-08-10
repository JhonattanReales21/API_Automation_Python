# Source
The funcionality of the API used is **Search**. 
The documentation of the search funcionality and the several parameters that allows can be found [here](https://jikan.docs.apiary.io/#reference/0/search). 

# Test cases developed

First, you can see more information and descriptions about the test cases generating the allure report following the steps described [before](https://github.com/JhonattanReales21/API_Automation_Python#usage).

The BDD structure designed for develop the tests is: **FEATURE -> TEST CASE -> TEST**

### Feature
The features are the main functionalities of the **Search** path, this are:
* Anime search
* Manga Search
* Advanced Search parameters

### Test case
Every feature have one or more test cases wich will help us to validate that the feature works. Which are:

###### Anime search
* As a customer i want to be able to search only Anime results.
* As a customer i want to be able to go to the Anime´s info website from the search result. 

###### Manga search
* As a customer i want to be able to search only Manga results.
* As a customer i want to be able to go to the Manga´s info website from the search result. 

###### Advanced Search parameters
* As a costumer i want to filter and order the results by specific parameters. 

### Test
The tests are designed according to the test cases, such as:

###### As a customer i want to be able to search only Anime results.
* Anime responses with none Manga observations.
* Data type for specific fields in Anime responses.

###### As a customer i want to be able to go to the Anime´s info website from the search result.
* Link and image-link for Anime responses

###### As a customer i want to be able to search only Manga results.
* Manga responses with none Anime observations.
* Data type for specific fields in Manga responses.

###### As a customer i want to be able to go to the Manga´s info website from the search result.
* Link and image-link for Manga responses

###### As a costumer i want to filter and order the results by specific parameters. 
* Verifying status filter.
* Verifying rated filter.
* Verifying order the results by score.
* Verifying order the results by id.
* Verifying several filters at the same time





