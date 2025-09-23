def save_patients_to_file(patient):
    try:
        with open("patient.txt", "a") as file:
            file.write(f"{patient.name},{patient.age},{patient.gender},{patient.patient_id},{patient.disease}\n")
        print("patient enter successfully")
    except Exception as e:
        print("error saving patient",e)

def load_patients_from_file():
    patients=[]
    try:
        with open("patient.txt","r") as file:
            for line in file:
                patient_data = line.strip().split(',')
                if len(patient_data)<5:
                    print("Skipping invalid or incomplete line:", line.strip())
                    continue
                patients.append({
                    "name": (patient_data[0]),
                    "age": int(patient_data[1]),
                    "gender": (patient_data[2]),
                    "patient_id": int(patient_data[3]),
                    "disease": (patient_data[4])
                 })
    except FileNotFoundError:
        print("No patient record found")

    return patients

# p1 = Patient("Arjun", 28, "Male", 101, "Flu")
# save_patients_to_file(p1)

def save_doctors_to_file(doctor):
    with open("doctors.txt","a") as file:
        file.write(f"{doctor.name},{doctor.age},{doctor.gender},{doctor.doctor_id},{doctor.specialization}\n")

def load_doctors_from_file():
    doctors=[]
    try:
        with open("doctors.txt","r") as file:
            for line in file:
                doctor_data = line.strip().split(',')
                doctors.append({
                    "doctor_id":int(doctor_data[0]),
                    "name":doctor_data[1],
                    "age":int(doctor_data[2]),
                    "gender":doctor_data[3],
                    "disease":doctor_data[4]
                })
    except FileNotFoundError:
        print("No doctor recode found")
    return doctors

# D=Doctor("Ashwini",32,"Female",123,"Cardiology")
# save_doctors_to_file(D)
