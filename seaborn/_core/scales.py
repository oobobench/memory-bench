                 vmin, vmax = data.min(), data.max()
             else:
                 vmin, vmax = new.norm
            vmin, vmax = map(float, axis.convert_units((vmin, vmax)))
             a = forward(vmin)
             b = forward(vmax) - forward(vmin)
 
