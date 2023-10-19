
# Introduction

made by a programmer brazilian, it's a project accomplished to automate the search informations in a website, and create a sheet with that.

## Technologies


 - [Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/) A Natively browser capable make automations and execute functions as an commom user 
 - [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) A library on Python for create and manipulation of Excel spreadsheets


## Project's Description 

This project was made for automate a task than, when did by human would late many hours. This project create a bot than navigate on website collecting especify informations, as: name's item, price and discount, of all items in website, creating a spreadsheets excel and saveing the data on the table. 

## How to use 
you must download the two librarys
```bash
pip install selenium
pip install openpyxl

```
also have the browser **Google Chrome** on the compatible version with chromedriver


done this, it's necessary put the file called **chromedriver** in the same folder, with it, the next code will be capable of work.
```python
driver = webdriver.Chrome(executable_path="./chromedriver")

```
that way the script will do what was mentioned 

## Finishing 

if you followed the instructions shown previously you will have a archive **Excel** named 'automate.xlsx', with a page 'infos', over there will be the names, prices and possible discounts.

