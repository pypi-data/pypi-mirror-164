from __future__ import annotations

from bokeh.plotting import figure
from bokeh.models import FreehandDrawTool, ColumnDataSource


class Plotting:
    @staticmethod
    def create_plot(title: str, x_axis_name: str = 'Time', x_axis_unit: str = 's', x_axis_type: str = 'linear', 
                                y_axis_name: str = None, y_axis_unit: str = None, y_axis_type: str = 'linear') -> dict:
        """
        Create empty Bokeh plot.
        """
        tooltips = [('Name', '$name'),
                    (x_axis_name, f'$x [{x_axis_unit}]'),
                    (y_axis_name, f'$y [{y_axis_unit}]')]

        tools = 'hover,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,reset,save'

        # Create figures (with options)
        figure_opts = {
            'x_axis_label': f'{x_axis_name} [{x_axis_unit}]',
            'x_axis_type': x_axis_type,
            'y_axis_label': f'{y_axis_name} [{y_axis_unit}]',
            'y_axis_type': y_axis_type,
            'sizing_mode': 'stretch_both',
            'tools': tools,
            'toolbar_location': 'left',
            'active_drag': 'box_zoom',
            'active_inspect': 'hover',
            'output_backend': 'webgl'
        }

        return figure(**figure_opts, title=title, tooltips=tooltips)

    
    @staticmethod
    def change_plot_settings(plot: figure):
        # Enable interactive legend
        plot.legend.click_policy = 'hide'
        
        # Move legend outside of plot
        plot.add_layout(plot.legend[0], 'right')

        # Add freehand drawing capabilities
        source = ColumnDataSource(dict(xs=[[0,0]], ys=[[0,0]]))
        r = plot.multi_line('xs', 'ys', source=source)
        tool = FreehandDrawTool(renderers=[r], empty_value=1)
        plot.add_tools(tool)

    
    @staticmethod
    def create_bode_plot(title: str) -> tuple[figure, figure]:
        mag_plot = Plotting.create_plot(title=f'{title} - Magnitude Plot',
                                        x_axis_name='Frequency',
                                        x_axis_unit='Hz',
                                        x_axis_type='log',
                                        y_axis_name='Magnitude',
                                        y_axis_unit='dB')

        phs_plot = Plotting.create_plot(title=f'{title} - Phase Plot',
                                        x_axis_name='Frequency',
                                        x_axis_unit='Hz',
                                        x_axis_type='log',
                                        y_axis_name='Phase',
                                        y_axis_unit='deg')
        phs_plot.x_range = mag_plot.x_range

        return mag_plot, phs_plot