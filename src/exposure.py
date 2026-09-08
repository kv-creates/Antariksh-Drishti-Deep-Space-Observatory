def exptime(snr_target=10, flux=1000):
    return round((snr_target**2*1100)/(flux**2)*100,2)
