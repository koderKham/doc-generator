# Documentation Generator

A Flask-based web application that generates beautiful documentation from various input formats and templates.

## Features

- 🚀 Simple and intuitive web interface
- 📝 Support for multiple documentation formats (Markdown, HTML)
- 💾 Copy to clipboard functionality
- 📱 Responsive design
- ⚡ Fast documentation generation
- 🛡️ CORS enabled for API usage
- 📤 **NEW: Upload and manage document templates**
- 🔄 **NEW: Auto-detect and configure placeholder fields**
- 📥 **NEW: Download generated documents**

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/koderKham/doc-generator.git
   cd doc-generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

## Usage

### Basic Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Generate documentation**
   - Paste your content in the input area
   - Select the documentation type (Markdown or HTML)
   - Click "Generate Documentation"
   - Copy the output using the "Copy Output" button

### Using Templates

1. **Add a Template**
   - Click the "Add Template" tab
   - Upload a .docx file with placeholders in the format `{{field_name}}`
   - The system will auto-detect all placeholders
   - Configure each field with a label and data type
   - Save the template

2. **Generate Documents from Templates**
   - Click the "Word Generator" tab
   - Select a template
   - Fill in all required fields
   - Click "Generate Word Document"
   - The document will download automatically

3. **View Generated Documents**
   - Click the "Generated Documents" tab
   - View all previously generated documents
   - Download any document again

## API Endpoints

### Template Management

#### POST /api/upload-docx-template
Upload a Word document template and extract placeholders

**Request:**
```bash
curl -X POST -F "file=@template.docx" http://localhost:5000/api/upload-docx-template
```

**Response:**
```json
{
  "success": true,
  "message": "Template uploaded successfully",
  "placeholders": ["field_name", "another_field"],
  "filename": "template.docx",
  "preview_text": "Template content preview..."
}
```

#### POST /api/save-template-from-upload
Save uploaded template with field configuration

**Request:**
```json
{
  "name": "Invoice Template",
  "description": "Professional invoice template",
  "category": "Invoices",
  "filename": "template.docx",
  "fields": [
    {"name": "invoice_number", "label": "Invoice Number", "type": "text", "required": true},
    {"name": "customer_name", "label": "Customer Name", "type": "text", "required": true}
  ]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Template saved successfully",
  "template": {...}
}
```

#### GET /api/templates
Get all active templates

**Response:**
```json
{
  "success": true,
  "templates": [
    {
      "id": 1,
      "name": "Invoice Template",
      "description": "Professional invoice template",
      "category": "Invoices",
      "fields": [...],
      "created_at": "2025-01-10T12:00:00",
      "is_active": true
    }
  ]
}
```

### Document Generation

#### POST /api/generate-document
Generate a Word document from a template

**Request:**
```json
{
  "template_id": 1,
  "filled_data": {
    "invoice_number": "INV-001",
    "customer_name": "John Doe"
  }
}
```

**Response:**
```json
{
  "success": true,
  "message": "Document generated successfully",
  "filename": "Invoice_Template_20250110_120000.docx",
  "download_url": "/api/download/1"
}
```

#### GET /api/download/<doc_id>
Download a generated document

**Response:** Binary file (Word document)

#### GET /api/documents
Get all generated documents

**Response:**
```json
{
  "success": true,
  "documents": [
    {
      "id": 1,
      "template_id": 1,
      "template_name": "Invoice Template",
      "filename": "Invoice_Template_20250110_120000.docx",
      "generated_at": "2025-01-10T12:00:00"
    }
  ]
}
```

### Legacy Endpoints

#### POST /api/generate
Generate documentation from content (legacy)

**Request:**
```json
{
  "content": "Your content here",
  "type": "markdown"
}
```

**Response:**
```json
{
  "success": true,
  "documentation": "Generated documentation..."
}
```

#### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy"
}
```

## Template Placeholder Format

Use double curly braces to define placeholders in your Word document:

```
{{field_name}}
```

### Examples:
- `{{customer_name}}`
- `{{invoice_date}}`
- `{{total_amount}}`
- `{{project_status}}`

## Project Structure

```
doc-generator/
├── app.py                    # Main Flask application
├── models.py                 # Database models (Template, GeneratedDocument)
├── word_generator.py         # Word document generation utilities
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables example
├── .gitignore               # Git ignore rules
├── templates/
│   └── index.html           # Web interface
├── uploads/                 # Uploaded template files directory
├── generated_docs/          # Generated document output directory
└── README.md                # This file
```

## Development

### Adding New Document Formats

1. Create a new generator function in `app.py`:
   ```python
   def generate_custom_docs(content):
       # Your logic here
       return formatted_content
   ```

2. Add the format to the `generate_documentation()` function

3. Update the HTML select dropdown in `templates/index.html`

### Adding New Field Types

1. Add field type handling in `templates/index.html` `generateDynamicForm()` function
2. Update backend field validation in `app.py` if needed

## Configuration

Edit `.env` to customize:

- `FLASK_ENV`: Set to `production` for deployment
- `SECRET_KEY`: Change this to a secure random key
- `MAX_CONTENT_LENGTH`: Max file upload size (default: 16MB)
- `UPLOAD_FOLDER`: Directory for uploaded templates (default: uploads)
- `DOCS_FOLDER`: Directory for generated documents (default: generated_docs)
- `DATABASE_URL`: Database connection string (default: sqlite:///doc_generator.db)

## Deployment

### Using Gunicorn (Recommended for production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t doc-generator .
docker run -p 5000:5000 doc-generator
```

## Troubleshooting

### Port 5000 already in use
```bash
python app.py --port 5001
```

### Module not found errors
Ensure your virtual environment is activated:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### Template upload fails
- Ensure the file is a valid .docx file
- Check that placeholders are in the format `{{field_name}}`
- Verify that the `uploads` directory exists and has write permissions

### Document download fails
- Check that the `generated_docs` directory exists and has write permissions
- Ensure the document hasn't been deleted from the file system

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for personal or commercial purposes

## Support

For issues and questions, please open an issue on GitHub.
