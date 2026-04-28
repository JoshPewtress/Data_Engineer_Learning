def transform(raw_data):
    return [{
        "name": row["name"],
        "height": row["height"],
        "weight": row["weight"],
        "types": [typ["type"]["name"] for typ in row["types"]]
    } for row in raw_data]