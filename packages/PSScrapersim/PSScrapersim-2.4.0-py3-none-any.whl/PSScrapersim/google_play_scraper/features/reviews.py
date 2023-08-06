from datetime import datetime, timedelta
import json
from time import sleep
from typing import Optional, Tuple, List
from .. import Sort
from ..constants.element import ElementSpecs
from ..constants.regex import Regex
from ..constants.request import Formats
from ..utils.request import post


MAX_COUNT_EACH_FETCH = 400


class _ContinuationToken:
    __slots__ = "token", "lang", "country", "sort", "count", "filter_score_with"

    def __init__(self, token, lang, country, sort, count, filter_score_with):
        self.token = token
        self.lang = lang
        self.country = country
        self.sort = sort
        self.count = count
        self.filter_score_with = filter_score_with


def _fetch_review_items(
    url: str,
    app_id: str,
    sort: int,
    count: int,
    filter_score_with: Optional[int],
    pagination_token: Optional[str],
):
    dom = post(
        url,
        Formats.Reviews.build_body(
            app_id,
            sort,
            count,
            "null" if filter_score_with is None else filter_score_with,
            pagination_token,
        ),
        {"content-type": "application/x-www-form-urlencoded"},
    )

    match = json.loads(Regex.REVIEWS.findall(dom)[0])

    return json.loads(match[0][2])[0], json.loads(match[0][2])[-1][-1]


def reviews(
    app_id: str,
    lang: str = "en",
    country: str = "us",
    sort: Sort = Sort.NEWEST,
    count: int = 100,
    filter_score_with: int = None,
    continuation_token: _ContinuationToken = None,
) -> Tuple[List[dict], _ContinuationToken]:
    if continuation_token is not None:
        token = continuation_token.token

        if token is None:
            return (
                [],
                continuation_token,
            )

        lang = continuation_token.lang
        country = continuation_token.country
        sort = continuation_token.sort
        count = continuation_token.count
        filter_score_with = continuation_token.filter_score_with
    else:
        token = None

    url = Formats.Reviews.build(lang=lang, country=country)

    _fetch_count = count

    result = []

    while True:
        if _fetch_count == 0:
            break

        if _fetch_count > MAX_COUNT_EACH_FETCH:
            _fetch_count = MAX_COUNT_EACH_FETCH

        try:
            review_items, token = _fetch_review_items(
                url, app_id, sort, _fetch_count, filter_score_with, token
            )
        except (TypeError, IndexError):
            token = None
            break

        for review in review_items:
            result.append(
                {
                    k: spec.extract_content(review)
                    for k, spec in ElementSpecs.Review.items()
                }
            )

        _fetch_count = count - len(result)

        if isinstance(token, list):
            token = None
            break

    return (
        result,
        _ContinuationToken(token, lang, country, sort,
                           count, filter_score_with),
    )


def reviews_all(
    app_id: str,
    today: Optional[bool] = False,
    yesterday: Optional[bool] = False,
    hour: Optional[bool] = False,
    sleep_milliseconds: int = 0,
    **kwargs
) -> list:
    kwargs.pop("count", None)
    kwargs.pop("continuation_token", None)

    continuation_token = None

    result = []
    today_result = []

    while True:
        _result, continuation_token = reviews(
            app_id,
            count=MAX_COUNT_EACH_FETCH,
            continuation_token=continuation_token,
            sort=Sort.NEWEST,
            **kwargs
        )
        # print(_result)
        if today:
            tday = datetime.today().strftime("%d/%m/%Y")
            for x in _result:
                # print(x["at"][:10], tday)
                if x["at"][:10] == tday:
                    result.append(x)
                elif x["at"][:10] != tday:
                    continuation_token.token = None
                    print(result)
                    break
            # print(today_result)
            # return today_result
        elif yesterday:
            tday = datetime.today()
            tdays = datetime.today().strftime("%d/%m/%Y")
            yday = (tday - timedelta(days=1)).strftime("%d/%m/%Y")
            # print(_result)
            for x in _result:
                # print(x["at"][:10] != yday or x["at"][:10] != tdays)
                # print(x["at"][:10], yday, tdays)
                if x["at"][:10] == yday:
                    result.append(x)
                elif x["at"][:10] != yday and x["at"][:10] != tdays:
                    continuation_token.token = None
                    print(result)
                    break
        elif hour:
            hour_time = datetime.now()
            start_htime = hour_time - timedelta(hours=1)
            for x in _result:
                #  print(datetime.strptime(x["at"], "%d/%m/%Y %H:%M:%S"), start_htime)
                if (
                    datetime.strptime(
                        x["at"], "%d/%m/%Y %H:%M:%S") > start_htime
                    and datetime.strptime(x["at"], "%d/%m/%Y %H:%M:%S") <= hour_time
                ):
                    result.append(x)
                elif not (
                    datetime.strptime(
                        x["at"], "%d/%m/%Y %H:%M:%S") > start_htime
                    and datetime.strptime(x["at"], "%d/%m/%Y %H:%M:%S") <= hour_time
                ):
                    continuation_token.token = None
                    print(result)
                    break
        else:
            result += _result

        if continuation_token.token is None:
            break

        if sleep_milliseconds:
            sleep(sleep_milliseconds / 1000)
        # print(result)
    return result
