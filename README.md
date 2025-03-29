# multi-language-patient-comms
Solution for Apollo Clinic's multi-language communication strategy

# Multi-Language Patient Communication System – Apollo Clinic

## Problem
Apollo Clinic serves patients who speak Tamil, Telugu, Malayalam, Hindi, and English. Messages are sent only in English with a 35% confirmation rate. Elderly patients especially struggle.

## Solution Overview
1. **Store language preferences**
2. **Use SMS, WhatsApp, and IVR** based on age/demographics
3. **AI auto-translation + voice**
4. **Measure effectiveness with A/B testing + surveys**

## Channels
- **SMS**: All patients (in preferred language)
- **WhatsApp**: Younger patients
- **IVR Calls**: Elderly (text-to-speech in Tamil, etc.)

## AI Usage
- NLP for translation
- Voice AI for IVR calls
- Simplified text for elderly patients

## Measurement
- A/B testing (native vs English)
- Track appointment confirmations
- Survey feedback post-interaction

## Repo Structure
multi-language-patient-comms/
├── README.md
├── video_link.txt
├── channel_selector.py
├── templates/
│   ├── appointment_tamil.txt
│   ├── appointment_telugu.txt
│   ├── appointment_malayalam.txt
│   ├── appointment_hindi.txt
│   └── appointment_english.txt
└── test/
    └── test.md
