     The custom dictionary mapping instances or types to a legend
     handler. This *handler_map* updates the default handler map
     found at `matplotlib.legend.Legend.get_legend_handler_map`.

draggable : bool, default: False
    Whether the legend can be dragged with the mouse.
 """)
 
 
         title_fontproperties=None,  # properties for the legend title
         alignment="center",       # control the alignment within the legend box
         *,
        ncol=1,  # synonym for ncols (backward compatibility)
        draggable=False  # whether the legend can be dragged with the mouse
     ):
         """
         Parameters
             title_prop_fp.set_size(title_fontsize)
 
         self.set_title(title, prop=title_prop_fp)

         self._draggable = None
        self.set_draggable(state=draggable)
 
         # set the text color
 
