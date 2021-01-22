# -*- coding: utf-8 -*-
from odoo import fields, models


class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    name = fields.Char(string='Name', required=True)
    birthday = fields.Date(string='Birthday')
    country = fields.Many2one('res.country', 'Country')
    group = fields.Many2one("college.group", string="Group")
