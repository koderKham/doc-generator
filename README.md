# Documentation Generator

A Flask-based web application that generates beautiful documentation from various input formats.

## Features

- 🚀 Simple and intuitive web interface
- 📝 Support for multiple documentation formats (Markdown, HTML)
- 💾 Copy to clipboard functionality
- 📱 Responsive design
- ⚡ Fast documentation generation
- 🛡️ CORS enabled for API usage

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

## API Endpoints

### POST /api/generate
Generate documentation from content

**Request:**
```json
{
  "content": "Your content here",
  "type": "markdown"  // or "html"
}
```

**Response:**
```json
{
  "success": true,
  "documentation": "Generated documentation..."
}
```

### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy"
}
```

## Project Structure

```
doc-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Web interface
├── uploads/              # Uploaded files directory
├── generated_docs/       # Generated documentation directory
└── README.md             # This file
```

## Development

To add new documentation formats:

1. Create a new generator function in `app.py`:
   ```python
   def generate_custom_docs(content):
       # Your logic here
       return formatted_content
   ```

2. Add the format to the `generate_documentation()` function

3. Update the HTML select dropdown in `templates/index.html`

## Configuration

Edit `.env` to customize:

- `FLASK_ENV`: Set to `production` for deployment
- `SECRET_KEY`: Change this to a secure random key
- Max file size limits
- Upload/output folders

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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - feel free to use this project for personal or commercial purposes

## Support

For issues and questions, please open an issue on GitHub.
