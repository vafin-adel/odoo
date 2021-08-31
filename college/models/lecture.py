# -*- coding: utf-8 -*-
from odoo import fields, models


class CourseLecture(models.Model):
    _name = "course.lecture"
    _description = "Course Lecture"

    name = fields.Char(string='Name', required=True)
    course = fields.Many2one(comodel_name="college.course", string="Course")
    description = fields.Text(string='Description')
    document = fields.Binary(string='Document')
    image = fields.Image(string='Image')
    duration = fields.Float(string='Duration')
