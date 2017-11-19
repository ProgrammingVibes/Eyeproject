import webbrowser

urlPatterns={"google":"https://www.google.com.tr/search?q=",
             "wiki":"https://en.wikipedia.org/wiki/"}
def website(webdom):
    return(urlPatterns[webdom])
def siteSearch(urlPattern,query):
    url = urlPattern+query    
    webbrowser.open(url)
