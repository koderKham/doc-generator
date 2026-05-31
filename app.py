from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOCS_FOLDER'] = 'generated_docs'

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOCS_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_docs():
    """API endpoint to generate documentation"""
    try:
        data = request.get_json()
        
        if not data or 'content' not in data:
            return jsonify({'error': 'No content provided'}), 400
        
        content = data.get('content', '')
        doc_type = data.get('type', 'markdown')
        
        # Generate documentation based on type
        generated_doc = generate_documentation(content, doc_type)
        
        return jsonify({
            'success': True,
            'documentation': generated_doc
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_documentation(content, doc_type='markdown'):
    """
    Generate documentation from input content
    
    Args:
        content (str): Input content to document
        doc_type (str): Type of documentation to generate
    
    Returns:
        str: Generated documentation
    """
    if doc_type == 'markdown':
        return generate_markdown_docs(content)
    elif doc_type == 'html':
        return generate_html_docs(content)
    else:
        return content

def generate_markdown_docs(content):
    """Generate markdown documentation"""
    # Simple implementation - can be expanded
    lines = content.split('\n')
    docs = "# Generated Documentation\n\n"
    docs += "## Overview\n"
    docs += f"{lines[0] if lines else 'No content provided'}\n\n"
    docs += "## Details\n"
    docs += "```\n" + content + "\n```\n"
    return docs

def generate_html_docs(content):
    """Generate HTML documentation"""
    html = f"""
    <html>
    <head>
        <title>Generated Documentation</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>Generated Documentation</h1>
        <pre>{content}</pre>
    </body>
    </html>
    """
    return html

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
