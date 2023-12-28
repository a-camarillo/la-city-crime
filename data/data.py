from typing import List
import utils
import json

def cleaned_data() -> List[dict]:
    with open("la-crime.json") as f:
        data = json.load(f)
        f.close()

    keys = []
    for column in data["meta"]["view"]["columns"]:
        keys.append(column["name"])

    values = []
    for value in data["data"]:
        values.append(value)
    
    data_list = utils.format_data_from_arrays(keys, values)
    
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    time_pattern = "%H%M"
    address_pattern = r"\s\s\s"
    
    for item in data_list:
        item["Date Rptd"] = utils.format_dates_with_regex(item["Date Rptd"], date_pattern)
        item["DATE OCC"] = utils.format_dates_with_regex(item["DATE OCC"], date_pattern)
        item["TIME OCC"] = utils.format_time(item["TIME OCC"], time_pattern)
        item["LOCATION"] = utils.format_address(item["LOCATION"], address_pattern)
        
        if not item["Vict Sex"]:
            item["Vict Sex"] = "X"
        
        if not item["Vict Descent"]:
            item["Vict Descent"] = "X"

        if not item["Premis Cd"]:
            item["Premis Cd"] = "710"
            item["Premis Desc"] = "OTHER PREMISE"
        
        if not item["Weapon Used Cd"]:
            item["Weapon Used Cd"] = "500"
            item["Weapon Desc"] = "UNKNOWN WEAPON/OTHER WEAPON"



        match item["Vict Descent"]:
            case "A":
                item["descentLong"] = "Other Asian"
            case "B":
                item["descentLong"] = "Black"
            case "C":
                item["descentLong"] = "Chinese"
            case "D":
                item["descentLong"] = "Cambodian"
            case "F":
                item["descentLong"] = "Filipino"
            case "G":
                item["descentLong"] = "Guamanian"
            case "H":
                item["descentLong"] = "Hispanic/Latin/Mexican"
            case "I":
                item["descentLong"] = "American Indian/Alaskan Native"
            case "J":
                item["descentLong"] = "Japanese"
            case "K":
                item["descentLong"] = "Korean"
            case "L":
                item["descentLong"] = "Laotian"
            case "O":
                item["descentLong"] = "Other"
            case "P":
                item["descentLong"] = "Pacific Islander"
            case "S":
                item["descentLong"] = "Samoan"
            case "U":
                item["descentLong"] = "Hawaiian"
            case "V":
                item["descentLong"] = "Vietnamese"
            case "W":
                item["descentLong"] = "White"
            case "X":
                item["descentLong"] = "Unknown"
            case "Z":
                item["descentLong"] = "Asian Indian"

    return data_list
