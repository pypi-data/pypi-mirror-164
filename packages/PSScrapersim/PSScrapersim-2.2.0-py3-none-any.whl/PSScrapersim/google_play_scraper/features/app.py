import json
from typing import Any, Dict

from ..constants.element import ElementSpecs
from ..constants.regex import Regex
from ..constants.request import Formats
from ..utils.request import get


def app(app_id: str, lang: str = "en", country: str = "us") -> Dict[str, Any]:
    url = Formats.Detail.build(app_id=app_id, lang=lang, country=country)

    dom = get(url)

    matches = Regex.SCRIPT.findall(dom)

    dataset = {}

    for match in matches:
        key_match = Regex.KEY.findall(match)
        value_match = Regex.VALUE.findall(match)

        if key_match and value_match:
            key = key_match[0]
            value = json.loads(value_match[0])

            dataset[key] = value

    result = {}

    for k, spec in ElementSpecs.Detail.items():
        content = spec.extract_content(dataset)

        result[k] = content

    result["appId"] = app_id
    result["url"] = url

    return result
