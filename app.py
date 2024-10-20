from flask import Flask, request, render_template, jsonify,send_file
from dotenv import load_dotenv
from search import google_search
from wiki import fetch_wikipedia_data
from scrape import fetch_webpage_content
from pdf_generator import generate_pdf
import os

load_dotenv()

app=Flask(__name__)

api_key=os.getenv('GOOGLE_API_KEY')
cse_id=os.getenv('CSE_ID')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    query=request.form.get('query')
    length_preference=request.form.get('length','short')
    wikipedia_summary=fetch_wikipedia_data(query,length_preference)
    google_results=google_search(query,api_key,cse_id)

    if not google_results:
        return jsonify({"error":"No Google search results found."}), 404
    
    first_result_content=fetch_webpage_content(google_results[1]['link'])
    pdf_file_path=generate_pdf(wikipedia_summary,first_result_content)

    if not pdf_file_path:
        return jsonify({"error":"Failed to generate PDF"}),500
    
    return jsonify({
        "wikipedia_summary":wikipedia_summary,
        "webpage_content":first_result_content[:500],
        "pdf_file":pdf_file_path
    })

@app.route('/download/<filename>',methods=['GET'])
def download(filename):
    return send_file(filename,as_attachment=True)
if __name__ =='__main__':
    app.run(debug=True)



