         to_merge = {var: [] for var in variables_to_merge}
 
         for ds in datasets:
             for var in variables_to_merge:
                if var in ds:
                    to_merge[var].append(ds.variables[var])
 
         for var in variables_to_merge:
             result_vars[var] = unique_variable(
