def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE
    
    if day+1>30:
        day=1
        
        if month+1>12:
            month=1
            year=year+1
        else:
            month=month+1
    else:
        day=day+1
    return (year,month,day)


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
       
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False 



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second. Assertation added for date order"""
        
    # YOUR CODE HERE!
    assert(dateIsBefore(year1, month1, day1, year2, month2, day2)==True),"the first date is not before the second date!"
    
    dayCount=1
    currentDay=nextDay(year1,month1,day1)
    while currentDay[0]<year2:
        currentDay=nextDay(currentDay[0],currentDay[1],currentDay[2])
        dayCount=dayCount+1
    while currentDay[1]<month2:
        currentDay=nextDay(currentDay[0],currentDay[1],currentDay[2])
        dayCount=dayCount+1
    while currentDay[2]<day2:
        currentDay=nextDay(currentDay[0],currentDay[1],currentDay[2])
        dayCount=dayCount+1
   
    return dayCount

def test():
    """This is a test function for the daysBetweenDates function"""
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print ("Test with data:", args, "failed")
            else:
                print ("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print ("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print ("Check your work! Test case {0} should not raise AssertionError!\n".format(args))   
test()
