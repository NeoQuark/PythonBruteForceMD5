## PythonBruteForceMD5

This repository is a simple set of some files that allow you to explore password cracking with **Python 2.7** using **brute force** and **dictionary attack**. The point of such scripts is to show the ease in cracking passwords if we use a password dictionary.

*Note that I only used it on MD5 hash, but it may work with other hash algorithms if you want **(you only have to add the possibility to manipulate other algorithms)***

## Usage example

First of all, note that you may require *"inquirer"* to run the script called **hashtool.py**. Also, it could be tricky to a beginner to install inquirer through Anaconda.

Let's say we want to add a user + password combination and then, we want to use hash comparison so we can retrieve password from hash using dictionary attack.

We run hashtool.py and select *"Set user + password"* and then, we will setup user and password consecutively. After that, we will select *"Find a password from MD5 hash"* and select a user the user whose password we want to find. Then, the script will test each password in the dictionary by comparing the user hash and the current password hash until we find similar hash.

## Files

You will find a total of 6 files wich include 3 main scripts :

* **brute** : One of the main scripts that crack passwords using brute force
* **dicAttack** : One of the main scripts that crack passwords using dictionary attack
* **dico_mini_fr** : Passwords dictionary used for experiences
* **hashtools** : One of the main scripts that manipulate hash to make new user + pwd combination and crack passwords using dictionary attack
* **passwords** : Password + user list with time spent to reveal the corresponding password
* **shadow** : Example of a shadow file like the one you can find on Linux distributions that stores users and corresponding password hash.
