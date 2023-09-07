# Takes in a time as a raw integer, 0 - 86399, and a format to output
# The time output is a string for each digit, so 12:28 will be "1228"
# If the time is in regular format, return a tuple
#       Item 1 of the tuple is the digits string
#       Item 2 is a boolean for whether it is am or pm
# If the format is military time, just return the digits string
def format_time(time):

    # number of seconds when it is mid-day (12:00:00 PM)
    MID_DAY = 43200

    # Conditions on whether it's past mid-day or not
    am = time < MID_DAY
    
    HOUR = 3600 # Number of seconds in an hour
    MINUTE = 60 # Number of seconds in a minute
    HOUR_MID_DAY = 12 # For non-military format

    # Extract the largest round number of hours within the raw time
    output_hour = time // HOUR
    # Take that many hours (in seconds) off the raw time
    time -= output_hour*HOUR 

    # Format hour (i.e., if output_hour was 13, set it to 1)
    output_hour = output_hour % HOUR_MID_DAY
    # If the hour is 0, replace it with 12. Done without conditionals for efficiency
    # This is done only for standard format
    output_hour = (output_hour == 0)*12 + (output_hour != 0)*output_hour

    # Extract the largest round number of minutes
    output_minute = time // MINUTE

    # Output string
    out = ""

    # The smallest number that creates at least two digits
    TWO_DIGITS = 10

    # Add the hour to our output
    out += str(output_hour) + ""

    # Add the minutes to our output, padd a 0 if necessary
    out += "0"*(output_minute < TWO_DIGITS) + str(output_minute)

    return (out, am)