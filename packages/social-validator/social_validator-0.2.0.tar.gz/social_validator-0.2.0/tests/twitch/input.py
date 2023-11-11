from social_validator.twitch import (
    DESCRIPTION_MAX_LENGTH,
    MESSAGE_MAX_LENGTH,
    USERNAME_MAX_LENGTH,
    USERNAME_MIN_LENGTH,
)
from tests.shared.input import ESCAPED_STRING, RANDOM_UNICODE_STRING

VALID_USERNAMES = {
    "a" * USERNAME_MIN_LENGTH,
    "a" * USERNAME_MAX_LENGTH,
    "a123",
    "123a",
    "a_12",
    "username",
    "user_name",
    "user___name",
    "u_s_e_r_n_a_m_e",
    "u_1_2_3_4_5_6",
    "username_______",
}

INVALID_USERNAMES = {
    "",  # empty
    "a" * (USERNAME_MIN_LENGTH - 1),  # too short
    "a" * (USERNAME_MAX_LENGTH + 1),  # too long
    "_username",  # starts with underscore
    "_" * USERNAME_MIN_LENGTH,  # consist entirely of special chars
    "123456",  # consist entirely of digits
    "user name",  # special char
    "username@",  # special char
    RANDOM_UNICODE_STRING,  # invalid chars
    ESCAPED_STRING,  # escaped chars
}

VALID_DESCRIPTIONS = {
    "",
    "a",
    "1" * DESCRIPTION_MAX_LENGTH,
    RANDOM_UNICODE_STRING,
}

INVALID_DESCRIPTIONS = {
    "1" * (DESCRIPTION_MAX_LENGTH + 1),  # too long
    ESCAPED_STRING,  # escaped chars
}

VALID_MESSAGES = {
    "a",
    "1" * MESSAGE_MAX_LENGTH,
    RANDOM_UNICODE_STRING,
}

INVALID_MESSAGES = {
    "",  # empty
    "1" * (MESSAGE_MAX_LENGTH + 1),  # too long
    ESCAPED_STRING,  # escaped chars
}
