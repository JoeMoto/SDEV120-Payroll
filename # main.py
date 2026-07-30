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
        employeeID = input("Employee ID: ")
        dependents = int(input("Number of Dependents: "))
        hoursWorked = float(input("Number of hours worked: "))
    
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
                f"{hours:.2f}",
                f"{rate:.2f}",
                f"{gross:.2f}",
                f"{preTax:.2f}",
                f"{stateTax:.2f}",
                f"{federalTax:.2f}",
                f"{postTax:.2f}",
                f"{net:.2f}",
            ]
            file.write(",".join(row) + "\n")

            # Accumulate totals
            totalGross    += gross
            totalPreTax  += preTax
            totalStateTax    += stateTax
            totalFederalTax  += federalTax
            totalPostTax += postTax
            totalNet      += net

        # Write totals row
        totals_row = [
            "TOTALS", "", "", "", "", "",
            f"{totalGross:.2f}",
            f"{totalPreTax:.2f}",
            f"{totalStateTax:.2f}",
            f"{totalFederalTax:.2f}",
            f"{totalPostTax:.2f}",
            f"{totalNet:.2f}",
        ]
        file.write(",".join(totals_row) + "\n")

    print(f"  Results saved to {"payroll.csv"}")

if __name__ == "__main__":
    main()