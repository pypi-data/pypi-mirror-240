# NLP
MINIMUN_CHAR_LENGTH = 15
MINIMUN_WORDS_LENGTH = 4
filenames_types = ["doc", "docx"]
lfilenames_types = ["doc", "docx", "pdf", "ppt", "pptx", "odt", "rtf", "xls", "xlsx"]
blacklist = [
    "[document]",
    "style",
    "noscript",
    "header",
    "html",
    "meta",
    "head",
    "input",
    "script",
    "style",
]
# score for NER fine tuning
SCORE_NER = 0.65

# ROT
FILE_NAME_COL = "file_name"
FILE_TYPE_COL = "file_type"
COLS_ROT = [
    "index",
    "is_image",
    "is_business",
    "days_accesed",
    "days_modified",
    "days_created",
    "seconds_accesed",
    "seconds_modified",
    "seconds_created",
    "outdated_group",
    "trivial",
    "obsolete",
    "redundant",
    "is_rot",
]

# Semantic
MAX_LENGTH_TEXT_EMBEDDING = 1000000
