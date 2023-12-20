def compare_feature(product,feature: str):
    commers = []
    for key in product:
        if (feature in key.lower()):
            commers.append(key)

    if len(commers) > 0 :
        return commers
    else:
        return None



    
