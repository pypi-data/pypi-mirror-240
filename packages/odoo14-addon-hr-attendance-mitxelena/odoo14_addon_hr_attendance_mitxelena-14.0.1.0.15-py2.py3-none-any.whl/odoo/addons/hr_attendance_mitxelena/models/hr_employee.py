from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    mother_calendar_id = fields.Many2one(
        "resource.calendar",
        domain="[('mother_calendar', '=', True)]",
        string="Shift Calendar",
        required=True,
    )

    def button_preview_attendance_report(self):
        self.ensure_one()
        context = dict(self.env.context, default_employee_id=self.id)
        return {
            "name": "Select Month for Report",
            "type": "ir.actions.act_window",
            "res_model": "attendance.report.wizard",
            "view_mode": "form",
            "view_id": self.env.ref(
                "hr_attendance_mitxelena.view_attendance_report_wizard_form"
            ).id,
            "target": "new",
            "context": context,
        }
