import webbrowser

f = open("webpage.html", "w")
f.write(htmlcode)
f.close()

# defining the url to it can open it in google chrome
url = 'file:///C:/Users/roman/Documents/GitHub/Python_Projects/webpage.html'

# this allows for the function to open the new tab with the url provided above
webbrowser.open_new(url)














    
    
    

