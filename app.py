from flask import Flask
from literature_discovery.views import literature_discovery_bp

# Initialize the Flask app
app = Flask(__name__, template_folder='literature_discovery/templates')

# Register the blueprint
app.register_blueprint(literature_discovery_bp)

if __name__ == '__main__':
    app.run(debug=True)






