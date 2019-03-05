import QuantLib as ql

'''
Input Bond Terms

'''
par = 100
coupon_rate = .0725
issueDate = ql.Date(23,4,2014)
maturityDate = ql.Date(15,5,2022)

'''
adding call schedule
***I suspect there is a simpler better way to do this***
'''

callability_schedule = ql.CallabilitySchedule()
call_price = 103.88
call_date = ql.Date(15,ql.April,2019);
null_calendar = ql.NullCalendar();
for i in range(0,12):
    callability_price  = ql.CallabilityPrice(
        call_price, ql.CallabilityPrice.Clean)
    callability_schedule.append(
            ql.Callability(callability_price, 
                           ql.Callability.Call,
                           call_date))

    call_date = null_calendar.advance(call_date, 3, ql.Months)
    
'''
Create the schedule
'''

issueDate = issueDate
maturityDate = maturityDate
tenor = ql.Period(ql.Quarterly)
calendar = ql.UnitedStates()
businessConvention = ql.Unadjusted
dateGeneration = ql.DateGeneration.Backward
monthEnd = False
schedule = ql.Schedule (issueDate, maturityDate, tenor, calendar, businessConvention,
                            businessConvention , dateGeneration, monthEnd)

###Coupon stream
dayCount = ql.Actual360()
couponRate = coupon_rate
coupons = [couponRate]