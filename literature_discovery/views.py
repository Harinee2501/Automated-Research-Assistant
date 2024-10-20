from flask import Flask, render_template, request, Blueprint
import requests
import xml.etree.ElementTree as ET
from .summarizer import summarize_text  # Import the summarize_text function

# Initialize the Blueprint for literature discovery
literature_discovery_bp = Blueprint('literature_discovery', __name__)

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

                # Summarize the paper's summary
                summarized_summary = summarize_text(summary)

                papers.append({
                    'title': title,
                    'author': author,
                    'summary': summarized_summary,
                    'published': published,
                    'link': link
                })
        else:
            papers = "Error fetching data. Please try again."

    return render_template('literature.html', papers=papers, query=query)

# Initialize the Flask app
app = Flask(__name__, template_folder='literature_discovery/templates')  # Specify the template folder

# Register the blueprint
app.register_blueprint(literature_discovery_bp)

if __name__ == '__main__':
    app.run(debug=True)

