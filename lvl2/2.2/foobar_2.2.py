import math

def answer(src, dest):
    ## pseudocode
    # [current_tiles] = start loc
    # while goal still in [remaining_tiles]
    #   generate moves from [current_tiles]
    #   remove them from [remaining_tiles]
    #   replace [current_tiles] with generated moves
    #   iterate move counter
    # return move counter
    ##
    
    # initial values
    remaining_tiles = set()
    gen_moves = set()
    current_tiles = {src}
    moves = 0
    
    # populate tile set
    for x in range(64):
        remaining_tiles.add(x)
        
    # remove source tile
    remaining_tiles.remove(src)
        
    # while we have not found the destination tile
    while dest in remaining_tiles:
        # loop through our current tiles and make all moves from them
        for n in current_tiles:
            x, y = int_to_coord(n)
            # add all moves from current tile
            if x-1 >= 0:
                if y-2 >= 0:
                    gen_moves.add(coord_to_int(x-1, y-2))
                if y+2 <= 7:
                    gen_moves.add(coord_to_int(x-1, y+2))
            if x+1 <= 7:
                if y-2 >= 0:
                    gen_moves.add(coord_to_int(x+1, y-2))
                if y+2 <= 7:
                    gen_moves.add(coord_to_int(x+1, y+2))
            if x-2 >= 0:
                if y-1 >= 0:
                    gen_moves.add(coord_to_int(x-2, y-1))
                if y+1 <= 7:
                    gen_moves.add(coord_to_int(x-2, y+1))
            if x+2 <= 7:
                if y-1 >= 0:
                    gen_moves.add(coord_to_int(x+2, y-1))
                if y+1 <= 7:
                    gen_moves.add(coord_to_int(x+2, y+1))
        
        # remove moves from remaining tiles (make the moves)
        remaining_tiles.difference_update(gen_moves)
        # update current_tiles and reset gen_moves for the next loop
        current_tiles = gen_moves.copy()
        gen_moves.clear()
        # iterate move counter
        moves+=1
        
    return moves

# helper functions        
def int_to_coord(n):
    return n%8, int(math.floor(n/8))
    
def coord_to_int(x, y):
    return (y*8)+x