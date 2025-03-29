def select_channel(patient):
    if patient["age"] > 60:
        return 'IVR'
    elif patient.get("prefers_whatsapp", False):
        return 'WhatsApp'
    else:
        return 'SMS'

def select_language(patient):
    return patient.get("language_preference") or infer_from_zip(patient["zip_code"])

def infer_from_zip(zip_code):
    regional_map = {
        "600001": "Tamil",
        "500001": "Telugu",
        "680001": "Malayalam",
        "110001": "Hindi",
    }
    return regional_map.get(zip_code, "English")
# -----------------------
# test scenarios
# -----------------------

patients = [
    {"name": "Elder Tamil Patient", "age": 72, "language_preference": "Tamil", "zip_code": "600001"},
    {"name": "Young Hindi Patient", "age": 30, "language_preference": "Hindi", "prefers_whatsapp": True, "zip_code": "110001"},
    {"name": "Middle-age Telugu", "age": 45, "zip_code": "500001"},
    {"name": "Malayalam Speaker", "age": 65, "language_preference": "Malayalam", "zip_code": "680001"},
    {"name": "Default English", "age": 40, "zip_code": "999999"}
]

for patient in patients:
    channel = select_channel(patient)
    language = select_language(patient)
    print(f"\nPatient: {patient['name']}")
    print(f"Recommended Channel: {channel}")
    print(f"Preferred Language: {language}")
