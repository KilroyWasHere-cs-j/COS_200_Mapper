import pandas as pd
import os
import mapPy


mapy = mapPy.mapper()

lat, lon = 43.680031, -70.310425

blat, blon = 43.909313, -69.987274

line = [[43.680031, -70.310425], [43.78347, -69.34421], [43.3456, -69.35683], [43.909313, -69.987274]]

# Load data into pandas dataframe
# Makes sure that the file is really a .csv file
def loadData(filepath):
    return pd.read_csv(filepath) if ".csv" in filepath else "Not csv file"


def plotPoints():
    pass


# Main point of program execution
def main():
    df = loadData(os.getcwd() + "/data/open_campus3.csv")
    print(df.columns)
    
    # Load in the needed columns from the dataframe
    lats = list(df[" lat"])
    lngs = list(df[" lon"])
    places = list(df["Place"])
    colors = list(df[" color"])

    # Generate a map and center it on the average of the latitudes and longitudes
    map = mapy.createMap(mapy.getCenterPoint(lats), mapy.getCenterPoint(lngs), zoom_factor=16)
    assert map is not None  # Make sure that we generated a map


    count = 0
    for j in lats:
        mapy.addMarker(map=map, lat=j, lon=lngs[count], tooltip=places[count], color=colors[count])
        count = count + 1

    # Save the map
    mapy.saveMap(map, "test_map.html")
    # Render the map in a web browser
    mapy.showMap(map)



    print("Distance between Brunswick Maine and Portland Maine is: ", end=" ")
    print(mapy.get_distance(lat_1=lat, lng_1=lon, lat_2=blat, lng_2=blon), " miles")


if __name__ == "__main__":
    main()
