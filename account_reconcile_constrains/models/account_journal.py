##############################################################################
#
#    Copyright (C) 2016 Compassion CH (http://www.compassion.ch)
#    Releasing children from poverty in Jesus' name
#    @author: Jérémie Lang <jlang@compassion.ch>
#
#    The licence is in the file __manifest__.py
#
##############################################################################

from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AccountJournal(models.Model):
    _inherit = "account.journal"

    excluded_account_ids = fields.Many2many(
        'account.account', string='Excluded Accounts',
        domain="[('company_id', '=', company_id)]", check_company=True
    )
