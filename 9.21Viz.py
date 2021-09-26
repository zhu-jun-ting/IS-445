# %%

import bqplot
from bqplot import scales
from bqplot import marks
from bqplot import axes
from bqplot.interacts import Interaction
from matplotlib.pyplot import sca
import numpy as np
from numpy.lib.function_base import disp
import pandas as pd
import traitlets
import ipywidgets

bqplot.Figure()
# %%

x = np.arange(100)
y = np.random.random(100) + 5
x_sc = bqplot.LinearScale()
y_sc = bqplot.LinearScale()
lines = bqplot.Lines(x=x, y=y, scales={'x':x_sc, 'y':y_sc})
ax_x = bqplot.Axis(scale=x_sc)
ax_y = bqplot.Axis(scale=y_sc, orientation='vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale=x_sc)

fig = bqplot.Figure(marks=[lines], axes=[ax_x, ax_y], interaction=interval_selector)
display(fig)

# %%

interval_selector.selected = interval_selector.selected * 2
# %%

label_lower = ipywidgets.Label("Lower Limit:")
label_upper = ipywidgets.Label("Upper Limit:")
label_aggregate = ipywidgets.Label('Sum:')

def on_change_selected(change):
    if change['new'].size < 2: return
    lower, upper = change['new']
    label_lower.value = "Lower Limit: %s" % lower
    label_upper.value = "Upper Limit: %s" % upper
    aggregate = y[(x > lower) & (x < upper)].sum()
    label_aggregate.value = 'Sum: %s' % aggregate
    
interval_selector.observe(on_change_selected, ['selected'])

display(ipywidgets.VBox([label_lower, label_upper, label_aggregate, fig]))
# %%

x = np.arange(100)
y1 = np.random.random(100) + 5
y2 = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y1_sc = bqplot.LinearScale()
y2_sc = bqplot.LogScale()

lines1 = bqplot.Lines(x = x, y = y1, scales = {'x': x_sc, 'y': y1_sc})
lines2 = bqplot.Lines(x = x, y = y2, scales = {'x': x_sc, 'y': y2_sc})
# scatter = bqplot.Scatter

ax_x = bqplot.Axis(scale = x_sc, label = 'X value')
ax_y1 = bqplot.Axis(scale = y1_sc, label = 'Y1 value', orientation = 'vertical')
ax_y2 = bqplot.Axis(scale = y2_sc, label = 'Y2 value', orientation = 'vertical')

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig1 = bqplot.Figure(marks = [lines1], axes = [ax_x, ax_y1], interaction = interval_selector)
fig2 = bqplot.Figure(marks = [lines2], axes = [ax_x, ax_y2], interaction = interval_selector)
# fig3 = bqplot.Figure(marks = [scatter], axes = [y1_sc, y2_sc])

display(ipywidgets.VBox([fig1, fig2]))
# %%

x = np.arange(100)
y1 = np.random.random(100) + 5
y2 = x**2 + np.random.random(100) * 10

x_sc = bqplot.LinearScale()
y1_sc = bqplot.LinearScale()
y2_sc = bqplot.LogScale()

lines1 = bqplot.Lines(x = x, y = y1, scales = {'x': x_sc, 'y': y1_sc})
lines2 = bqplot.Lines(x = x, y = y2, scales = {'x': x_sc, 'y': y2_sc})

ax_x = bqplot.Axis(scale = x_sc, label = 'X value')
ax_y1 = bqplot.Axis(scale = y1_sc, label = 'Y1 value', orientation = 'vertical')
ax_y2 = bqplot.Axis(scale = y2_sc, label = 'Y2 value', orientation = 'vertical')

ax_y1sc = bqplot.Axis(scale = y1_sc, label = 'Y1 value')
ax_y2sc = bqplot.Axis(scale = y2_sc, label = 'Y2 value', orientation = 'vertical')

scatter = bqplot.Scatter(x = y1, y = y2, scales = {'x': y1_sc, 'y': y2_sc})

interval_selector = bqplot.interacts.FastIntervalSelector(scale = x_sc)

fig1 = bqplot.Figure(marks = [lines1], axes = [ax_x, ax_y1], interaction = interval_selector)
fig2 = bqplot.Figure(marks = [lines2], axes = [ax_x, ax_y2], interaction = interval_selector)
fig3 = bqplot.Figure(marks = [scatter], axes = [ax_y1sc, ax_y2sc])

display(
    ipywidgets.HBox([
        ipywidgets.VBox(
            [fig1, fig2]
        ),
        fig3
    ])
)

# %%

# %%

scatter.selected_style = {'stroke': 'black', 'fill': 'orange'}
scatter.selected = np.arange(10)
# %%

def on_change_selected(change):
    lower, upper = change['new']
    selected_points = np.where((x > lower) and (x < upper))
    scatter.selected = selected_points

interval_selector.observe(on_change_selected, ['selected'])
# %%

df = pd.read_csv("building_inventory.csv", na_values = {'Year Acquired': 0, 'Year Constructed': 0,'Square Footage': 0})
df
# %%

year_constructed_sc = bqplot.LinearScale()
year_acquired_sc = bqplot.LinearScale()

year_acquired = df['Year Acquired']
year_constructed = df['Year Constructed']

scatter = bqplot.Scatter(x = year_constructed, y = year_acquired, scales = {'x': year_constructed_sc, 'y': year_acquired_sc})

constructed_ax = bqplot.Axis(scale = year_constructed_sc)
acquired_ax = bqplot.Axis(scale = year_acquired_sc, orientation = 'vertical')

brush = bqplot.interacts.BrushSelector(x_scale = year_constructed_sc, y_scale = year_acquired_sc)
fig = bqplot.Figure(marks = [scatter], axes = [constructed_ax, acquired_ax], interaction = brush)

display(fig)
# %%

# %%

# %%
