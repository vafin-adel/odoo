# -*- coding: utf-8 -*-
from odoo import fields, models


class CollegeGroup(models.Model):
    _name = "college.group"
    _description = "College Group"

    name = fields.Char(string='Name', required=True)
