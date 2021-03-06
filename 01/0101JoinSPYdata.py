"""


"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    print "type(df1)=", type(df1), "df1.shape=", df1.shape
    #NB: df1 shape is 5 rows & zero columns at this point, but content = []
    print "df1=\n", df1
    print "index values = df1.index.values=", df1.index.values
    dfSPY = pd.read_csv("data/SPY.csv")
    print "type(dfSPY)=", type(dfSPY), "dfSPY.shape=", dfSPY.shape
    print "dfSPY.head(5)=\n", dfSPY.head(5)
    print "dfSPY.columns.values.tolist()=", dfSPY.columns.values.tolist()
    print "list(dfSPY)=", list(dfSPY)
    print "index values = dfSPY.index.values=", dfSPY.index.values
    df1 = df1.join(dfSPY)
    print "\ndf1.head(5)=\n", df1.head(5)
    print "type(df1)=", type(df1)
    print "df1.shape=", df1.shape

if __name__ == "__main__":
    test_run()
