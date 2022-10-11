import comp151Helpers

graduation_list = ["stu dent", "All Done", "Fin Ished"]
name = input("What is the student’s name")
if name in graduation_list or comp151Helpers.get_credits_from_database(name) > 120 :
    print("Congrats!!!! you are eligible for graduation!!")
else:
    print(f"sorry, with  you can't graduate yet")