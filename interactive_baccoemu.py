
import numpy as np
import baccoemu

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, output_file, show

pars = {
    'omega_matter' : 0.315,
    'omega_baryon' : 0.05,
    'hubble' : 0.7,
    'ns' : 0.96,
    'sigma8' : 0.83,
    'neutrino_mass' : 0,
    'w0' : -1,
    'wa' : 0,
    'expfactor' : 1
}
emu = baccoemu.Matter_powerspectrum()
k, pk = emu.get_nonlinear_pk(pars)

source = ColumnDataSource(data=dict(k=k, pk=pk))

plot = figure(plot_width=400, plot_height=400,
              y_range=[10,4e4],
              y_axis_type='log', x_axis_type='log')

plot.line('k', 'pk', source=source, line_width=3, line_alpha=0.6)

omega_m_slider = Slider(start=0.23, end=0.4, value=0.315,
                        step=0.01, title="omega cold")
omega_b_slider = Slider(start=0.04, end=0.06, value=0.05,
                        step=0.001, title="omega baryons")
hubble_slider = Slider(start=0.6, end=0.8, value=0.67,
                        step=0.001, title="hubble")
ns_slider = Slider(start=0.92, end=1.01, value=0.96,
                       step=0.001, title="ns")
sigma8_slider = Slider(start=0.73, end=0.9, value=0.83,
                       step=0.001, title="sigma8")
neutrino_mass_slider = Slider(start=0.0, end=0.4, value=0,
                       step=0.01, title="neutrino mass")
w0_slider = Slider(start=-1.15, end=-0.85, value=-1,
                              step=0.001, title="w0")
wa_slider = Slider(start=-0.3, end=0.3, value=0,
                   step=0.001, title="wa")
expfactor_slider = Slider(start=0.4, end=1, value=1,
                   step=0.001, title="a")

def callback(attr, old, new):
    om = omega_m_slider.value
    ob = omega_b_slider.value
    h = hubble_slider.value
    ns = ns_slider.value
    sigma8 = sigma8_slider.value
    mnu = neutrino_mass_slider.value
    w0 = w0_slider.value
    wa = wa_slider.value
    a = expfactor_slider.value
    pars = {
    'omega_matter' : om,
    'omega_baryon' : ob,
    'hubble' : h,
    'ns' : ns,
    'sigma8' : sigma8,
    'neutrino_mass' : mnu,
    'w0' : w0,
    'wa' : wa,
    'expfactor' : a
    }
    _k, _pk = emu.get_nonlinear_pk(pars)
    source.data['k'] = _k
    source.data['pk'] = _pk


omega_m_slider.on_change('value', callback)
omega_b_slider.on_change('value', callback)
hubble_slider.on_change('value', callback)
ns_slider.on_change('value', callback)
sigma8_slider.on_change('value', callback)
neutrino_mass_slider.on_change('value', callback)
w0_slider.on_change('value', callback)
wa_slider.on_change('value', callback)
expfactor_slider.on_change('value', callback)

layout = row(
    plot,
    column(omega_m_slider,
           omega_b_slider,
           hubble_slider,
           ns_slider,
           sigma8_slider,
           neutrino_mass_slider,
           w0_slider,
           wa_slider,
           expfactor_slider),
)

curdoc().add_root(layout)
