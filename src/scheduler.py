def schedule(requests):
    req=sorted(requests, key=lambda x: -x['priority'])
    tl=[]; t=0
    for r in req:
        if r.get('sun',100)>85:
            tl.append({'id':r['id'],'start':t,'end':t+r['duration']})
            t+=r['duration']+5
    return {'scheduled':len(tl),'timeline':tl}
