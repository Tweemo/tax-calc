'''
Function to loop through all the invoices in a directory
'''

import os

PATH = os.environ.get('INVOICE_PATH')

invoices = os.listdir(PATH)

for invoice in invoices:
    if invoice.endswith('.pdf'):
        print(invoice)
