def find_region(acronym, regions):
    region = None
    for feature in regions["features"]:
        if feature["properties"]["Acronym"] == acronym:
            region = feature.copy()
            break

    if region is None:
        raise ValueError(f"Region {acronym} does not exist.")

    return region

def find_region_bbox(region):
    polygon = region["geometry"]["coordinates"]
    coords = polygon[0]  # assuming one ring (exterior ring)
    xs = [pt[0] for pt in coords]
    ys = [pt[1] for pt in coords]
    
    min_x, min_y = min(xs), min(ys)
    max_x, max_y = max(xs), max(ys)
    
    bbox = [min_x, min_y, max_x, max_y]

    return bbox