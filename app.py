from flask import Flask
from literature_discovery import literature_discovery_bp

app=Flask(__name__)

app.register_blueprint(literature_discovery_bp)

@app.route('/')
def home():
    return "Welcome to the Automated Research Assistant!"

if __name__=='__main__':
    app.run(debug=True)



