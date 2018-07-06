#6.21.18 Rainfall 6kyu
#data and data1 are strings with rainfall records for a few cities for each month

data = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7"""

import pandas as pd
import numpy as np

def parse_data(data):
    lines = data.split('\n')
    cities = []
    rainfall_by_city = []
    for line in lines:
        if len(line) > 1:
            city = line.split(':')[0]
            cities.append(city)
            month_rainfalls = line.split(':')[1]
            month_rainfall = month_rainfalls.split(',')
            months = [m_r.split(' ')[0] for m_r in month_rainfall]
            rainfall = np.array([m_r.split(' ')[1] for m_r in month_rainfall]).astype(float)
            rainfall_by_city.append(rainfall)
    columns = months
    index = cities
    df = pd.DataFrame(columns = columns, index = cities, data = rainfall_by_city)
    return df

def mean(town, strng):
    df = parse_data(strng)
    means = df.mean(axis=1)
    if town in df.index:
        return means.loc[town]
    else:
        return -1

def variance(town, strng):
    df = parse_data(strng)
    var = df.var(axis=1, ddof = 0)
    if town in df.index:
        return var.loc[town]
    else:
        return -1

########## Solutions ##########
def get_towndata(town, strng):
    for line in strng.split('\n'):
        s_town, s_data = line.split(':')
        if s_town == town:
            return [s.split(' ') for s in s_data.split(',')]
    return None

def mean(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        return sum([float(x) for m,x in data]) / len(data)
    else:
        return -1.

def variance(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        mean = sum([float(x) for m,x in data]) / len(data)
        return sum([(float(x)-mean)**2 for m,x in data]) / len(data)
    else:
        return -1.

############
import numpy as np

def split_data(town,strng):
    city_data = dict(city.split(":") for city in strng.splitlines())
    return dict(v.split() for v in [m for m in city_data[town].split(',')]) if town in city_data else 0

def mean(town, strng):
    d = split_data(town, strng)
    return np.average(np.array([float(x) for x in d.values()])) if d else -1

def variance(town, strng):
    d = split_data(town, strng)
    return np.var(np.array([float(x) for x in d.values()])) if d else -1

############
import statistics, re

rain = lambda town, strng: map(float, re.findall("\d+(?:\.\d+)?", "".join(re.findall(town+":(.+)\n", strng))))

def mean(town, strng):
    return statistics.mean(rain(town, strng))
def variance(town, strng):
    return statistics.pvariance(rain(town, strng))
