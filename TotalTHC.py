#Prompts user to enter THCa %
print ("Enter THCa percentage")
#Shows actual prompt where user enters THCa
THCa = input ("THCa Percentage:")
 #Does math to get total THCa
THCa = float (THCa) *.877
#Shows outcome of math to get total THCa %
print ("Total THCa:", THCa)
#Prompts user to enter THC %
print ("Enter THC percentage")
#Shows actual prompt where user enters THC %
THC = input ("THC Percentage:")
#Does math to add THCa and THC to get total THC %
sum = float(THCa) + float(THC)
#Shows user total THC %
print ("Total THC:", sum)
