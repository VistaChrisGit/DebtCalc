# 6.00 PS1-A Solution
# Determines remaining credit card balance after a year of making the minimum payment each month

balance = float(input("Enter the outstanding balance on your credit card: "))
annualInterestRate = float(input("Enter the annual credit card interest rate as a decimal: "))
minMonthlyPaymentRate = float(input("Enter the minimum monthly payment rate as a decimal: "))

# Monthly Interest Rate
monthlyInterestRate = annualInterestRate/12

# Initialize state variables
numMonths = 1
totalAmtPaid = 0

while numMonths <= 12:
    # Minimum monthly payment of balance at start of the month
    minPayment = round(minMonthlyPaymentRate * balance,2)
    totalAmtPaid += minPayment
    
    # Amt of monthly payment that goes to interest
    interestPaid = round(monthlyInterestRate * balance,2)
    
    # Amt of principal paid off
    principalPaid = minPayment - interestPaid
    
    # Subtract monthly payment from outstanding balance
    balance -= principalPaid
    
    print("Month:", round(numMonths, 2))
    print("Minimum monthly payment:", round(minPayment, 2))
    print("Remaining balance:", round(balance, 2))
    print()
    
    # Count this as a new month     
    numMonths += 1

print("RESULT")
print("Total amount paid:",round(totalAmtPaid, 2))
print("Remaining balance:",round(balance, 2))
        
        
    
    

