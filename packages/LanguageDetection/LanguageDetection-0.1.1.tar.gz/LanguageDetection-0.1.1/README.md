# About Package
This package is developed by Mayuresh Choudhary. Its a NLP model, Package help in Language detection. It uses MultinomialNB algorithm to Detect the langauge from Text.
Different versions of packages will be released in the future.
With just three lines of code you can start detecting the Language from text for more details scroll down.

## Installation
Install my-project with pip
```bash
  pip install -i https://test.pypi.org/simple/ LanguageDetection
```
## Accessing Package
After successfull installation of "LanguageDetection" package.
```bash

  #Import Package in this way
  from LanguageDetection import LanguageDetection as lang

  #Specify the variable name as shown bellow:
  lg = lang.LanguageDetection()

  #create variable and store the result in it.
  prediction = lg.LanguageDetect("PASS THE TEXT")

  #Print the result on the screen  or just perform the operation.
  print(prediction)

  #Here in this demo, variables like lg, prediction, Lang and other are just used for demo purposes they can anything as per the requirments of the programmer.

```
## Languages
Dataset used by the Model consists of text details for 17 different languages, ie, Package can predict 17 different language...

- English
- Malayalam
- Hindi
- Tamil
- Kannada
- French
- Spanish
- Portuguese
- Italian
- Russian
- Sweedish
- Dutch
- Arabic
- Turkish
- German
- Danish
- Greek

## Authors
- Name: Mayuresh Choudhary 
- Email: mayureshchoudhary22@gmail.com
- Profile: https://myadorn.in/members/mayureshchoudhary/