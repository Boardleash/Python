##################################
### TITLE: rent-calc.py        ###
### AUTHOR: Boardleash (Derek) ###
### DATE: Monday, July 7 2025  ###
##################################
#
###################
### DESCRIPTION ###
###################
#
# A simple Python rent calculator that will ask income questions and make
# income breakdown calculations based on those questions.
# Tested on Python 3.13.53.53.5

print("Hello, I can perform some basic income calcualtions for you.")
print("In order to do this, I will ask you two questions.  Please exclude commas from your input.")
print("For example, rather than type 70,000.00, please type 70000.00.")
try:
  annual = float(input("What is your ANNUAL income?  If you do not know, enter '0': "))
  hourly = float(input("What is your HOURLY income?  If you do not know, enter '0': "))
except:
  print("Input must be numerical.  Exiting now.")
else:
  if annual == 0 and hourly == 0:
    print("You have no income to calculate")
  elif annual == 0:
    biweekly = round((hourly * 80),2)
    monthly = round((biweekly * 2),2)
    annual = round((monthly * 12),2)
    monthly_rent = round(((annual * 0.30) / 12),2)
    print("Based solely on your HOURLY income, here is the layout of your income, excluding taxes:")
    print()
    print("$" +str(biweekly)+ " BIWEEKLY (every two weeks)")
    print("$" +str(monthly)+ " MONTHLY")
    print("$" +str(annual)+ " ANNUAL")
    print("Using the 30% rule, you can afford $" +str(monthly_rent)+ " in rent a month.")
    print()
  elif hourly == 0:
    monthly = round((annual / 12),2)
    biweekly = round((monthly / 2),2)
    hourly = round((biweekly / 80),2)
    monthly_rent = round(((annual * 0.30) / 12),2)
    print("Based solely on your ANNUAL income, here is the layout of your income, excluding taxes: ")
    print()
    print("$" +str(monthly)+ " MONTHLY")
    print("$" +str(biweekly)+ " BIWEEKLY (every two weeks)")
    print("$" +str(hourly)+ " HOURLY")
    print("Using the 30% rule, you can afford $" +str(monthly_rent)+ " in rent a month.")
    print()

# EOF
