from msilib.schema import Class


class Route:
  def __init__(self, departure, destination, startTime, endTime):
      self.departure = departure
      self.destination = destination
      if startTime == 0:
          self.time = endTime
          self.start = False
      else:
          self.time = startTime
          self.start = True

  def getRoutes(self):
      #use map to find routes and save into arrRoutes
      sortedTimes = TimeSort(arrRoutes, self.time)
      if start == True:
          routeOrder = sortedTimes.orderShortestStart()
      else:
          routeOrder = sortedTimes.orderShortestEnd()

      return routeOrder


  
