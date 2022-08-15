inp = int(input("Enter time in seconds : "))
i = inp//60
hours = i//60
min = i - (hours*60)
sec = inp - ((hours*3600)+(min*60))
print(hours , "Hours, ", min, "Minutes and ", sec,"Seconds.")