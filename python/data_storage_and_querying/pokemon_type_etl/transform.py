def transform(raw_data):
    output = []

    for row in raw_data:
        output.append({
            "name": row["name"],
            "height": row["height"],
            "weight": row["weight"],
            "types": [typ["type"]["name"] for typ in row["types"]]
        })

    return output