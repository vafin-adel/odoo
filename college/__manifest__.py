# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'College',
    'version': '1.0',
    'summary': '',
    'description': "",
    'depends': [],
    'category': 'Education',
    'sequence': 25,
    'demo': [],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/group.xml",
        "views/course.xml",
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
