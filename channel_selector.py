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
