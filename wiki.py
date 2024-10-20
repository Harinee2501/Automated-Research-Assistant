import wikipediaapi #provides functions to retrieve wikipedia pages and their contents.
import re
import os
def fetch_wikipedia_data(topic,length='short'): #function to fetch data from wikipedia based on the given topic
  user_agent = os.getenv('USER_AGENT')
  wiki_wiki=wikipediaapi.Wikipedia(language='en',user_agent=user_agent) #wiki_wike- object that allows to interact with wikipedia (specifically english version'en', wikipediaapi lib has funcs to help fetch pages,summaries and other content, Wikipedia is a class)
  page=wiki_wiki.page(topic) #page() retrieves the page data and store it in page (page function creates an object of other class called Page that has title summary method etc)
  if page.exists():
      summary=page.summary
      if length=='short':
        max_length=500
        truncated_summary=summary[:max_length]
        last_period=truncated_summary.rfind('.')
        if last_period!=-1:
          truncated_summary=truncated_summary[:last_period+1]
        final_summary=truncated_summary
      else:
        final_summary=summary
      points=re.split(r'(?<=[.!?])+',final_summary)
      formatted_summary='\n'.join(f"-{point.strip()}" for point in points if point.strip())
      return formatted_summary
  else:
      print("Wikipedia page doesn't exist")
      return None