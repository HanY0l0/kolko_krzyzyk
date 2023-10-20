def get_menu_option():
    while True:
        level = input(
            "Choose game mode:\n1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI\n")
        if level == "1":
            return int("1")
            break
        elif level == "2":
            return int("2")
            break
        elif level == "3":
            return int("3")
            break
        elif level == "4":
            return int("4")
            break
        else:
            print("No such game mode, try again!")


    '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
    '''




if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 