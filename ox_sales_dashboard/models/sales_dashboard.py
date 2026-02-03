# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SalesDashboard(models.Model):
    """Model for Sales Dashboard KPIs based on sale.order.line."""

    _name = 'sales.dashboard'
    _description = 'Sales Dashboard'

    name = fields.Char(string='Name', default='Sales Dashboard')

    @api.model
    def get_dashboard_data(self):
        """Get dashboard KPI data from sale.order.line.

        Returns:
            dict: Dictionary containing KPI data for the dashboard
        """
        SaleOrderLine = self.env['sale.order.line']
        SaleOrder = self.env['sale.order']

        # Get company currency for proper formatting
        company = self.env.company
        currency = company.currency_id

        # Total sales amount using read_group for efficiency
        sales_data = SaleOrderLine.read_group(
            domain=[],
            fields=['price_subtotal:sum'],
            groupby=[],
        )
        total_sales = sales_data[0]['price_subtotal'] if sales_data else 0

        # Number of orders
        total_orders = SaleOrder.search_count([])

        # Average order value
        avg_order_value = total_sales / total_orders if total_orders else 0

        # Total quantity sold using read_group for efficiency
        qty_data = SaleOrderLine.read_group(
            domain=[],
            fields=['product_uom_qty:sum'],
            groupby=[],
        )
        total_qty_sold = qty_data[0]['product_uom_qty'] if qty_data else 0

        # Orders by state using read_group for efficiency
        state_data = SaleOrder.read_group(
            domain=[],
            fields=['state'],
            groupby=['state'],
        )
        orders_by_state = {
            'draft': 0, 'sent': 0, 'sale': 0, 'done': 0, 'cancel': 0
        }
        for record in state_data:
            state = record['state']
            if state in orders_by_state:
                orders_by_state[state] = record['state_count']

        # Top 5 selling products using read_group for efficiency
        product_data = SaleOrderLine.read_group(
            domain=[],
            fields=['product_id', 'price_subtotal:sum'],
            groupby=['product_id'],
            orderby='price_subtotal desc',
            limit=5,
        )
        top_products = []
        for record in product_data:
            if record.get('product_id'):
                top_products.append({
                    'name': record['product_id'][1],
                    'amount': round(record['price_subtotal'], 2),
                })

        # Recent orders
        recent_orders = SaleOrder.search([], limit=5, order='create_date desc')
        recent_orders_data = [{
            'id': order.id,
            'name': order.name,
            'partner': order.partner_id.name,
            'amount': order.amount_total,
            'state': order.state,
            'date': order.date_order.strftime('%Y-%m-%d') if order.date_order else '',
        } for order in recent_orders]

        return {
            'total_sales': round(total_sales, 2),
            'total_orders': total_orders,
            'avg_order_value': round(avg_order_value, 2),
            'total_qty_sold': round(total_qty_sold, 2),
            'orders_by_state': orders_by_state,
            'top_products': top_products,
            'recent_orders': recent_orders_data,
            'currency': {
                'symbol': currency.symbol,
                'position': currency.position,
                'decimal_places': currency.decimal_places,
            },
        }
