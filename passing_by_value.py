#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This function calculates the area of a triangle


def calculate_area(base, height):
    # calculate area

    # process
    area = base * height / 2

    # output
    print("The area is {0} cm²".format(area))


def main():
    # this function gets base and hieght

    # input
    while True:
        try:
            base_from_user = int(input("Enter the base of the triangle (cm):"))
            height_from_user = int(input(
                "Enter the height of a rectangle(cm): "))
            print("")

            # call functions
            calculate_area(base_from_user, height_from_user)
            break
        except Exception:
            print("Error")


if __name__ == "__main__":
    main()
