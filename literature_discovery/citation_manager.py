def format_citation(paper):
    authors = paper['author'] if paper['author'] else "Unknown Author"
    title = paper['title'] if paper['title'] else "Untitled"
    published = paper['published'] if paper['published'] else "No Date"
    
    return f"{authors}. {title}. {published}. Available at: {paper['link']}."



