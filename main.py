from hospital import Patient, Doctor, Hospital
import records
import database

def main():
    hospital = Hospital()
    database.create_table()
    saved_patients = records.load_patients_from_file()
    hospital = Hospital()
    # database.create_table()
    for patients_data in saved_patients:
        patient = Patient(
            name=patients_data["name"],
            age=patients_data["age"],
            gender=patients_data["gender"],
            patient_id=patients_data["patient_id"],
           disease=patients_data["disease"]
        )
        hospital.add_patient(patient)

    while True:
        print("\n1. Add patient details")
        print("2. Add doctor details")
        print("3. view patient's details")
        print("4. view doctor's details")
        print("5. Exit")

        option=int(input("Enter option: "))

        if option==1:
            name = input("Enter patient name: ")
            age = int(input("Enter Age: "))
            gender =input("Enter gender: ")
            disease = input("Enter disease: ")
            patient=Patient(name,age,gender,len(hospital.patients)+1,disease)
            hospital.add_patient(patient)
            database.add_patients_to_db(name,age,gender,disease)
            records.save_patients_to_file(patient)

        elif option==2:
            name=input("Enter doctors name: ")
            age=int(input("Enter age: "))
            gender=input("Enter gender: ")
            specialization=input("Enter specialization: ")
            doctor=Doctor(name,age,gender,specialization,len(hospital.doctors)+1)
            hospital.add_doctor(doctor)
            database.add_doctors_to_db(name,age,gender,specialization)
            records.save_doctors_to_file(doctor)

        elif option==3:
            print("Patients in system")
            for patient in database.get_all_patients():
                print(patient)

        elif option==4:
            print("Doctors in system")
            for doctor in database.get_all_doctors():
                print(doctor)

        elif option==5:
            break

if __name__=="__main__":
    main()