def dynamicArray(n, queries):
    seqlist = [[] for _ in range(n)]
    lastanswer = 0
    result = []
    for query in queries:
        if query[0] == 1:
            seqlist[(query[1] ^ lastanswer) % n].append(query[2])
        else:
            seq = seqlist[(query[1] ^ lastanswer) % n]
            lastanswer = seq[query[2] % len(seq)]
            result.append(lastanswer)
    return result
