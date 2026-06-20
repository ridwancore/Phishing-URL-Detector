import re
from urllib.parse import urlparse

def has_ip_address(url):
    pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return 1 if re.search(pattern, url) else 0

def extract_features(url):
    parsed = urlparse(url)

    features = {
        "url_length": len(url),
        "hostname_length": len(parsed.netloc),
        "path_length": len(parsed.path),
        "count_dots": url.count('.'),
        "count_hyphen": url.count('-'),
        "count_at": url.count('@'),
        "count_question": url.count('?'),
        "count_percent": url.count('%'),
        "count_equal": url.count('='),
        "count_http": url.count('http'),
        "count_https": url.count('https'),
        "count_www": url.count('www'),
        "digit_count": sum(c.isdigit() for c in url),
        "letter_count": sum(c.isalpha() for c in url),
        "has_ip": has_ip_address(url),
    }

    return list(features.values())