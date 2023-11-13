"""
Conversions and normalizations.
"""
import re


def as_gib(value: int):
    """
    Convert from bytes to GigiBytes.
    """
    return value / 1024**3


def normalize_hwaddress( value: str):
    if not value:
        return value

    if value.startswith('MAC:'):
        value = value[len('MAC:'):]

    value = value.strip()

    for regex in [HWADDRESS6_REGEX, HWADDRESS8_REGEX]:
        if m := regex.match(value):
            groups = m.groups()
            return ':'.join(groups[i].lower() for i in range(0, len(groups)))

    return value

HWADDRESS6_REGEX = re.compile(r'^([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})$', re.IGNORECASE)
HWADDRESS8_REGEX = re.compile(r'^([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})[\:\-]?([0-9a-f]{2})$', re.IGNORECASE)
