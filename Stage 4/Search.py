class Search:
    def __innit__ (self, destStation, deptStation, startTime, endTime):
        self.destStation = destStation
        self.deptStation = deptStation
        self.startTime = startTime
        self.endTime = endTime

    def findRoutes(self):
        station = Stations()
        if station.findStation(self.destStation) = False:
            return "Could not find Station"
        if station.findStation(self.deptStation) = False:
            return "Could not find Station"

        route = Routes(self.deptStation, self.destStation, self.startTime, self.endTime)
        route.getRoutes()
        return route


