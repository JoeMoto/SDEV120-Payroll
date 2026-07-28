# main.py
# Payroll Program

def main():
    employees = []
    
    print("Employee Payroll System\n")
    employees = employeeInput()
    hourlyRate = getHourlyRate(employees)
    grossPay = getGrossPay(employees, hourlyRate)
    taxes = getTaxes(grossPay)
    netPay = getNetPay(taxes)
    employeeOutput(employees, hourlyRate, grossPay, taxes, netPay)
    
    
    
    
def employeeInput():
    employees = []
    numOfEmployees = 10
    
    for i in range (1, numOfEmployees + 1):
        print("Please enter the information for employee number: ", i)
        
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        employeeID = int(input("Employee ID: "))
        dependents = int(input("Number of Dependents: "))
        hoursWorked = float(input("Number of hours worked: "))
    
        employees.append([firstName, lastName, employeeID, dependents, hoursWorked])
    return employees  
        
    
def getHourlyRate(employees):
    hourlyRate = []
    
    for i in range (1, len(employees) + 1):
        employeeID = employees[i][2]
        
        #database query to get rate
        
        #hourlyRate.append(rate)
    return hourlyRate

def getGrossPay(employees, hourlyRate):
    grosspay = []
    
    for i in range (1, len(employees) + 1):
        hours = employees[i][4]
        rate = hourlyRate[i]
        # gross =
        
        #grosspay.append(gross)
    return grosspay
    
def getTaxes(grossPay):
    taxes = []
    for i in range (1, len(grossPay) + 1):
        preTax = grossPay[i]
        # get stateTax
        # get federalTax
        # get postTax
        
        #taxes.append([preTax, stateTax, fedralTax, postTax])
    return taxes
    
def getNetPay(taxes):
    netPay = []
    
    for i in range (1, len(taxes) + 1):
        postTax = taxes[i][3]
        #get employee net pay
        #netPay.append(emplyeeNetPay)
    return netPay
    
def employeeOutput(employees, hourlyRate, grossPay, taxes, netPay):
    # output results and record into spreadsheet
    return

if __name__ == "__main__":
    main()