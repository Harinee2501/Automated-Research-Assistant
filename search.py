from googleapiclient.discovery import build

def google_search(query,api_key,cse_id,num_results=5):
    service=build("customsearch","v1",developerKey=api_key)
    results=service.cse().list(q=query,cx=cse_id,num=num_results).execute()
    return results['items']