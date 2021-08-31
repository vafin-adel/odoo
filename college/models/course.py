# -*- coding: utf-8 -*-
from odoo import fields, models


class CollegeCourse(models.Model):
    _name = "college.course"
    _description = "College Course"

    name = fields.Char(string='Name', required=True)
    lectures = fields.One2many(comodel_name="course.lecture", inverse_name="course", string = "Lectures")