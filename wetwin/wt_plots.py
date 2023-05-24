# Create base class for plots
#
# As a user, you can extend this class to create your own plots. For example:
# class MyPlot1(wtPlot):
#     def __init__(self,variables,amplitude,*args,**kwargs): # You can add your own arguments before *args
#         super().__init__(variables,*args,**kwargs) #this is needed and will link to the variables
#                                        # the *args and **kwargs are passed to the widgets.Output class
#         #expand here with your own data
#         self.amplitude=amplitude
#     def redraw(self):
#         ax=self.ax
#         period=self.variables[0].value # assumes the first variable is the period
#         x = np.linspace(0, period * 2 * np.pi, 100)
#         ax.plot(x, self.amplitude * np.sin(x), color='C0')
#         plt.title(f"Sine with period {period} cycles")
#         ax.set_ylim([-2, 2])
#         ax.grid(True)
# 
import ipywidgets as widgets
import matplotlib.pyplot as plt

# Base class for plots
# You can extend this class to create your own plots, see example above
class wtPlot(widgets.Output):
    def __init__(self,variables,*args,**kwargs):
        # layout = widgets.Layout(width="100%",height='400px')
        super().__init__(*args,**kwargs)
        fig, ax = plt.subplots() #figsize=(6, 4)
        fig.canvas.header_visible = False
        fig.tight_layout()
        self._fig=fig
        self._ax=ax
        self._variables=variables
        for v in variables:
            v.observe(self)
    @property
    def caller(self):
        return self._caller
    @property
    def ax(self):
        return self._ax
    @property
    def fig(self):
        return self._fig
    @property
    def variables(self):
        return self._variables
    def redraw(self): pass 
    def update(self,v):
        self._caller=v
        self._ax.clear()
        self.redraw()
        self._fig.canvas.draw_idle()