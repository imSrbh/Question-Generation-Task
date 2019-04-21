# Question-Generation-Task
Overall goal is to generate automatic questions from variety of inputs.



   
 # Automatic Question Generation Using NLP
 
 
 <!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [HowToUse](#howtouse)
* [Example](#example)
* [Result](#result)
* [YetToBeDone](#yettobedone)

<!-- ABOUT THE PROJECT -->
## About The Project
Automatic question generation (QG) is a useful yet challenging task in NLP. Neural network-based approaches represent the state-of-the-art in this task, but they are not without shortcomings. Firstly, these models lack the ability to handle rare words and the word repetition problem.

### Built With
Here I had used Python3 and it's Libraries.
* [Python](https://www.tecmint.com/install-python-in-ubuntu/)


<!-- GETTING STARTED -->
## Getting Started
To run the program clone the project and run this command after satisfying the requirements

### Prerequisites

<kbd>⌘Python3</kbd>
<kbd>⌘Spacy</kbd>
<kbd>⌘NumPy</kbd>
<kbd>⌘Textblob</kbd>
<kbd>⌘nltk</kbd>



## Installation

1- Python3
```
sudo apt-get install python3
```
2- SpaCy
```
   python3 -m venv .env
   source .env/bin/activate
   pip install spacy
```
   
3- NumPy 
```
sudo pip3 install numpy
```

4- Textblob 
```
sudo pip3 install textblob
```

5- nltk 
```
python3 -c "import nltk; nltk.download('all')"
```

## HowToUse
Open the repository  and Run this Command in terminal
```
python3 main.py db.txt
```
## Example
* Input
```
------INPUT TEXT------


My name is Saurabh
 
```


* Output
```
------OUTPUT Questions------


Q-01: What is your name?
Q-02: Whose name is Saurabh?
Q-03: Who is Saurabh?
```

* Input
```
Abraham Lincoln was born to Thomas and Nancy Lincoln.
```

* Output
```
Q-01: Who was born to Thomas and Nancy Lincoln?

```

## Result
[![AQG](https://github.com/imSrbh/IntelliMind-Task/blob/master/ssss.png)](https://www.youtube.com/embed/ZoJLmm5wYNc "AQG")


## YetToBeDone
```
1- web Application(Using Flask)
2- more accurate and valid Question
```
