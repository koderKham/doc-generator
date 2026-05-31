from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Template(db.Model):
    """Template model for storing document templates"""
    __tablename__ = 'templates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False, default='General')
    fields = db.Column(db.JSON, nullable=False)  # JSON array of field definitions
    template_content = db.Column(db.Text, nullable=False)  # Template structure with placeholders
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'fields': self.fields,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'is_active': self.is_active
        }
    
    def __repr__(self):
        return f'<Template {self.name}>'


class GeneratedDocument(db.Model):
    """Generated document model for tracking generated documents"""
    __tablename__ = 'generated_documents'
    
    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey('templates.id'), nullable=False)
    template_name = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    filled_data = db.Column(db.JSON, nullable=False)  # Data used to generate the document
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    file_path = db.Column(db.String(512), nullable=True)
    
    template = db.relationship('Template', backref='generated_documents')
    
    def to_dict(self):
        return {
            'id': self.id,
            'template_id': self.template_id,
            'template_name': self.template_name,
            'filename': self.filename,
            'filled_data': self.filled_data,
            'generated_at': self.generated_at.isoformat(),
        }
    
    def __repr__(self):
        return f'<GeneratedDocument {self.filename}>'
