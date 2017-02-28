balance = 103;
annualInterestRate = 0.25;

monthlyInterestRate = annualInterestRate / 12.0;
monthlyUnpaidBalance = balance;
minimumFixedPayment = 10;

while(True):
    
    # Reset balance to original amount
    monthlyUnpaidBalance = balance;
    
    # Determine if the balance will be paid off
    for i in range(1,13):
        monthlyUnpaidBalance -= minimumFixedPayment;
        monthlyUnpaidBalance += monthlyInterestRate*monthlyUnpaidBalance;
        #print('Month: ' + str(i) + '   ' + 'Balance: '
        #            + str(monthlyUnpaidBalance));
    
    if (monthlyUnpaidBalance > 0):
        # Increase the monthly payment by 10
        minimumFixedPayment += 10;
    else:
        break       
print('Lowest Payment: ' + str(minimumFixedPayment));