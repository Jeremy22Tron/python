Name = input('Name: ')
print("Hello " + Name +
      "! We are going to find out how long you have been alive!")
Age = int(input('How old are you? '))
print('You are ' + str(Age) + ' years old.')
Months = Age * 12
#12 is the number of months in a year
Days = Age * 365
#365 is the number of days in a year
Minutes = Age * 525948
Seconds = Age * 31556926
print(Name + ' has been alive for about: ' +
      str(Months) + ' months or ' + str(Days) + ' days '
       + str(Minutes) + ' minutes and ' + str(Seconds) + ' seconds! ')



