#project1 : School Administration Program


import csv

def write_into_csv(info_list):
    with open('student_in.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "City", "State","Contact Number", "Email id","Other"])

        writer.writerow(info_list)

        
if __name__ == '__main__':
    condition = True

    while(condition):
        Student_in = input("Enter some Student info as follows [name.age,city,state,contact_number,emial_id,other]")
        print(Student_in)

            #split function
        Student_in_list = Student_in.split(' ')
        print("Entered spilt information is :" + str(Student_in_list))

        print("\n The entered information is -\n Name:- {}\n Age: {}\n City: {}\n State: {}\n Contact_Number: {}\n Email_id: {}\n Otehr: {}\n".format(Student_in_list[0],
                    Student_in_list[1],Student_in_list[2],Student_in_list[3],Student_in_list[4],Student_in_list[5],Student_in_list[6]))

        choice_check = input("Is this information is correct? (yes/no):")
        if choice_check == "yes":
            write_into_csv(Student_in_list)

            condition_check = input("Enter (yes/no) if you want to enter information for the another student:")
            if condition_check == 'yes':
                condition = True
            elif condition_check == 'no':
                condition = False
        elif choice_Check == "no":
            print("\n Please reenter the values:")
