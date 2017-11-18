import webbrowser

def openGoogle(query):
    url = "https://www.google.com.tr/search?q="+query    
    webbrowser.open(url)
