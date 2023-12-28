from datetime import datetime, time
from typing import Any, List
import re

def format_data_from_arrays(keys: List[str], values: List[List[Any]]) -> List[dict]:
    '''
    Format array of key strings and nested array of values into an array of
    dicts with respective key, value pairs
    '''
    return_list = []
    
    for v in values:
        return_list.append(dict(zip(keys,v)))
    return return_list

def format_dates_with_regex(date: str, pattern: str) -> str | None:
    matched = re.match(pattern, date)
    if matched is not None:
        return matched.group()
    else:
        return matched

def format_time(time: str, pattern: str) -> time:
    date_formatted = datetime.strptime(time, pattern) 
    time_formatted = date_formatted.time()
    return time_formatted

def format_address(address: str, pattern: str) -> str:
    address_formatted = re.sub(pattern,"", address)
    return address_formatted
