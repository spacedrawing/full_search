def find_spn(toponym):
    envelope = toponym["boundedBy"]["Envelope"]

    
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")

        
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

        
    span = f"{dx},{dy}"

    return span