"""
File: Ackerman.py
-------------------------------
This program calculates the Ackerman and Ackerman Percentage for the designed Steering Geometry
"""

import math
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# Enter your values here to iterate tha Ackerman Geometry
# Wheel Base and Track Front are in inches
# Angles are in degree
wheel_base = 54
track_front = 48.645669
theta_out_degree = 35.45
theta_in_degree = 63.53


def main():
    # Converting the angles is degree to radians
    theta_out_radians = theta_out_degree * (math.pi / 180)
    theta_in_radians = theta_in_degree * (math.pi / 180)

    # Calculating the Ackerman
    Ackerman_denominator = float((wheel_base / math.tan(theta_out_radians)) - track_front)
    Ackerman_numerator = float(wheel_base)
    Ackerman_ratio = float(Ackerman_numerator / Ackerman_denominator)
    Ackerman = math.degrees(math.atan(Ackerman_ratio))

    # Calculating the Ackerman Percentage
    Ackerman_percentage_numerator = theta_out_degree - theta_in_degree
    Ackerman_percentage_denominator = theta_out_degree - Ackerman
    Ackerman_percentage = (Ackerman_percentage_numerator / Ackerman_percentage_denominator) * 100

    # Printing the results
    print("Ackerman: " + str(Ackerman))
    print("Ackerman Percentage: " + str(Ackerman_percentage))

    # Appending the data to a text file
    file = open('Ackerman Iterations.txt', 'a+')
    file.write('\n')
    file.write(str(now))
    file.writelines(['\nWheel Base: ' + str(wheel_base), '\nTrack Front: ' + str(track_front),
                     '\nOuter Angle: ' + str(theta_out_degree), '\nInner Angle: ' + str(theta_in_degree)])
    file.writelines(['\nAckerman :' + str(Ackerman), '\nAckerman Percentage: ' + str(Ackerman_percentage)])
    file.write('\n')
    file.close()


# This provided line is required at the end of Python file to call the main() function
if __name__ == "__main__":
    main()
