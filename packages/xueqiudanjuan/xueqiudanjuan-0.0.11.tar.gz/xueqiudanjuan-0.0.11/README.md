# Warning
This package only for personal use under the rules of XueQiu.
Please obey the rules of XueQiu, and do not take the bad influence for the XueQiu website.

# General Information
This is a Python package designed by BugMakerH, which is used for getting the data on the XueQiu website.
You can import this package using:
```python
import xueqiudanjuan
```

# How to use this package
## hello.py
#### hello()
- This function is nothing but a test for checking whether the package works well.
## stocks.py
### Stock
This is a class to get data about stocks.
You can create a Stock class using:
```python
st = stocks.Stock()
```
This means to create a Stock object.
And, you can use 'get_realtime_quotec()' to get the real price of a specified stock. Like this:
```python
st.get_realtime_quotec("SH000001")
```


# Update documentation
## 0.0.11
- Deleted the function 'get_realtime_quotec_prize' in the class 'Stock'.
## 0.0.10
- Update the import in '\_\_init\_\_'.
## 0.0.9
- Updated the test of stocks.py in '\_\_main\_\_'.
- Added the import of all the files in '\_\_init\_\_'.
## 0.0.8
- Updated the url of long description.
## 0.0.7
- Updated the url of long description.
## 0.0.6
- Added the Github URL of the package.
- Remove the stock's code from the '\_\_init\_\_' function to the 'get_realtime_quotec' function.
## 0.0.5
- Updated nothing, cuz I deleted the version 0.0.4 by mistake.
## 0.0.4
- Created the README file and added the README file to the package.
- Linked the package's long description to the README file.
## 0.0.3
- Created the class engine and the class stocks.
- Finished the first version of the class engine.
- Added a function of the class stocks, which is called 'get_realtime_quotec' to get the realtime price of the specified stocks.
- Added a test of the class stocks in the '\_\_main\_\_'.
## 0.0.2
- Updated nothing, but a joke.
## 0.0.1
- Added a test for the package, which added a file called "hello.py" with a function called "hello".