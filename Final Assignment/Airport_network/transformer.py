import pandas

airports = pandas.read_csv("C:/Users/lorga/Uni/2. Block/Tools and Methods/Lab 4/Airport_network/airports.csv")
routes = pandas.read_csv("C:/Users/lorga/Uni/2. Block/Tools and Methods/Lab 4/Airport_network/routes.csv")

airports_updated = airports.sort_values(by=["TotalSeats"], ascending = False).head(200)
airports_updated = airports_updated.rename(columns={"Orig": "ID"})

routes_updated = routes.groupby(["Source Airport", "Destination Airport"]).size().reset_index().rename(columns={0:'count'})
routes_updated = routes_updated.loc[routes_updated["Source Airport"].isin(airports_updated["ID"])]
routes_updated = routes_updated.loc[routes_updated["Destination Airport"].isin(airports_updated["ID"])]
routes_updated = routes_updated.set_axis(["Source", "Target", "Weight"], axis = 1)

airports_updated.to_csv("C:/Users/lorga/Uni/2. Block/Tools and Methods/Lab 4/Airport_network/airports_updated.csv", encoding = "utf8", index = False)
routes_updated.to_csv("C:/Users/lorga/Uni/2. Block/Tools and Methods/Lab 4/Airport_network/routes_updated.csv", index = False)