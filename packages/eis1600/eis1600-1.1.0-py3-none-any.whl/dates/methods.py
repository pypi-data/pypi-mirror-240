from eis1600.miu.YAMLHandler import YAMLHandler
from pandas import DataFrame, Series
from typing import Match

from openiti.helper.ara import normalize_ara_heavy

from eis1600.dates.Date import Date
from eis1600.dates.date_patterns import DATE_CATEGORIES_NOR, DATE_CATEGORY_PATTERN, DATE_PATTERN, \
    DAY_ONES_NOR, \
    DAY_TEN_NOR, MONTHS_NOR, \
    WEEKDAYS_NOR, ONES_NOR, TEN_NOR, HUNDRED_NOR
from eis1600.processing.preprocessing import get_tokens_and_tags


def parse_year(m: Match[str]) -> (int, int):
    year = 0
    length = 1  # word sana
    if m.group('ones'):
        year += ONES_NOR.get(normalize_ara_heavy(m.group('ones')))
        length += 1
    if m.group('ten'):
        year += TEN_NOR.get(normalize_ara_heavy(m.group('ten')))
        length += 1
    if m.group('hundred'):
        year += HUNDRED_NOR.get(normalize_ara_heavy(m.group('hundred')))
        length += len(m.group('hundred').split())

    return year, length


def get_dates_headings(yml_handler: YAMLHandler) -> None:
    """Checks the headings for date statements and if a such a statement is found, it is converted into a tag and
    added to the yml header.

    :param YAMLHandler yml_handler: arabic text.
    """
    headings = yml_handler.headings
    for key, val in headings:
        if DATE_PATTERN.search(val):
            m = DATE_PATTERN.search(val)
            year, length = parse_year(m)
            yml_handler.add_date_headings(year)


def tag_dates_fulltext(text: str) -> str:
    """Inserts date tags in the arabic text and returns the text with the tags.

    :param str text: arabic text.
    :return str: arabic text with date tags.
    """
    text_updated = text
    m = DATE_PATTERN.search(text_updated)
    while m:
        month = None
        day = 0
        weekday = None
        # Length is one because sana is definitely recognized
        year, length = parse_year(m)

        if DATE_CATEGORY_PATTERN.search(m.group('context')):
            last = DATE_CATEGORY_PATTERN.findall(m.group('context'))[-1]
            date_category = DATE_CATEGORIES_NOR.get(normalize_ara_heavy(last))
        else:
            date_category = 'X'

        # if m.group('weekday'):
        #     weekday = WEEKDAYS_NOR.get(normalize_ara_heavy(m.group('weekday')))
        # if m.group('day_ones'):
        #     day += DAY_ONES_NOR.get(normalize_ara_heavy(m.group('day_ones')))
        # if m.group('day_ten'):
        #     day += DAY_TEN_NOR.get(normalize_ara_heavy(m.group('day_ten')))
        # if m.group('month'):
        #     month_str = normalize_ara_heavy(m.group('month'))
        #     month = MONTHS_NOR.get(month_str)
        # else:
        #     mm = MONTH_PATTERN.search(m[0])
        #     if mm:
        #         month_str = mm[0]
        #         month = MONTHS.get(month_str)

        # if day == 0:
        #     day = None
        if year == 0:
            year = None

        date = Date(year, length, date_category)
        pos = m.start('sana')
        text_updated = text_updated[:pos] + date.get_tag() + text_updated[pos:]

        m = DATE_PATTERN.search(text_updated, m.end('sana') + len(date.get_tag()))

    return text_updated


def date_annotate_miu_text(ner_df: DataFrame, yml: YAMLHandler) -> Series:
    """Annotate dates in the headings and in the MIU text, returns a list of tag per token.

    :param DataFrame ner_df: df containing the 'TOKENS' column.
    :param YAMLHandler yml: yml_header to collect date tags in.
    :return Series: List of date tags per token, which can be added as additional column to the df.
    """
    get_dates_headings(yml)

    ner_df.mask(ner_df == '', None, inplace=True)
    tokens = ner_df['TOKENS'].dropna()
    ar_text = ' '.join(tokens)

    tagged_text = tag_dates_fulltext(ar_text)
    ar_tokens, tags = get_tokens_and_tags(tagged_text)
    ner_df.loc[ner_df['TOKENS'].notna(), 'DATE_TAGS'] = tags

    return ner_df['DATE_TAGS'].tolist()
