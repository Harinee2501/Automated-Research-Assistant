from flask import Blueprint, render_template, request
from transformers import pipeline
import requests
import xml.etree.ElementTree as ET

literature_discovery_bp = Blueprint('literature_discovery', __name__)
summarization_model = pipeline("summarization", model="facebook/bart-base")

def summarize_text(paper_summaries):
    # Summarizing multiple papers at once
    summaries = summarization_model(paper_summaries, max_length=130, min_length=30, do_sample=False)
    return [summary['summary_text'] for summary in summaries]

def format_citation(paper):
    return f"{paper['author']}. {paper['title']}. Published on {paper['published']}. Link: {paper['link']}"

@literature_discovery_bp.route('/literature', methods=['GET', 'POST'])
def literature():
    papers = []
    query = None
    if request.method == 'POST':
        query = request.form['query']
        url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=5'
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the XML response
            root = ET.fromstring(response.content)
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                author = ', '.join([a.find('{http://www.w3.org/2005/Atom}name').text for a in entry.findall('{http://www.w3.org/2005/Atom}author')])
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
                published = entry.find('{http://www.w3.org/2005/Atom}published').text
                link = entry.find('{http://www.w3.org/2005/Atom}id').text

                papers.append({
                    'title': title,
                    'author': author,
                    'summary': summary,
                    'published': published,
                    'link': link
                })

            # Batch summarize the papers
            summaries = summarize_text([paper['summary'] for paper in papers])
            for i in range(len(papers)):
                papers[i]['citation'] = format_citation(papers[i])
                papers[i]['summary'] = summaries[i]  # Update summary with the new summary
        else:
            papers = "Error fetching data. Please try again."

    return render_template('literature.html', papers=papers, query=query)








