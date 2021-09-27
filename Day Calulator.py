'''
month code
0 - January - 6 
3 - February - 0 
3 - March - 3
6 - April - 6
1 - May - 1
4 - June - 4
6 - July - 6
2 - August - 2
5 - September - 5
0 - October - 0
3 - November - 3
5 - December - 5
'''

'''
year code 
1600 - 0
1700 - 6
1800 - 4
1900 - 2
2000 - 0

if first_two_digit_of_year%4==0: year_code = 0
if first_two_digit_of_year%4==1: year_code = 6
if first_two_digit_of_year%4==2: year_code = 4
if first_two_digit_of_year%4==3: year_code = 2
'''

def daycal(d,m,y):
    if y%100==0:#cheking if year is leap or not.
        if y%400==0:
            leap=True
        else:
            leap=False
    else:
        if y%4==0:
            leap=True
        else:
            leap=False

    if leap: #month code if year is leap.
        if m==1:
            month=6
        elif m==2:
            month=0
        elif m==3:
            month=3
        elif m==4:
            month=6
        elif m==5:
            month=1
        elif m==6:
            month=4
        elif m==7:
            month=6
        elif m==8:
            month=2
        elif m==9:
            month=5
        elif m==10:
            month=0
        elif m==11:
            month=3
        elif m==12:
            month=5
    else:#month code if year is not leap.
        if m==1:
            month=0
        elif m==2:
            month=3
        elif m==3:
            month=3
        elif m==4:
            month=6
        elif m==5:
            month=1
        elif m==6:
            month=4
        elif m==7:
            month=6
        elif m==8:
            month=2
        elif m==9:
            month=5
        elif m==10:
            month=0
        elif m==11:
            month=3
        elif m==12:
            month=5

    stryr=str(y)
    first_two_digit_of_year=int(stryr[:2])
    if first_two_digit_of_year%4==0:#dividing first two digit of year by 4 and finding year code.
        year_code = 6
    elif first_two_digit_of_year%4==1:
        year_code = 4
    elif first_two_digit_of_year%4==2:
        year_code = 2
    elif first_two_digit_of_year%4==3:
        year_code = 0
    last_two_digit_of_year=int(stryr[2:])
    day_q=d+month+year_code+last_two_digit_of_year+(last_two_digit_of_year//4)#the part 1 of formula.

    day_rem=day_q%7# the part 2 of formula.

    if day_rem==1:#finding day based on results from formula
        day="Monday"
    elif day_rem==2:
        day="Tuesday"
    elif day_rem==3:
        day="Wednesday"
    elif day_rem==4:
        day="Thrusday"
    elif day_rem==5:
        day="Friday"
    elif day_rem==6:
        day="Saturday"
    elif day_rem==0:
        day="Sunday"

    if leap:#printing the results
        str_leap_year="is a leap year."
    elif not leap:
        str_leap_year="is not a leap year"
    print(f'''Day on {d}/{m}/{y} is {day}
{y} {str_leap_year}
Year Code = {year_code}
Month Code = {month}

Thank you for using my program!!
''')


date=input("Enter date (DD/MM/YYYY):")
'''21/09/2006'''
day=int(date[:2])#slicing date string into day, month, year.
month=int(date[3:5])
year=int(date[6:])

daycal(day,month,year)#running the function.