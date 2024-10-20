import requests
from flask import render_template,request,Blueprint

from . import literature_discovery_bp

@literature_discovery_bp.route('/literature',methods=['GET','POST'])
def literature():
    papers=None
    query=None
    if request.method=='POST':
        query=request.form['query']
        url=f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=5'
        response=requests.get(url)

        if response.status_code==200:
            papers=response.text

        else:
            papers="Error fetching data. Please try again"

    return render_template('literature.html',papers=papers,query=query)