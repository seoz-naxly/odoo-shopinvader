# -*- coding: utf-8 -*-
# Copyright 2020 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def reset_price_tax(self):
        """
        Inherit to apply the promotion rules when prices are updated
        :return:
        """
        result = super(SaleOrder, self).reset_price_tax()
        if self.has_promotion_rules:
            self.apply_promotions()
        return result
