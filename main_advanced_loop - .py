"""
HomeWork#6
This is Exercise in Advanced
written by Eyal Lev
Date March 29st 2019
"""

MAX_RAW=50                                       # Max Raw Limit
MAX_COL=100                                      # Max Column Limit
def draw_table (raw,col):
    if raw> MAX_RAW or col> MAX_COL:             # In case the Number of raw and/or column are out of limits return False
        return False
    for raw_index in range(1,2*(raw+1)):         # external loop running on the raws
        if raw_index%2==1:                       # if the raw number is odd :
            for col_index in range(1,2*(col+1)):  #run in internal loop all over the ccolumn
                if col_index<2*col+1:             # if the number is not the last-->  end of line then print w/o newline
                   print ("=",end="")
                else:
                    print("=")                     # if the column is the last print "="  with newline
        else:                                      # if raw number is even then :
            for col_index in range(1,2*(col+1)):   #run in internal loop all over the ccolumn
                if col_index%2==1 and col_index<2*col+1: #   if the number is not the lastand nor end of line end of line then print w/o newline
                   print ("|",end="")
                elif col_index==2*col+1:
                    print("|")
                else:
                 print (" ",end="")                # if the column number is even print spce
    return True


if (draw_table(40,80)):
    print("")
else:
    print ("Raw and/or Column are out of Screen MAX Limits")
