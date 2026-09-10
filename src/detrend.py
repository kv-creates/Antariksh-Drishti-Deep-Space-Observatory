def median_detrend(flux, w=11):
    import statistics
    return [x-statistics.median(flux) for x in flux]
