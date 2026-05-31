 
     def __call__(self, data, groupby, orient, scales):
 
        return (
            groupby
            .apply(data.dropna(subset=["x", "y"]), self._fit_predict)
        )
 
 
 @dataclass
