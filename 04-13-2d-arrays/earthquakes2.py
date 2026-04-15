import requests
import matplotlib.pyplot as pyplot

def plot_quakes() -> None:
  """Plot the locations of all earthquakes in the past 30 days.
  Parameters: None
  Return value: None
  """
  url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
  quake_file = requests.get(url)
  latitudes = [] # y coordinates
  longitudes = [] # x coordinates
  depths = [] # depths
  header = True # first line is the header

  for raw_line in quake_file.iter_lines():
    if header: # don't process this line
      header = False # but do process the rest
    else:
      line = raw_line.decode('utf-8') # interpret the line as text]
      row = line.split(',') # split columns at commas

      latitudes.append(float(row[1])) # append latitude
      longitudes.append(float(row[2])) # append longitude
      depths.append(float(row[3]))

  colors = []
  for depth in depths:
    if depth < 10:
      colors.append('yellow')
    elif depth < 50:
      colors.append('red')
    else:
      colors.append('blue')

  pyplot.scatter(longitudes, latitudes, 10, color=colors) # 10 = area of each point
  pyplot.show()


plot_quakes()
