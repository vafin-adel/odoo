# -*- coding: utf-8 -*-
from odoo import fields, models


class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    name = fields.Char(string='Name', required=True)
    birthday = fields.Date(string='Birthday')
    country = fields.Many2one('res.country', 'Country')
    group = fields.Many2one("college.group", string="Group")
    phone = fields.Text(string="Phone")
    mail = fields.Text(string="Email")
    image = fields.Image(string='Image')
    state = fields.Selection(
        string='State',
        selection=[
            ('enrollee', 'Enrolle'),
            ('student', 'Student'),
            ('alumnus', 'Alumnus'),
            ('expelled', 'Expelled'),
        ],
        default='enrollee'
    )
