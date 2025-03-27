import re

# Mapping of CID numbers to Hebrew characters
MAP = {
    "15": ",",
    "16": "-",
    "17": ".",
    "29": ":",
    "154": "א",
    "155": "ב",
    "156": "ג",
    "157": "ד",
    "158": "ה",
    "159": "ו",
    "160": "ז",
    "161": "ח",
    "162": "ט",
    "163": "י",
    "164": "ך",
    "165": "כ",
    "166": "ל",
    "167": "ם",
    "168": "מ",
    "169": "ן",
    "170": "נ",
    "171": "ס",
    "172": "ע",
    "173": "ף",
    "174": "פ",
    "175": "ץ",
    "176": "צ",
    "177": "ק",
    "178": "ר",
    "179": "ש",
    "180": "ת",
    "188": "-",
    "5": "״",
    "3": " ",
}


def cid_to_hebrew(text: str) -> str:
    pattern = r"\(cid:(\d+)\)"

    def cid_replacer(match):
        cid_number = match.group(1)
        return MAP.get(cid_number, f"({cid_number})")

    return re.sub(pattern, cid_replacer, text)


def replace_cid_tokens_in_list(row_list):
    return [cid_to_hebrew(cell) for cell in row_list]
