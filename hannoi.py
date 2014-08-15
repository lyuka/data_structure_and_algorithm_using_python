# Print the moves required to solve the Towers of Hanoi puzzle.
def move( n, src, dst, tmp ):
    if n >= 1:
        move( n-1, src, tmp, dst )
        print "Move %d -> %d" % ( src, dst )
        move( n-1, tmp, dst, src )

print "moving tower of hanoi starts: "
move( 1, 1, 3, 2 )
