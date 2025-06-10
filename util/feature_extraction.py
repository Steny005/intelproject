# utils/feature_extraction.py

import re

def extract_features(url):
    features = []

    # Feature 1: Length of URL
    features.append(len(url))

    # Feature 2: Count of '.'
    features.append(url.count('.'))

    # Feature 3: Count of '-'
    features.append(url.count('-'))

    # Feature 4: Count of '@'
    features.append(url.count('@'))

    # Feature 5: Count of digits
    digits = sum(c.isdigit() for c in url)
    features.append(digits)

    # Feature 6: Has HTTPS
    features.append(1 if "https" in url.lower() else 0)

    # Feature 7: Count of suspicious words
    suspicious_words = ['secure', 'account', 'login', 'update', 'verify', 'password']
    count = sum(word in url.lower() for word in suspicious_words)
    features.append(count)

    return features
