import datetime
import logging

from odoo import api, fields, models

from ..helpers.calendar import compute_year_bussiness_days

_logger = logging.getLogger(__name__)


class ResourceCalendar(models.Model):
    _inherit = "resource.calendar"

    bussiness_days = fields.Integer(
        name="Bussiness Days",
        default=0,
        help="Number of bussiness days in the calendar.",
    )
    mother_calendar = fields.Boolean(
        name="Master calendar",
        default=False,
        help="Check if this calendar is intended to be replicated every month.",
    )

    from_calendar = fields.Many2one(
        "resource.calendar", string="From calendar", ondelete="cascade"
    )

    child_calendars = fields.One2many(
        "resource.calendar",
        "from_calendar",
        string="Child calendars",
        ondelete="cascade",
    )

    @api.depends("bussiness_days", "hours_per_day")
    def _compute_total_hours(self):
        for rec in self:
            rec.total_hours = rec.bussiness_days * rec.hours_per_day

    def compute_yearly_resource_calendars(self):
        year = datetime.date.today().year
        # TODO: Holidays
        holidays = []

        # Compute bussiness days per month
        monthly_bussiness_days = compute_year_bussiness_days(year, holidays)

        # Create resource calendars for month and type of calendar
        for month, bussiness_days in monthly_bussiness_days.items():
            self._create_monthly_calendars(month, year, bussiness_days)

    def _create_monthly_calendars(self, month, year, bussiness_days):
        """
        # TODO: Move to Odoo entities in order to be configurable.
        types = {
            "workshop": 8,
            "office": 7.5,
            "reduced hours": 6,
        }

        workshop_calendar_default = self.env.ref(
            "hr_attendance_mitxelena.workshop_calendar"
        )
        workshop_calendar = fields.Many2one(
            "resource.calendar", workshop_calendar.id, default=workshop_calendar_default
        )
        office_calendar_default = self.env.ref(
            "hr_attendance_mitxelena.office_calendar"
        )
        office_calendar = fields.Many2one(
            "resource.calendar", office_calendar.id, default=office_calendar_default
        )
        reduced_hours_calendar_default = self.env.ref(
            "hr_attendance_mitxelena.reduced_hours_calendar"
        )
        reduced_hours_calendar = fields.Many2one(
            "resource.calendar",
            reduced_hours_calendar.id,
            default=reduced_hours_calendar_default,
        )
        types = {
            workshop_calendar.name: workshop_calendar.hours_per_day,
            office_calendar.name: office_calendar.hours_per_day,
            reduced_hours_calendar.name: reduced_hours_calendar.hours_per_day,
        }
        """
        # Get all mother calendars and create a monthly calendar for each one
        mother_calendars = self.search([("mother_calendar", "=", True)])
        for mother_calendar in mother_calendars:
            logging.debug(
                f"Creating {mother_calendar.name} calendar for {month}/{year} "
            )
            self.env["resource.calendar"].create(
                {
                    "name": f"[{month}/{year}]: for {mother_calendar.name}",
                    "bussiness_days": bussiness_days,
                    "hours_per_day": mother_calendar.hours_per_day,
                    "from_calendar": mother_calendar.id,
                    "attendance_ids": mother_calendar.attendance_ids,
                }
            )
