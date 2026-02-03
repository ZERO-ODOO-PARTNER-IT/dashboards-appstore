/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Sales Dashboard Component
 *
 * Displays KPIs based on sale.order.line model including:
 * - Total Sales Amount
 * - Number of Orders
 * - Average Order Value
 * - Total Quantity Sold
 * - Orders by State
 * - Top Selling Products
 * - Recent Orders
 */
export class SalesDashboard extends Component {
    static template = "sales_dashboard.SalesDashboard";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");

        this.state = useState({
            dashboardData: null,
            isLoading: true,
        });

        onWillStart(async () => {
            await this.loadDashboardData();
        });
    }

    /**
     * Load dashboard data from the server
     */
    async loadDashboardData() {
        this.state.isLoading = true;
        try {
            const result = await this.orm.call(
                "sales.dashboard",
                "get_dashboard_data",
                []
            );
            this.state.dashboardData = result;
        } catch (error) {
            console.error("Error loading dashboard data:", error);
            this.state.dashboardData = {
                total_sales: 0,
                total_orders: 0,
                avg_order_value: 0,
                total_qty_sold: 0,
                orders_by_state: {},
                top_products: [],
                recent_orders: [],
            };
        }
        this.state.isLoading = false;
    }

    /**
     * Refresh dashboard data
     */
    async onRefresh() {
        await this.loadDashboardData();
    }

    /**
     * Navigate to sale orders list
     */
    viewSaleOrders() {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Sale Orders",
            res_model: "sale.order",
            view_mode: "list,form",
            views: [[false, "list"], [false, "form"]],
            target: "current",
        });
    }

    /**
     * Navigate to a specific sale order
     * @param {number} orderId - The ID of the sale order
     */
    viewOrder(orderId) {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Sale Order",
            res_model: "sale.order",
            res_id: orderId,
            view_mode: "form",
            views: [[false, "form"]],
            target: "current",
        });
    }

    /**
     * Format currency values using company currency from server
     * @param {number} value - The value to format
     * @returns {string} Formatted currency string
     */
    formatCurrency(value) {
        const currency = this.state.dashboardData?.currency;
        if (!currency) {
            return value.toFixed(2);
        }
        const formatted = value.toFixed(currency.decimal_places || 2);
        if (currency.position === 'before') {
            return `${currency.symbol}${formatted}`;
        }
        return `${formatted}${currency.symbol}`;
    }

    /**
     * Get state display name
     * @param {string} state - The state code
     * @returns {string} Display name for the state
     */
    getStateLabel(state) {
        const stateLabels = {
            'draft': 'Quotation',
            'sent': 'Quotation Sent',
            'sale': 'Sales Order',
            'done': 'Locked',
            'cancel': 'Cancelled',
        };
        return stateLabels[state] || state;
    }

    /**
     * Get CSS class for state badge
     * @param {string} state - The state code
     * @returns {string} CSS class for the badge
     */
    getStateBadgeClass(state) {
        const badgeClasses = {
            'draft': 'text-bg-secondary',
            'sent': 'text-bg-info',
            'sale': 'text-bg-primary',
            'done': 'text-bg-success',
            'cancel': 'text-bg-danger',
        };
        return badgeClasses[state] || 'text-bg-secondary';
    }
}

registry.category("actions").add("sales_dashboard", SalesDashboard);
