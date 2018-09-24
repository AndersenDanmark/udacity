
#To do find out the number of days between your birthday and current date


# variables
#beginning=mmddyyyy
#ending=mmddyyyy
daysInMonthLeapYear={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
daysInMonthNonLeapYear={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# determine if a year is a leap year
def isLeapYear(yearInput):
    if yearInput%4==0:

        if yearInput%100==0:

            if yearInput%400==0:
                
                return(366)
            else:
                return(365)
        else:
            return (366)
    else:
        return (365)


#Determine which calendar to use based on leap year or not
def calendarToUse(n1):
    if n1==365:
        return daysInMonthNonLeapYear
    else:
        return daysInMonthLeapYear


def daysLeftToYearEnd(date_be):

    be_Year=int(date_be[4:8])
    be_Month=int(date_be[0:2])
    be_Day=int(date_be[2:4])
    monthCount=be_Month

    daysLeftFirstMonth=calendarToUse(isLeapYear(be_Year)).get(be_Month)-be_Day
    numOfDays=daysLeftFirstMonth

    if be_Month<12:

        while monthCount<12:
            monthCount=monthCount+1

            numOfDays=numOfDays+calendarToUse(isLeapYear(be_Year)).get(monthCount)
        return numOfDays
    else:
        return numOfDays


def countDays(beginning,ending):

    #parse out the month, day, and year for beginning and ending dates
    beginningYear=int(beginning[4:8])

    endingYear=int(ending[4:8])

    #To do, count 1st year days
    numOfDays=daysLeftToYearEnd(beginning)

    #To do, count days after the 1st year and prior to the last year. days after the beginning date plus following days to the last day of the ending year

    count_year=beginningYear
    while count_year<endingYear:

        count_year=count_year+1
        numOfDays=numOfDays+isLeapYear(count_year)

    #To do, count days in the last year. subtract the days after ending date from the total number
    numOfDays=numOfDays-daysLeftToYearEnd(ending)

    return numOfDays



print(countDays('06292012','06312013'))
    
    

