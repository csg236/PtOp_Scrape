import scraperwiki
import lxml.html 

html = scraperwiki.scrape("https://www.patientopinion.org.uk/feed/opinions?format=atom&tag=miscarriage&pagesize=25")     
root = lxml.html.fromstring(html)
for tr in root.cssselect("content"):
       
    try:
        website = tr.text
        print website
        
    except:
        website = "parser issue :("
  
    data = {
        'text': website
        }
    scraperwiki.sqlite.save(unique_keys=['text'], data=data)
