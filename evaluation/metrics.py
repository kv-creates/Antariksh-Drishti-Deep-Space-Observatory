def precision(tp,fp):
    return tp/max(1,tp+fp)

def recall(tp,fn):
    return tp/max(1,tp+fn)
