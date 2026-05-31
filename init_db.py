"""Initialize the database with sample templates"""
from app import app, db
from models import Template
import json

def init_database():
    """Create database and add sample templates"""
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✓ Database tables created")
        
        # Check if templates already exist
        if Template.query.first():
            print("✓ Templates already exist")
            return
        
        # Sample templates
        templates = [
            {
                'name': 'Project Report',
                'description': 'Professional project status report template',
                'category': 'Reports',
                'fields': [
                    {'name': 'project_name', 'type': 'text', 'label': 'Project Name', 'required': True},
                    {'name': 'report_date', 'type': 'date', 'label': 'Report Date', 'required': True},
                    {'name': 'project_manager', 'type': 'text', 'label': 'Project Manager', 'required': True},
                    {'name': 'status', 'type': 'select', 'label': 'Project Status', 'options': ['On Track', 'At Risk', 'Off Track'], 'required': True},
                    {'name': 'summary', 'type': 'textarea', 'label': 'Project Summary', 'required': True},
                    {'name': 'completed_tasks', 'type': 'textarea', 'label': 'Completed Tasks', 'required': False},
                    {'name': 'upcoming_tasks', 'type': 'textarea', 'label': 'Upcoming Tasks', 'required': False},
                    {'name': 'risks_issues', 'type': 'textarea', 'label': 'Risks & Issues', 'required': False}
                ],
                'template_content': """# {{project_name}} - Project Report

**Report Date:** {{report_date}}
**Project Manager:** {{project_manager}}
**Status:** {{status}}

## Project Summary
{{summary}}

## Completed Tasks
{{completed_tasks}}

## Upcoming Tasks
{{upcoming_tasks}}

## Risks & Issues
{{risks_issues}}
"""
            },
            {
                'name': 'Meeting Minutes',
                'description': 'Template for documenting meeting minutes',
                'category': 'Meetings',
                'fields': [
                    {'name': 'meeting_title', 'type': 'text', 'label': 'Meeting Title', 'required': True},
                    {'name': 'meeting_date', 'type': 'date', 'label': 'Meeting Date', 'required': True},
                    {'name': 'attendees', 'type': 'textarea', 'label': 'Attendees', 'required': True},
                    {'name': 'agenda', 'type': 'textarea', 'label': 'Agenda', 'required': True},
                    {'name': 'discussion', 'type': 'textarea', 'label': 'Discussion Points', 'required': True},
                    {'name': 'decisions', 'type': 'textarea', 'label': 'Decisions Made', 'required': False},
                    {'name': 'action_items', 'type': 'textarea', 'label': 'Action Items', 'required': False},
                    {'name': 'next_meeting', 'type': 'date', 'label': 'Next Meeting Date', 'required': False}
                ],
                'template_content': """# {{meeting_title}} - Meeting Minutes

**Date:** {{meeting_date}}

## Attendees
{{attendees}}

## Agenda
{{agenda}}

## Discussion
{{discussion}}

## Decisions
{{decisions}}

## Action Items
{{action_items}}

**Next Meeting:** {{next_meeting}}
"""
            },
            {
                'name': 'Invoice',
                'description': 'Professional invoice template',
                'category': 'Finance',
                'fields': [
                    {'name': 'invoice_number', 'type': 'text', 'label': 'Invoice Number', 'required': True},
                    {'name': 'invoice_date', 'type': 'date', 'label': 'Invoice Date', 'required': True},
                    {'name': 'client_name', 'type': 'text', 'label': 'Client Name', 'required': True},
                    {'name': 'client_address', 'type': 'textarea', 'label': 'Client Address', 'required': True},
                    {'name': 'items', 'type': 'textarea', 'label': 'Items/Services', 'required': True},
                    {'name': 'subtotal', 'type': 'text', 'label': 'Subtotal', 'required': True},
                    {'name': 'tax', 'type': 'text', 'label': 'Tax', 'required': True},
                    {'name': 'total', 'type': 'text', 'label': 'Total Amount', 'required': True},
                    {'name': 'due_date', 'type': 'date', 'label': 'Due Date', 'required': True},
                    {'name': 'company_name', 'type': 'text', 'label': 'Company Name', 'required': True}
                ],
                'template_content': """# INVOICE

**Invoice #:** {{invoice_number}}
**Date:** {{invoice_date}}

## Bill To:
{{client_name}}
{{client_address}}

## Items/Services:
{{items}}

## Summary
- Subtotal: {{subtotal}}
- Tax: {{tax}}
**Total: {{total}}**

**Due Date:** {{due_date}}

**From:** {{company_name}}
"""
            }
        ]
        
        # Add templates to database
        for template_data in templates:
            template = Template(
                name=template_data['name'],
                description=template_data['description'],
                category=template_data['category'],
                fields=template_data['fields'],
                template_content=template_data['template_content']
            )
            db.session.add(template)
        
        db.session.commit()
        print(f"✓ Added {len(templates)} sample templates")
        print("\nAvailable templates:")
        for template in Template.query.all():
            print(f"  - {template.name}")

if __name__ == '__main__':
    init_database()
