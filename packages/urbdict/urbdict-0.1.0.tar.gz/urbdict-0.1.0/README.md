# urbdict
A library for [urbandictionary.com](https://www.urbandictionary.com/)

## Install:
```shell
pip install urbdict
```

## Usage:
Command line:
```shell
$ urbdict xterm
xterm

  Godly creature, omnipotent, guru in every way imaginable. 

Ex: I wish i was an xterm

 by Anonymous August 26, 2003

https://www.urbandictionary.com:443/define.php?term=xterm
```

Python:
```shell
$ python3
Python 3.9.12 (main, Jun  1 2022, 06:36:29) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import urbdict
>>> x = urbdict.define("xterm")
>>> print(x)
{'word': 'xterm', 'definition': 'Godly creature, omnipotent, guru in every way imaginable.', 'example': 'I wish i was an xterm', 'contributor': 'by Anonymous August 26, 2003', 'url': 'https://www.urbandictionary.com:443/define.php?term=xterm'}
>>> print(x["definition"])
Godly creature, omnipotent, guru in every way imaginable.
>>>  
```