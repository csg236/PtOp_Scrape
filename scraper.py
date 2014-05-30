import scraperwiki
import lxml.html 

html = scraperwiki.scrape("https://www.patientopinion.org.uk/feed/opinions?format=atom&tag=miscarriage")     
root = lxml.html.fromstring(html)
for tr in root.cssselect("title"):
       
    try:
        website = tr.text
        cont = root.cssselect("content")
        print website & cont
        
    except:
        website = "parser issue :("
  
    data = {
        'title' : cont,
        'text': website
        }
    scraperwiki.sqlite.save(unique_keys=['text'], data=data)
