def SorensenEval(inter,gen,stat):
    Sorensen = (2*inter / (gen+stat)) 
    return Sorensen
def JaccardEval(inter,gen,stat):
    Jaccard = (inter / (gen+stat-inter)) 
    return Jaccard
def HammingDist(gen, stat):
    dist_counter = 0
    for n in range(len(stat)):
        if gen[n] != stat[n]:
            dist_counter += 1
    return dist_counter