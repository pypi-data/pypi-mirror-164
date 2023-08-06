**This module is in alpha test!**
hi my name is mani, and i want to show you what you can do with 'ChorusFruit' python module
***This module is a replacement for curses module***
# Tutorial:
### Installation
****
first `pip install --upgrade py-getch` and then
you can just `pip install --upgrade ChorusFruit`
or for source code You can download source code from [my Github](https:\\github.com\mani_farizi)
### TUI Screen
****
##### First 'Hello World!'
Hello World is Very Simple
```python 
#Importing module
import ChorusFruit
scr = ChorusFruit.Screen()
#Outputing on Screen with Y of 0 and x of 0
scr.write(0, 0, 'Hello World!')
#That means in First Line and First Column Type 'Hello World!'
```
or
```python 
#Importing module
import ChorusFruit
def main(self)
    #Outputing on Screen with Y of 0 and x of 0
    self.write(0, 0, 'Hello World!')
    #That means in First Line and First Column Type 'Hello World!'
main(ChorusFruit.screen())
#This Line Runs the Code
```
If You Want to print in Last Line you can 
```python 
self.write(None, None, 'Hello World!')
```
But If you Want to print on a X and Y you can
```python
self.write(X, Y, 'Hello World!')
```
##### Boxes and Lines
For crating a border around the screen you can
```python
self.boxborder('┌─┐││└─┘')
# With this Code You can Create a Border But if you resize the screen the code is not working corect
#for making it better you can
import ChorusFruit
def main(self):
    while True:
        self.boxborder('┌─┐││└─┘')
        self.reset()
main(ChorusFruit.screen())
#This Code is Working Fine
```
```text
┌─────────────────────────────────────────────────────┐
│                                                     │
│                                                     │
│                                                     │
│                                                     │
│                                                     │
│                                                     │
└─────────────────────────────────────────────────────┘
```
it Works like this
For crating a box you can
```python
import ChorusFruit
def main(self):
        self.box(0, 1, 10, 10, '┌─┐││└─┘')
main(ChorusFruit.screen())
```
This Code Returns this
```text
┌────────┐
│        │
│        │
│        │
│        │
│        │
│        │
│        │
│        │
└────────┘
```
For crating a Vertical line use:
```python
Screen().vLine(0, 1, 5)
```
For crating a Horizontal line use:
```python
Screen().hLine(0, 1, 5)
```
##### Others
Moving UP
```python
scr.UP()
```
Moving DOWN
```python
scr.DOWN()
```
Clearing Screen
```python
scr.clear()
```
Writing a text with color
```python
self.write(0, 0, 'This text is RED', 'fore_red')
```
getting a Character
```python
ch = self.getch()
```
getting a Character without echo
```python
ch = self.getch(no_echo=True)
```
### Coffee
Calculate Numbers and Strings with eval but secure
```python
Coffee().calc('2+2')
```
Return a GET Request Text
```python
Coffee().get_request_text('https://www.example.com')
```
Find a String Between Two Strings
```python
Coffee().find_between('Atext123Btext', 'Atext', 'Btext')
#This Code Returns '123'
```
### dotconf
Gets the Config file in Working Directory and Save it in Variable "Conf"
like:
.Conf:
```json5
int: Integer = 1
str: String = "this is a String"
bool: Boolean = true
list: String_list = {"hi", "hello", "hii"}
```
main.py:
```python
from ChorusFruit import dotconf
conf = dotconf()
print(conf.Conf)
```
output of python:
```js
{'Integer': 1, 'String': 'this is a String', 'Boolean': True, 'String_list': ['hi', 'hello', 'hii']}
```
## and so much More in the Future