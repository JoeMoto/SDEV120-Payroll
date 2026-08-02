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
        
        while True:
            firstName = input("First Name: ").strip()
            if firstName == "":
                print("  Error: First name cannot be blank.")
            else:
                break
            
        while True:
            lastName = input("Last Name: ").strip()
            if lastName == "":
                print("  Error: Last name cannot be blank.")
            else:
                break
            
        while True:
            employeeID = input("Employee ID: ").strip()
            if employeeID == "":
                print("  Error: Employee ID cannot be blank.")
            elif not employeeID.isdigit():
                print("  Error: Employee ID must be a number")
            else:
                break
            
        while True:
            try:
                dependents = int(input("Number of Dependents: "))
                if dependents < 0:
                    print("  Error: Dependents cannot be negative.")
                elif dependents > 20:
                    print("  Error: Number of dependents is too high please enter a number less than 20.")
                else:
                    break
            except ValueError:
                print("  Error: Please enter a whole number.")
                
        while True:
            try:
                hoursWorked = float(input("Number of hours worked: "))
                if hoursWorked < 0:
                    print("  Error: Hours cannot be negative.")
                elif hoursWorked > 60:
                    print("  Warning: Hours entered are larger than 60. This is atypical.")
                    confirm = input("  Are you sure? Enter 'yes' to accept or 'no' to re-enter: ").strip().lower()
                    if confirm == "yes":
                        break
                else:
                    break
            except ValueError:
                print("  Error: Please enter a number.")
    
        employees.append([firstName, lastName, employeeID, dependents, hoursWorked])
    return employees  
        
    
def getHourlyRate(employees):
    hourlyRateData = []
    hourlyRate = []
    
    with open("payrates.csv", "r") as file:
        file.readline()
        
        for line in file:
            line = line.strip()
            if line == "":
                continue
            columns = line.split(",")
            employee_id = columns[0]
            rate   = float(columns[3])
            hourlyRateData.append([employee_id, rate])
    
    for i in range (len(employees)):
        employeeID = employees[i][2]
        rate = 0.0
        
        for row in hourlyRateData:
            if row[0] == employeeID:
                rate = row[1]
                break
            
        if rate == 0.0:
            print("Pay rate not found for employee ID: ", employeeID)
        
        hourlyRate.append(rate)
    return hourlyRate

def getGrossPay(employees, hourlyRate):
    MAXHOURS = 40
    OVERTIME = 1.5
    grosspay = []
    
    for i in range (len(employees)):
        hours = employees[i][4]
        rate = hourlyRate[i]
        
        
        if hours <= MAXHOURS:
            gross = rate * hours
        else:
            pay = rate * MAXHOURS
            overTimePay = (hours - MAXHOURS) * (rate * OVERTIME)
            gross = pay + overTimePay
        
        grosspay.append(gross)
    return grosspay
    
def getTaxes(grossPay):
    STATETAX = .056
    FEDERALTAX = .079
    taxes = []
    
    for i in range (len(grossPay)):
        preTax = grossPay[i]
        stateTax = preTax * STATETAX
        federalTax = preTax * FEDERALTAX
        postTax = preTax - stateTax - federalTax
        
        taxes.append([preTax, stateTax, federalTax, postTax])
    return taxes
    
def getNetPay(taxes):
    netPay = []
    
    for i in range (len(taxes)):
        postTax = taxes[i][3]
        netPay.append(postTax)
    return netPay
    
def employeeOutput(employees, hourlyRate, grossPay, taxes, netPay):
    with open("payroll.csv", "w") as file:
        file.write("Employee ID,Last Name,First Name,Dependents,Hours Worked,Hourly Rate,Gross Pay,Pre-Tax Amount,State Tax (5.6%),Federal Tax (7.9%),Post-Tax Amount,Net Pay,\n")
        
        totalGross     = 0.0
        totalPreTax   = 0.0
        totalStateTax     = 0.0
        totalFederalTax   = 0.0
        totalPostTax  = 0.0
        totalNet       = 0.0
        
        for i in range (len(employees)):
            employee_id      = employees[i][2]
            lastName   = employees[i][1]
            firstName  = employees[i][0]
            dependents  = employees[i][3]
            hours       = employees[i][4]
            rate        = hourlyRate[i]
            gross          = grossPay[i]
            preTax     = taxes[i][0]
            stateTax   = taxes[i][1]
            federalTax = taxes[i][2]
            postTax    = taxes[i][3]
            net          = netPay[i]

            row = [
                employee_id,
                lastName,
                firstName,
                str(dependents),
                str(round(hours, 2)),
                str(round(rate, 2)),
                str(round(gross, 2)),
                str(round(preTax, 2)),
                str(round(stateTax, 2)),
                str(round(federalTax, 2)),
                str(round(postTax, 2)),
                str(round(net, 2)),
            ]
            file.write(",".join(row) + "\n")

            # Accumulate totals
            totalGross    += gross
            totalPreTax  += preTax
            totalStateTax    += stateTax
            totalFederalTax  += federalTax
            totalPostTax += postTax
            totalNet      += net

        totals_row = [
            "TOTALS", "", "", "", "", "",
            str(round(totalGross, 2)),
            str(round(totalPreTax, 2)),
            str(round(totalStateTax, 2)),
            str(round(totalFederalTax, 2)),
            str(round(totalPostTax, 2)),
            str(round(totalNet, 2)),
        ]
        file.write(",".join(totals_row) + "\n")

    print("Results saved to payroll.csv")

if __name__ == "__main__":
    main()