'''
Get income from invoices.
'''

from pdfminer.high_level import extract_text

text = extract_text('sample-invoice.pdf')

arr = text.split('\n')
intsInArr = []

for string in arr:
    try:
        intsInArr.append(float(string))
    except ValueError:
        pass

print(max(intsInArr))
