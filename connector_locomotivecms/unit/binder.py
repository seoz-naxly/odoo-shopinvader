# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.addons.connector.connector import Binder


class LocomotiveBinder(Binder):
    "Base Binder for locomotive"
    _openerp_field = 'record_id'
