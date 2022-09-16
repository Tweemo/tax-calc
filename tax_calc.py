'''
Program that calculates taxes and returns the total amount of taxes.
'''

import sys

sys.tracebacklimit = 0

try:
    TAXABLE_INCOME = int(input('Enter Taxable income: '))
except ValueError:
    print("You must enter a number with no commas.")

# < $14000 = 10.5% TAX
# $14,000 < && < $48,000= 17.5% TAX
# $48,000 < && < $70,000= 30.0% TAX
# $70,000 < && < $180,000= 33.0% TAX
# $180,000 < = 39.0% TAX

FIRST_TAX_BRACKET = 14000 * 0.105
SECOND_TAX_BRACKET = FIRST_TAX_BRACKET + 34000 * 0.175
THIRD_TAX_BRACKET = SECOND_TAX_BRACKET + 22000 * 0.3
FOURTH_TAX_BRACKET = THIRD_TAX_BRACKET + 110000 * 0.33

# Check if eligible for Independent earner tax credit (IETC)
# https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc
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

TAKE_HOME_PAY =  TAXABLE_INCOME - TAX

print(f'You need to pay ${round(TAX, 2)} in taxes.')
print(f'Your take home pay is ${round(TAKE_HOME_PAY, 2)}.')
