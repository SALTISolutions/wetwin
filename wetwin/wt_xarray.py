# Convenience functions for xarray

import pandas as pd

"""
def dataset_get_python_times(ds)
    returns t0,dt,ntimes for an xarray dataset
    t0: first time as python datetime
    dt: time step as python datetime
    ntimes: number of times
"""
def dataset_get_python_times(ds):
    ntimes=len(ds.time)
    t0=pd.Timestamp(ds.time[0].values).to_pydatetime()
    if ntimes==1:
        return t0,0,1
    elif ntimes==2: 
        t1=pd.Timestamp(ds.time[1].values).to_pydatetime()
        dt=t1-t0
        return t0,dt,2
    else:
        t1=pd.Timestamp(ds.time[1].values).to_pydatetime()
        t2=pd.Timestamp(ds.time[2].values).to_pydatetime()
        dt=t2-t1
        return t0,dt,ntimes