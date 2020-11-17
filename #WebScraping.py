import requests
"""pip install requests"""
from bs4 import BeautifulSoup
"""pip install beautiful soup"""
v =  requests.session()
"""Stars a requetst session using the callable variable of < v >, you would make all the future requests to the site using the same varibale"""

i = v.get("https://www.footlocker.co.uk/en/homepage",allow_redirects=False)
"""Here we make a <GET> request to the site ast we are GETTING INFORMATION, the < i > is used so we can call this request later"""

soup = BeautifulSoup(i.content, 'html.parser')
"""Here we call the Beautiful Soup Module to start scraping the html from the website. as you can see the < i > from the < i.content > is from the request. this is 
    the most efficient way of telling beautiful soup to look in the request assigned to the letter < i >"""

print(soup)
"""We now print the information beautiful soup retried from the site, this can be know as thye inner html or in some cases the backend source code of the site, now from the parsed html
    we can try and get the Synchroniser Token, this being one of many antibot methods put in place by footlocker"""
"""google this link    view-source:https://www.footlocker.co.uk/en/homepage    then press ctrl+f and type in SynchronizerToken, you will see a link looking like this"""

"""<input type="hidden" name="SynchronizerToken" value="f336f26416c886fcfee5af0a1383bef1903707986e7b953ad9148946bbe57b85"/>"""

"""At the start we have an input tag, this refers to the line which the token is. Then we have the name, this refers to name of the item on the line. Now we have the value, which 
    which is what we want to extract. The hexadecimal code next to Value is the token that we need to scrape in order to act like the request we make using code is like the one 
    a normal client would make on the site"""

html_input = soup.find_all('input')
"""here we cask soup to find all the lines with input in them and we name this command < html_input > so we can call it later"""

print(html_input)
"""Here we are asking beautiful soup to find all the lines with < input > in them, and to print them out (Before you re run the code put a <#> in front of the previous print statement)
    Now run the code"""

"""In python you count from 0 so when all the input tags are printed out you should count all the input from 0 until you find one similar to the one 4 above. it should be number 1 in
    terms of python"""

token = soup.find_all('input')[1]
"""As we know the input tage we need is number one we can simply write < [1] > next to the statement like the one above, now write a < # > next to the above print statement and the html_input
    as we dont need to run those lines"""
print(token)
"""This will now print the line where the token is located, you should get something similar to this:"""
"""<input name="SynchronizerToken" type="hidden" value="382db44460ce8f5fa35704ec3f77ef9ef373e6236dbfc5e1251cda8ef7bfc985"/>"""

SynchronizerToken = token['value']
print(SynchronizerToken)
"""This is the final line as we can now see the line in which the token is located in we just need to specify that we want whats written next to the < value > statement
    we do this by using the variable < token > which we assigned to < token = soup.find_all('input')[1] >. the statement < SynchronizerToken = token['value'] > now tells beautiful
    soup to look in the input line number 1 then look at the < value > statement, then print the string of hexadecimal code assigned to it, now run the code and make sure all the 
    print statements other than the last have a < # > in front of them as we only want one thing being the < SynchronizerToken >"""
