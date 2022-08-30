from multiprocessing.connection import answer_challenge
from ssl import Options
import requests
from bs4 import BeautifulSoup
import re
import string


URL = "https://www.itexams.com/exam/AZ-900"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="q_collapse show")

def seperate_options(list,question,answers):
 

    print(question)
    option_array=[]

    for o in list:
        str = o.text.strip()
        option_array.append(str)
        print(str)
    # push to a list in a model
    list = answers

    answers_array=[]

    for a in list:
        str = a.text.strip()
        str_arr = str.split("\n")
        answer = str_arr[1]
        exp = str_arr[4]
        answers_array.append(f'Answer: {answer}\n')
        print(str)



for x in job_elements:
    question = x.find("div", class_="question_text").getText()

    #add to 
    options = x.find_all("ul", class_="choices-list list-unstyled")
   
    answers = x.find_all("div", class_="answer_block green accent-1")
    user_input = ""
    seperate_options(options,question,answers)




#print(f'Question:\n{type(question)}----------\nOptions:\n{options}----------\nAnswer:\n{answer}')




# for q in question:
#     print(q.text.strip())

    
# Output
# iwanther

# for a in answers:
#     print(a.text.strip())




#Get question, options, answer, user select, result+

# # importing required modules 
# import PyPDF2 
    
# # creating a pdf file object 
# pdfFileObj = open('example.pdf', 'rb') 
    
# # creating a pdf reader object 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# # printing number of pages in pdf file 
# print(pdfReader.numPages) 
    
# # creating a page object 
# pageObj = pdfReader.getPage(0) 
    
# # extracting text from page 
# print(pageObj.extractText()) 
    
# # closing the pdf file object 
# pdfFileObj.close() 