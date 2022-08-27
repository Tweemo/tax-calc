'''
Function to get all the invoices in a directory
Then tells you your taxable income and how much you need to pay in taxes.
'''

import os
import sys
from pdfminer.high_level import extract_text

sys.tracebacklimit = 0
PATH = os.environ.get('INVOICE_PATH')
invoices = os.listdir(PATH)
INVOICE_INCOME = []

for invoice in invoices:
    if invoice.endswith('.pdf'):
        text = extract_text(f'{PATH}/{invoice}')
        arr = text.split('\n')
        intsInArr = []
        for string in arr:
            try:
                intsInArr.append(float(string))
            except ValueError:
                pass
        INVOICE_INCOME.append(max(intsInArr))

TAXABLE_INCOME = sum(INVOICE_INCOME)
print(f'Your Taxable income is: ${TAXABLE_INCOME}')

FIRST_TAX_BRACKET = 14000 * 0.105
SECOND_TAX_BRACKET = FIRST_TAX_BRACKET + 34000 * 0.175
THIRD_TAX_BRACKET = SECOND_TAX_BRACKET + 22000 * 0.3
FOURTH_TAX_BRACKET = THIRD_TAX_BRACKET + 110000 * 0.33

IETC = 24000 <= TAXABLE_INCOME <= 44000

if TAXABLE_INCOME <= 14000:
    TAX = TAXABLE_INCOME * 0.105
elif 14000 < TAXABLE_INCOME <= 48000:
    CURRENT_TAXABLE_INCOME = TAXABLE_INCOME - 14000
    CURRENT_TAX_BRACKET = CURRENT_TAXABLE_INCOME * 0.175
    if IETC is True:
        TAX = FIRST_TAX_BRACKET + CURRENT_TAX_BRACKET - 520
    else: TAX = FIRST_TAX_BRACKET + CURRENT_TAX_BRACKET
elif 48000 < TAXABLE_INCOME <= 70000:
    CURRENT_TAXABLE_INCOME = TAXABLE_INCOME - 48000
    TAX = SECOND_TAX_BRACKET + CURRENT_TAXABLE_INCOME * 0.3
elif 70000 < TAXABLE_INCOME <= 180000:
    CURRENT_TAXABLE_INCOME = TAXABLE_INCOME - 70000
    TAX = THIRD_TAX_BRACKET + CURRENT_TAXABLE_INCOME * 0.33
else:
    CURRENT_TAXABLE_INCOME = TAXABLE_INCOME - 180000
    TAX = FOURTH_TAX_BRACKET + CURRENT_TAXABLE_INCOME * 0.39

print(f'You need to pay ${round(TAX, 2)} in taxes.')
