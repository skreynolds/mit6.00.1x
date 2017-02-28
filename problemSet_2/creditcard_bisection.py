balance = 999999;
annualInterestRate = 0.18;

def creditCardBalance(minPayment, balance, monthlyInterestRate):
    for i in range(12):
        balance -= minPayment;
        balance += monthlyInterestRate*balance;
    return balance;
    
monthlyInterestRate = annualInterestRate/12.0;
monthlyLowerBound = balance/12;
monthlyUpperBound = (balance*(1 + monthlyInterestRate)**12)/12.0;
epsilon = 0.01;

while(True):
    
    minPayment = 0.5*(monthlyLowerBound + monthlyUpperBound);
    unpaidBalance = creditCardBalance(minPayment,
                            balance, monthlyInterestRate);
    
    if (abs(unpaidBalance) < epsilon):
        print('Lowest Payment: ' + str(round(minPayment,2)));
        break
    elif (unpaidBalance > 0):
        monthlyLowerBound = minPayment;
    else:
        monthlyUpperBound = minPayment;