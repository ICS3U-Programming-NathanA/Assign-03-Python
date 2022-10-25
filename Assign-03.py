# Created by: Nathan Araujo
# Created on: Oct 19 2022
# This program asks the user for their age, it then tells them if their allowed to vote

import constants


def main():

    # Get the users age
    country_string = input("Enter 1 for Canada, 2 for Austria or 3 for Bahrain: ")
    user_age_string = input("Enter your age: ")
    # An try catch to catch any errors if they enter a string for country_string
    try:
        country_num = int(country_string)
    except Exception:
        print("Enter either 1, 2 or 3 for the countries")
        play_again_string = input(
            "To play again type 1 otherwise type any other number: "
        )
    else:
        if country_num < constants.NEGATIVE:
            print("Please enter a positive number")
            play_again_string = input(
                "To play again type 1 otherwise type any other number: "
            )
        # An If statement to see if the user can vote in Canada
        if country_num == constants.CANADA:
            try:
                # A try catch to catch if they entered a string for the users age
                user_age = int(user_age_string)
            except Exception:
                print("Please enter a number a whole number")
                play_again_string = input(
                    "To play again type 1 otherwise type any other number: "
                )
            else:
                # A if statement to see if the number is a negative
                if user_age < constants.NEGATIVE:
                    print("Please enter a positive number")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                # A Elif statement to see if the users age is greater than or equal to 18 and is less than or equal to 122
                elif (
                    user_age >= constants.MIN_AGE_CANADA
                    and user_age <= constants.MAX_AGE
                ):
                    print("Your allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                else:
                    print("Your not allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
        # If statement to see if you can vote in Austria
        elif country_num == constants.AUSTRIA:
            # A try catch to catch if they entered a string for the users age
            try:
                user_age = int(user_age_string)
            except Exception:
                print("Please enter a number a whole number")
                play_again_string = input(
                    "To play again type 1 otherwise type any other number: "
                )
            else:
                # A if statement to see if the number is a negative
                if user_age < constants.NEGATIVE:
                    print("Please enter a positive number")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                # A Elif statement to see if the users age is greater than or equal to 16 and is less than or equal to 122
                elif (
                    user_age >= constants.MIN_AGE_AUSTRIA
                    and user_age <= constants.MAX_AGE
                ):
                    print("Your allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                else:
                    print("Your not allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
        # If statement to see if you can vote in Bahrain
        elif country_num == constants.BAHRAIN:
            # A try catch to catch if they entered a string for the users age
            try:
                user_age = int(user_age_string)
            except Exception:
                print("Please enter a number a whole number")
                play_again_string = input(
                    "To play again type 1 otherwise type any other number: "
                )
            else:
                # A if statement to see if the number is a negative
                if user_age < constants.NEGATIVE:
                    print("Please enter a positive number")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                # A Elif statement to see if the users age is greater than or equal to 20 and is less than or equal to 122
                elif (
                    user_age >= constants.MIN_AGE_BAHRAIN
                    and user_age <= constants.MAX_AGE
                ):
                    print("Your allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )
                else:
                    print("Your not allowed to vote")
                    play_again_string = input(
                        "To play again type 1 otherwise type any other number: "
                    )

    # try catch to catch if they entered a string for the loop question
    finally:
        try:
            play_again_num = int(play_again_string)
        except Exception:
            print("Please enter a number a whole number")
        else:
            # An if statement to see if they entered 1
            if play_again_num == constants.YES:
                main()
            else:
                print("Thanks for playing")


if __name__ == "__main__":
    main()
