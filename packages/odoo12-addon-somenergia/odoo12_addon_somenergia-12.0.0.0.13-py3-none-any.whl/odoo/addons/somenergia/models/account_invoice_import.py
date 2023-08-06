from odoo import models, api
from datetime import datetime


class AccountInvoiceImport(models.TransientModel):
    _inherit = 'account.invoice.import'

    @api.model
    def _prepare_create_invoice_vals(self, parsed_inv, import_config=False):
        (vals, import_config) = (
            super()._prepare_create_invoice_vals(parsed_inv, import_config)
        )
        vals['name'] = parsed_inv.get('name')
        import_config = self.import_config_id.convert_to_import_config()
        if import_config['invoice_line_method'] == '1line_static_product':
            vals['invoice_line_ids'][0][2]['name'] = parsed_inv['name_line']
        return vals, import_config

    @api.model
    def parse_facturae_invoice(self, xml_root, xsd_file):
        parsed_inv = super().parse_facturae_invoice(xml_root, xsd_file)
#        if (
#           parsed_inv['type'] == 'out_invoice' and 
#           '86025558' in parsed_inv['partner'].get('vat')
#       ):
        invoice = xml_root.find('Invoices/Invoice')
        inv_series_code = invoice.find('InvoiceHeader/InvoiceSeriesCode').text
        parsed_inv['name'] = inv_series_code# + "/" + parsed_inv['invoice_number']
        parsed_inv['ref'] = inv_series_code
        date_orig = invoice.find('InvoiceIssueData/InvoicingPeriod/StartDate').text
        date_parsed = datetime.strptime(date_orig,'%Y-%m-%d').strftime('%m/%Y')
        parsed_inv['name_line'] = 'Energia {}'.format(date_parsed)
        return parsed_inv

