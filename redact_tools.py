import spacy
import en_core_web_md
import pandas as pd
import re

def redact_name(text):
    nlp = en_core_web_md.load()
    doc = nlp(text)
    redacted_count = 0
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            text = text.replace(ent.text, "█" * len(ent.text))
            redacted_count += 1
    stats = f" Name              | {redacted_count}"
    return text, stats, redacted_count

def redact_email_address(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, text)
    redacted_count = 0
    for match in matches:
        name_part = match.split('@')[0]
        redacted_name = "█" * len(name_part)
        redacted_email = redacted_name + match[len(name_part):]
        text = text.replace(match, redacted_email)
        redacted_count += 1
    stats = f" Email             | {redacted_count}"
    return text, stats, redacted_count

def redact_gender(text):
    redacted_count = 0
    gender_terms = ["he", "she", "him", "her", "his", "hers", "himself", "herself"]
    for term in gender_terms:
        matches = re.findall(rf'\b{term}\b', text, flags=re.IGNORECASE)
        redacted_count += len(matches)
        text = re.sub(rf'\b{term}\b', "█" * len(term), text, flags=re.IGNORECASE)
    stats = f" Gender            | {redacted_count}"
    return text, stats, redacted_count

def redact_date(text):
    nlp = en_core_web_md.load()
    doc = nlp(text)
    redacted_count = 0
    for ent in doc.ents:
        if ent.label_ == 'DATE':
            text = text.replace(ent.text, "█" * len(ent.text))
            redacted_count += 1
    stats = f" Date              | {redacted_count}"
    return text, stats, redacted_count

def redact_phone_number(text):
    phone_pattern =r'(?:(?<=\s)|^)\(?\b\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4}\b(?:(?=\s)|$)'
    matches = re.findall(phone_pattern, text)
    redacted_count = len(matches)
    text = re.sub(phone_pattern, lambda m: "█" * len(m.group(0)), text)
    stats = f" Phone Number      | {redacted_count}"
    return text, stats, redacted_count

def redact_address(text):
    nlp = en_core_web_md.load()
    doc = nlp(text)
    redacted_count = 0
    for ent in doc.ents:
        if ent.label_ == 'GPE' or ent.label_ == 'LOC' or ent.label_ == 'FAC' or ent.label_ == 'ORG':
            text = text.replace(ent.text, "█" * len(ent.text))
            redacted_count += 1
    stats = f" Address           | {redacted_count}"
    return text, stats, redacted_count