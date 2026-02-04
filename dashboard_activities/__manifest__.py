# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Activities Dashboard",
    "version": "18.0.1.0.0",
    "category": "Productivity",
    "summary": "Dashboard for managing and tracking activities",
    "description": """
Activities Dashboard
====================
This module provides a comprehensive dashboard for managing mail activities with:
- List, Form, Kanban, and Calendar views for activities
- Dashboard overview
- Activity Types configuration
    """,
    "author": "Greemed",
    "website": "https://www.greemed.al",
    "license": "LGPL-3",
    "depends": [
        "mail",
        "board",
    ],
    "data": [
        "security/dashboard_activities_security.xml",
        "security/ir.model.access.csv",
        "views/mail_activity_views.xml",
        "views/mail_activity_type_views.xml",
        "views/dashboard_views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
}
