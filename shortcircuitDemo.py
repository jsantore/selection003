import comp151Helpers

graduation_list =  ["stu dent", "all done", "fin ished"]
student_name = input("what student do you want to check:")
lower_name = student_name.lower()
if lower_name in graduation_list or comp151Helpers.get_credits_from_database() >=120:
    print("Congrats, you are almost done!")
# the slow version
#if comp151Helpers.get_credits_from_database() >=120 or lower_name in graduation_list:
#    print("Congrats, you are almost done!")
