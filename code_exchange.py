from itertools import combinations

##==================================================
## reduce hidden (2, 3, 4) pairs
##==================================================
def reduce_possible_from_hidden_pair(dictPossible, target):     # e.g. ((5, 7, 9, 6), {(6, 1), (8, 1), (7, 0), (6, 0)})
    reduced = False
    for tgt in target:
        source, to_keep = tgt[1], tgt[0]
        for s in source:
            if dictPossible[s] != [v for v in dictPossible[s] if v in to_keep]:
                reduced = True
                print(f"reduce a hidden pair,", tgt)
                dictPossible[s] = [v for v in dictPossible[(x,i)] if v in to_keep]
    return reduced

def check_hidden_pairs(dictPossible, block):
    reduced = False
    # convert possible list in a block to number & cell pair 
    pair=[(i,b[0]) for b in block for i in b[1] if b[1]!=[]]
    # grouping the same number by combining their cells into a list
    grouped={}
    [grouped.setdefault(key,[]).append(value) for key, value in pair]
    #print(grouped)
    # discover and reduce hidden 2-number pairs
    target = [(n, set(grouped[n[0]]+grouped[n[1]])) for n in list(combinations(grouped,2)) if len(n)==len(set(grouped[n[0]]+grouped[n[1]]))]
    block_reduced = reduce_possible_from_hidden_pair(dictPossible, target)
    reduced = reduced or block_reduced
    # discover and reduce hidden 3-number pairs
    target = [(n, set(grouped[n[0]]+grouped[n[1]]+grouped[n[2]])) for n in list(combinations(grouped,3)) if len(n)==len(set(grouped[n[0]]+grouped[n[1]]+grouped[n[2]]))]
    block_reduced = reduce_possible_from_hidden_pair(dictPossible, target)
    reduced = reduced or block_reduced
    # discover and reduce hidden 4-number pairs
    target = [(n, set(grouped[n[0]]+grouped[n[1]]+grouped[n[2]]+grouped[n[3]]))  for n in list(combinations(grouped,4)) if len(n)==len(set(grouped[n[0]]+grouped[n[1]]+grouped[n[2]]+grouped[n[3]]))]
    block_reduced = reduce_possible_from_hidden_pair(dictPossible, target)
    reduced = reduced or block_reduced

def reduce_hidden_pair(puzzle, dictPossible):
    for i in range(9):
        # check horizental block
        block = [d for d in dictPossible.items() if d[0][0]==i]
        check_hidden_pairs(dictPossible, block)

        # check vertical block
        block = [d for d in dictPossible.items() if d[0][1]==i]
        check_hidden_pairs(dictPossible, block)

    for x in range(0,9,3):
        for y in range(0,9,3):
            block = [d for i in range(x//3*3,x//3*3+3) for j in range(y//3*3,y//3*3+3) for d in dictPossible.items() if (i,j)==d[0]]
            check_hidden_pairs(dictPossible, block)

printPuzzle(puzzle, dictPossible)
