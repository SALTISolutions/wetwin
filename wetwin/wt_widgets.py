# Add new widgets here.

import solara

"""
def index2time(index,tstart,tstep)
Convert index of time series to time
index: index of time series
tstart: start time of time series, as datetime object
tstep: time step of time series, as timedelta object
"""
def index2time(index,tstart,tstep):
    return tstart+index*tstep

"""
def SliderDateTime(label="",value=None,tstart=None,ntimes=None,tstep=None,skip_steps=3)
Slider widget for time series data.  The slider is based on the index of the time series, not the time itself.
The time series is assumed to be evenly spaced in time.  The time series is assumed to start at tstart and end at tstop.
label: label for the widget
value: initial value of the slider, should be the index, ie an integer, starting at 0
tstart: start time of the time series, as datetime object
ntimes: number of time steps in the time series
tstep: time step of the time series, as timedelta object
skip_steps: number of time steps to skip when using the << and >> buttons
"""
@solara.component
def SliderDateTime(label="",value=None,tstart=None,ntimes=None,tstep=None,skip_steps=3):
    if value is None:
        error("Value must be specified for SliderDateTime")
    if tstart is None:
        error("tstart must be specified for SliderDateTime")
    if ntimes is None:
        error("ntimes must be specified for SliderDateTime")
    if tstep is None:
        error("tstep must be specified for SliderDateTime")
    with solara.Row(gap="10px", justify="space-around"):
        solara.Text(f"{label} {index2time(value.value,tstart,tstep)}")
        solara.Button("<<",on_click=lambda: value.set(value.value-skip_steps))
        solara.Button("<",on_click=lambda: value.set(value.value-1))
        solara.Button(">",on_click=lambda: value.set(value.value+1))
        solara.Button(">>",on_click=lambda: value.set(value.value+skip_steps))
        solara.SliderInt(label="",value=value,min=0,max=ntimes-1,step=1)
