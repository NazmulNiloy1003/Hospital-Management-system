import random

# User class
class User:
    def __init__(self, username, password):
        self.__username = username    # Private attribute
        self.__password = password    # Private attribute
        self.__user_id = random.randint(1000, 9999)   # Generate a random user ID

    def authenticate(self, username, password):
        return username == self.__username and password == self.__password

    def get_username(self):
        return self.__username

    def get_user_id(self):
        return self.__user_id

# Patient class
class Patient(User):
    def __init__(self, username, password, name, age, contact_info, medical_history):
        super().__init__(username, password)
        self.__name = name    # Private attribute
        self.__age = age  # Private attribute
        self.__contact_info = contact_info    # Private attribute
        self.__medical_history = medical_history  # Private attribute
       
    def patient_details(self):
        return f"{self.__name}, {self.__age}"

    def update_medical_history(self, new_history):
        self.__medical_history.append(new_history)  # Updating medical history

    def get_medical_history(self):
        return self.__medical_history

    def get_details(self):
        return f"\n       ----PATIENT DETAILS----\n     \n     Name: {self.__name},     \n     Age: {self.__age},     \n     Contact Info: {self.__contact_info},     \n     Medical History: {self.__medical_history}"

# Appointment class
class Appointment:
    def __init__(self, patient, age, doctor_username, date, time):
        self.patient = patient
        self.age = age
        self.doctor_username = doctor_username
        self.date = date
        self.time = time
        self.paid = False  # Payment status

    def display_appointment(self):
        print(f"\n       ----APPIONTMENT DETAILS----\n     \n     Patient: {self.patient}\n     Doctor: {self.doctor_username}\n     Date: {self.date}\n     Time: {self.time}\n     Paid: {'Yes' if self.paid else 'No'}")

    def make_payment(self, amount):
        # Assuming a fixed fee for simplicity
        fee = 1000
        if amount == fee:
            self.paid = True
            return True
        elif amount > fee:
            rtrn = amount - fee
            self.paid = True
            print(f"\nYour extra amount {rtrn} has been returned.")  
            return True  
        else:
            print("\nFee amount is 1000!")
            return False

    def get_doctor_username(self):
        return self.doctor_username

# Doctor class
class Doctor(User):
    def __init__(self, username, password, specialty):
        super().__init__(username, password)   # Inherit from User class
        self.__specialty = specialty
        self.__appointments = []  # List to store appointments

    def get_specialty(self):
        return self.__specialty

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def view_appointments(self):
        if not self.__appointments:
            return "\nNo appointments scheduled."
        result = "\n      ----APPOINTMENTS----\n"
        for appointment in self.__appointments:
            result += f"\n     Patient: {appointment.patient},\n     Date: {appointment.date},\n     Time: {appointment.time},\n     Paid: {'Yes' if appointment.paid else 'No'}\n"
        return result

# Main function

patients = []
doctors = [Doctor('Moni', 'moni241', 'Cardiologist'),
            Doctor('Nusrat', 'nusrat221', 'Cardiologist')]
appointments = []

while True:
    print("\n                                   ++BookMyHealth++")
    print("\n                 __Simple backend of a Hospital Management System__")
    print("\n        1. Register")
    print()
    print("        2. Paitent Portal LogIn")
    print()
    print("        3. Doctor Portal LogIn")
    print()
    print("        4. Emergency service")
    print()
    print("        5. About us")
    print()
    print("        6. Media and Gallery")
    print()
    print("        7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        # Input for creating a patient
        username = input("\nEnter patient's username: ").upper()
        while True:            
            password = input("\nEnter patient's password: ")
            if len(password)>=5:
                break
            else:
                print("\nPlease enter at least 5 characters long!!")
                continue
        name = input("\nEnter patient's name: ")
        while True:
            try:
                age = int(input("\nEnter patient's age: "))
                break
            except ValueError:
                print("\n!!!Invalid input. Please enter an integer value!!!")
       
        contact_info = input("\nEnter patient's contact info: ")
        medical_history = input("\nEnter patient's medical history: ").split(',')
        patient = Patient(username, password, name, age, contact_info, medical_history)
        patients.append(patient)
        print()
        print(f"\n----Patient registered successfully!!----")
        print(f"\n----User ID: {patient.get_user_id()}-----")

    elif choice == '2':
        username = input("\nEnter your username: ").upper()
        password = input("Enter your password: ")

        logged_in_patient = None
        for patient in patients:
            if patient.authenticate(username, password):
                logged_in_patient = patient
                break

        if logged_in_patient:
            print(f"__\nWelcome, Dear {logged_in_patient.get_username()}!")
            print(f"---Your Unique ID is: {logged_in_patient.get_user_id()}!__")
           
            while True:
                print("\n        1. Book an appointment")
                print("\n        2. View medical report")
                print("\n        3. Search medical report by ID")
                print("\n        4. Test & Service charges")
                print("\n        5. Log out")
                print("\n      <-6. Go Back")


                patient_choice = input("\nEnter your choice: ")

                if patient_choice == '1':
                    while True:
                        print("\n1. Cardiologist", end='    ')
                        print("2. Neurologist")
                        print("\n3. Orthopedist", end='     ')
                        print("4. Psychiatrist")
                        print("\n5. Gynecologist", end='    ')
                        print("6. Internal Medicine")
                        print("\n7.<-Go Back")
                        print()
                                                   
                        specialist_choice = input("\nChoose a Specialist: ")

                        if specialist_choice == '1':
                           
                            while True:
                                print("\n1. Dr. Moni Akter ->", end='    ')
                                print("2. Dr. Nusrat Jahan ->")
                                print("\n3.<-Go Back")
                               
                                doctor_choice = input("\nWhom do you need an appointment with: ")
                               
                                if doctor_choice == '1':
                                    print("\n                   ---------Dr. MONI AKTER---------")
                                    print("       \nSenior Cardiologist,")
                                    print("       Highly experienced cardiologist with over 20 years in the field. \n       She specializes in complex cardiac cases and provides compassionate care.")
                                    print("\n       Graduated from Dhaka Medical College, fellowship at Cleveland Clinic from UK")
                                    print("\n       Fellow of the American College of Cardiology (FACC) \n       Member of the European Society of Cardiology (ESC) \n       Member of the Bangladesh Cardiac Society (BCS)")
                                    print("\nAvailable appoinment slot and time: ")
                                    print("        Monday - Thursday")
                                    print("        3:00PM - 7:00PM")
                                    print("\nAcppoinment fee 1000/- BDT")
                                   
                                   
                                                                           
                                    while True:
                                        print("\n1. Book an appointment")
                                        print("\n2.<-Go Back")
                                        appointment_choice = input("\nChoose an Option: ")
                                       
                                        if appointment_choice == '1':
                                            # Input for creating an appointment                                        
                                            patient_name = input("\nEnter the patient name: ")                                                                          
                                            while True:
                                                try:
                                                    age = int(input("\nEnter patient's age: "))
                                                    break
                                                except ValueError:
                                                    print("\n!!!Invalid input. Please enter an integer value!!!")
                                            date = input("\nEnter appointment date (YYYY-MM-DD): ")
                                            time = input("\nEnter appointment time (HH:MM AM/PM): ")
                                            doctor_username = "Moni"
                                            appointment = Appointment(patient_name, age, doctor_username, date, time)
                                            appointments.append(appointment)
                                            for doctor in doctors:
                                                if doctor.get_username() == doctor_username:
                                                    doctor.add_appointment(appointment)
                                            appointment.display_appointment()
                                           
                                            # Ask for payment option
                                            while True:
                                                print("\nWhich mathod you want to pay?")
                                                print("\n1. Online")
                                                print("\n2. Offline")
                                           
                                               
                                                while True:
                                                    payment_option = input("\nSelect a method: ")
                                                    if payment_option == '1':
                                                        while True:
                                                            try:
                                                                amount = float(input("\nEnter payment amount: "))
                                                                break
                                                            except ValueError:
                                                                print("\n!!!Invalid input. Please enter an integer value!!!")
                                                       
                                                        if appointment.make_payment(amount):
                                                            print("\nPayment successful!")
                                                           
                                                            break
                                                        else:
                                                            print("\nPayment failed!! Insufficient amount.")
                                                            continue
                                                    elif payment_option == '2':
                                                        print("\nYou have chosen to pay offline. Please visit the hospital reception to complete your payment.")
                                                        break
                                                    else:
                                                        print("\nInvalid payment option. Please try again.")
                                                        continue
                                                   
                                                break
                                            break
                                               
                                        elif appointment_choice == '2':
                                            break
                                        else:
                                            print("\nInvalid choice. Please try again.")
                                            continue
                                       
                                    break
                                if doctor_choice == '2':
                                    print("\n                   ---------Dr. NUSRAT JAHAN---------")
                                    print("       \nSenior Cardiologist,")
                                    print("       Highly experienced cardiologist with over 20 years in the field. \n       She specializes in complex cardiac cases and provides compassionate care.")
                                    print("\n       Graduated from Dhaka Medical College, fellowship at Cleveland Clinic from UK")
                                    print("\n       Fellow of the American College of Cardiology (FACC) \n       Member of the European Society of Cardiology (ESC) \n       Member of the Bangladesh Cardiac Society (BCS)")
                                    print("\nAvailable appoinment slot and time: ")
                                    print("        Monday - Thursday")
                                    print("        3:00PM - 7:00PM")
                                    print("\nAcppoinment fee 1000/- BDT")
                                   
                                   
                                                                           
                                    while True:
                                        print("\n1. Book an appointment")
                                        print("\n2.<-Go Back")
                                        appointment_choice = input("\nChoose an Option: ")
                                       
                                        if appointment_choice == '1':
                                            # Input for creating an appointment                                        
                                            patient_name = input("\nEnter the patient name: ")                                                                          
                                            while True:
                                                try:
                                                    age = int(input("\nEnter patient's age: "))
                                                    break
                                                except ValueError:
                                                    print("\n!!!Invalid input. Please enter an integer value!!!")
                                            date = input("\nEnter appointment date (YYYY-MM-DD): ")
                                            time = input("\nEnter appointment time (HH:MM AM/PM): ")
                                            doctor_username = "Nusrat"
                                            appointment = Appointment(patient_name, age, doctor_username, date, time)
                                            appointments.append(appointment)
                                            for doctor in doctors:
                                                if doctor.get_username() == doctor_username:
                                                    doctor.add_appointment(appointment)
                                            appointment.display_appointment()
                                           
                                            # Ask for payment option
                                            while True:
                                                print("\nWhich mathod you want to pay?")
                                                print("\n1. Online")
                                                print("\n2. Offline")
                                           
                                               
                                                while True:
                                                    payment_option = input("\nSelect a method: ")
                                                    if payment_option == '1':
                                                        while True:
                                                            try:
                                                                amount = float(input("\nEnter payment amount: "))
                                                                break
                                                            except ValueError:
                                                                print("\nInvalid input. Please enter an integer value.")
                                                        if appointment.make_payment(amount):
                                                            print("\nPayment successful!")
                                                           
                                                            break
                                                        else:
                                                            print("\nPayment failed. Insufficient amount.")
                                                            continue
                                                    elif payment_option == '2':
                                                        print("\nYou have chosen to pay offline. Please visit the hospital reception to complete your payment.")
                                                        break
                                                    else:
                                                        print("\nInvalid payment option. Please try again.")
                                                        continue
                                                   
                                                break
                                            break
                                               
                                        elif appointment_choice == '2':
                                            break
                                        else:
                                            print("\nInvalid choice. Please try again.")
                                            continue
                                       
                                    break
                                elif doctor_choice == '2':
                                    break
                                elif doctor_choice == '3':
                                    break
                                else:
                                    print("\nInvalid choice. Please try again.")
                            break
                        elif specialist_choice == '7':
                            break
                        else:
                            print("\nSpecialist option not implemented yet. Please try again.")

                elif patient_choice == '2':
                    print(logged_in_patient.get_details())

                elif patient_choice == '3':
                    while True:
                        try:
                            user_id = int(input("\nEnter User ID: "))
                            break
                        except ValueError:
                            print("\n!!!Invalid input. Please enter an integer value!!!")
                   
                    found = False
                    for patient in patients:
                        if patient.get_user_id() == user_id:
                            print(patient.get_details())
                            found = True
                            break
                    if not found:
                        print("\nPatient not found")

                elif patient_choice == '4':
                    while True:
                        print("\n        1. Available Tests ")
                        print("\n        2. Make payments ")
                        print("\n        3. <-Go Back")
                       
                        patient_choice = input("\nEnter an option: ")
                       
                        if patient_choice == "1":
                            print("\n                 ----AVAILABLE TESTS----")
                            print("\n     i. Blood tests------------------------500/- BDT")
                            print("     ii. Blood pressure measurement--------250/- BDT")
                            print("     iii. Electrocardiogram (ECG or EKG:--1000/- BDT")
                            print("     iv. Screening tests ------------------500/- BDT")
                            print("     v. X-rays -----------------------500-1000/- BDT")
                            print("     vi. CT scans ------------------------2000/- BDT")
                            print("     vii. Biopsy ---------------------500-2000/- BDT")
                            print("     viii. Urinalysis --------------------1000/- BDT")
                            print("     ix. TSH -----------------------------1500/- BDT")
                            print("     x. Glucose test ---------------------1500/- BDT")
                            print("     xi. Lipid profile ----------------300-400/- BDT")
                            print("     xii. Ultrasonography ------------700-3000/- BDT")
                            print("     xiii. MRI ---------------------------8000/- BDT")
                            while True:
                                patient_choice = input("\n<-Enter 0 to Go Back ")
                       
                                if patient_choice == "0":
                                    break
                                else:
                                    print("\nInvalid Choice!! Please Try again...")
                           
                        elif patient_choice == "2":
                            print("\nThere is no due payments!!")
                                   
                        elif patient_choice == "3":
                            break    
                        else:
                            print("\nInvalid Choice!! Please Try again...")
                               

                elif patient_choice == '5':
                    print("\nLogging out...")
                    break

                elif patient_choice == '6':
                    break

                else:
                    print("\nInvalid Choice!! Please Try again...")

        else:
            print("\nInvalid username or password!!")

    elif choice == '3':
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")

        logged_in_doctor = None

        for doctor in doctors:
            if doctor.authenticate(username, password):
                logged_in_doctor = doctor
                break

        if logged_in_doctor:
            print(f"\nWelcome, Dr. {logged_in_doctor.get_username()}! Your Unique ID is: {logged_in_doctor.get_user_id()}!")

            while True:
                print("\n1. View Appointments")
                print("\n2. Search Patient Medical History by ID")
                print("\n3. Log out")
                print("\n4.<-Go Back ")

                doctor_choice = input("Enter your choice: ")

                if doctor_choice == '1':
                    print(logged_in_doctor.view_appointments())

                elif doctor_choice == '2':
                    while True:
                        try:
                            user_id = int(input("\nEnter Patient User ID: "))
                            break
                        except ValueError:
                            print("\n!!!Invalid input. Please enter an integer value!!!")
                   
                    found = False
                    for patient in patients:
                        if patient.get_user_id() == user_id:
                            print(patient.get_details())
                            found = True
                            break
                    if not found:
                        print("\nPatient not found")

                elif doctor_choice == '3':
                    print("\nLogging out...")
                    break

                elif doctor_choice == '4':
                    break

                else:
                    print("\nInvalid Choice!! Please Try again...")

        else:
            print("\nInvalid username or password")

    elif choice == '4':
        print("         ---EMERGENCY SERVICES---")
        print("\n      Emergency Contract:")
        print("    +880123456789")
        print("    +880187654321")
        print("\n      Emergency Ambulance Service:")
        print("    +880198765432")
        print("    +880112234898")
       
    elif choice=='5':
        print("\nClick here for details about us---")
        print("\n     WWW.BookMyHealth.com")
       
    elif choice=='6':
        print("\nNot implemented yet")
        print("\n  Stay connencted.....")
           
    elif choice=='7':
        print("\nExiting...")
        break

    else:
        print("\nInvalid Choice!! Please Try again...")


