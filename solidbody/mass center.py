def converter(coords):
    for i in range(len(coords)):
        x1=coords[i][0]
        y1=coords[i][1]
        x2=coords[(i+1)//len(coords)][0]
        y2=coords[(i+1)//len(coords)][0]
        k=(y1-y2)/(x1-x2)
        d=[]
        if abs(k)<1:
            for i in range(abs(y1-y2)):
                y=min(y1, y2)
def center_mass(coords):
    pass