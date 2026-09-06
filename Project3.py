print ("\nWelcome to our time converter program \n")
str_seconds = input ("Please enter the number of seconds you want to convert: \n")
                     
int_seconds = int(str_seconds)

hours = int_seconds // 3600
rest_hours = int_seconds % 3600

minutes = rest_hours // 60
rest_minutes = rest_hours % 60

seconds = rest_minutes % 60

print ("\nThe time is: \n" +   str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")

print ("\nThank you for using our time converter program. \n")
