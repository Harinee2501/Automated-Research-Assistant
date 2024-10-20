from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    if not text:
        return "No summary available."
    # Generate the summary
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def format_citation(paper):
    return f"{paper['author']} ({paper['published'][:4]}). {paper['title']}. Available at: {paper['link']}"

