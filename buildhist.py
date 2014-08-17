# Prints a histogram for a distribution of letter grades computed
# from a collection of numeric grades extracted from a text file.

from maphist import Histogram

def main():
    gradeHist = Histogram( "ABCDEF" )
    gradeFile = open( 'cs101grades.txt', 'r' )
    for line in gradeFile:
        grade = int(line)
        gradeHist.incCount( letterGrade(grade) )
    printChart( gradeHist )
    print gradeHist.totalCount()
    gradeFile.close()

# Determines the letter grade for the given numeric value.
def letterGrade( grade ):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Prints the histogram as a horizontal bar chart.
def printChart( gradeHist ):
    print "         Grade Distribution"
    letters = ('A', 'B', 'C', 'D', 'F')
    for letter in letters:
        freq = gradeHist.getCount( letter )
        print ' |'
        print letter + "+" + '*' * freq
    print ' |'
    print ' +----+----+----+----+----+----+----+'
    print ' 0    5    10   15   20   25   30   35'

main()
