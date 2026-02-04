# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class MailActivity(models.Model):
    _inherit = "mail.activity"

    color = fields.Integer(string="Color Index", compute="_compute_color", store=True)

    @api.depends("date_deadline")
    def _compute_color(self):
        """Compute color based on deadline status."""
        today = fields.Date.context_today(self)
        for activity in self:
            if activity.date_deadline:
                if activity.date_deadline < today:
                    activity.color = 1  # Red - Overdue
                elif activity.date_deadline == today:
                    activity.color = 2  # Orange - Due today
                else:
                    activity.color = 10  # Green - Planned
            else:
                activity.color = 0  # No color
