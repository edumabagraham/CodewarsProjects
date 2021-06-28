# filters
# filter(function, iterable)  The filter() method constructs an iterator from elements of an iterable for which a function returns true.

##########-------------Filter with normal function-----------------############

# days = ( 'Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Sat' , 'Sun' )
# # for a in days:
# #      print(a)
#
#
# def letsFilter(days):
#      weekEnd = ('Sat','Sun')
#
#      if(days in weekEnd):
#           return True
#      else:
#           return False
#
# letsFilter = filter(letsFilter,days)
# print('Weekends:\n')
# for weekEnd in letsFilter:
#      print(weekEnd)



#################-----------Filter with LAMBDA------------------####################


def letsFilterwithLambda(days, weekEnd):
    for b in weekEnd:
        if b in days:
            days = remove_all_weekend(days)
    return days


def remove_all_weekend(days):
    return tuple(filter(lambda a: a in weekEnd, days))


days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
weekEnd = ('Sat', 'Sun')

print(letsFilterwithLambda(days, weekEnd))
