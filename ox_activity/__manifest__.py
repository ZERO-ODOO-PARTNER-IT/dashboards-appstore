# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Activities",
    "version": "18.0.1.0.0",
    "category": "Productivity",
    "summary": "Dashboard for managing and tracking activities",
    "description": """
Activities
==========
This module provides a comprehensive dashboard for managing mail activities with:
- List, Form, Kanban, and Calendar views for activities
- Reporting and analytics
- Activity Types configuration
    """,
    "author": "The Odoo Experts",
    "website": "https://www.theodooexperts.com",
    "license": "OPL-1",
    "depends": [
        "mail",
        "board",
    ],
    "data": [
        "security/ox_activity_security.xml",
        "security/ir.model.access.csv",
        "views/mail_activity_views.xml",
        "views/mail_activity_type_views.xml",
        "views/dashboard_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
    "price": 29,
    "currency": "EUR",
}
