from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import csv
import xlwt
import xlrd
import re
from xlwt import Workbook 



app = Flask(__name__)

@app.route('/', methods=['POST'])
def my_form_post():
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1') 
    url = request.form['text']
    file = request.form['text2']
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    row = 0
    for item in soup.find_all("div", attrs={"class": "product-item"}):
        brand = item.find("h3", attrs={"class": "product-name"})
        brand = brand.text.upper()
        sheet1.write(row, 0, brand)
        row+=1
    wb.save(file + ".xls")
    return render_template("index.html",**locals())
    
    

@app.route("/")
def home():
    return render_template("index.html",**locals())


    


    
if __name__ == "__main__":
    app.run(debug=True)




