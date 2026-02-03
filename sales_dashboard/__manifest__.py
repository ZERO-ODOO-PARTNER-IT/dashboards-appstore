# -*- coding: utf-8 -*-
{
    'name': 'Sales Dashboard',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Dashboard for Sales Order Lines KPIs',
    'description': """
Sales Dashboard
===============
This module adds a Dashboard menu under Sales application.
It provides key performance indicators (KPIs) based on sale.order.line model.

Features:
---------
* Total Sales Amount
* Number of Orders
* Average Order Value
* Top Selling Products
* Sales by Status
    """,
    'author': 'The Odoo Experts',
    'website': 'https://www.yourcompany.com',
    'license': 'OPL-1',
    'price': 79,
    'currency': 'EUR',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_dashboard_views.xml',
        'views/sales_dashboard_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sales_dashboard/static/src/components/**/*',
        ],
    },
    'images': ['static/description/banner.svg'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
