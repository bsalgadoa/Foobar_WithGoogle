'''
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution({4, 17, 50})
Output:
    -1,-1

Input:
Solution.solution({4, 30, 50})
Output:
    12,1

-- Python cases --
Input:
solution.solution([4, 30, 50])
Output:
    12,1

Input:
solution.solution([4, 17, 50])
Output:
    -1,-1
'''

## References:
    # https://docs.python.org/3/library/fractions.html
    # https://realpython.com/python-fractions/

## Notes:
    # r is always the radius of the first gear, r = r0
    # Python 2.7.13 sandbox (!)

## Approach:
    # I first tried to solve this problem for 3 gears (p[0], p[1] and p[2])
        # considering p[2]-p[0] = 3r2 + 2r1, it didn't went as expected so,
        # instead of considering 3r2, I tried to solve it again this time replacing 3r2 for r + r2 (r = 2r2)
        # total distance = p[2]-p[0] = 2r + 2r1 + r2
        # from here I deducted that:
            # d0 = p[1] - p[0] = r + r1
            # d1 = p[2] - p[1] = r1 + r2
            # dn = p[n+1] - p[n] = rn + rn+1
            # and we know that r = 2r2 (for n=2), so r = 2rn (for n)
        # this means that we'll always have n equations to n gears and therefore
        # be able to find r for n gears.

        # from here I first solved for 3 gears as follows:
            # p[1] - p[0] = r + r1      r1 = p[1] - p[0] - 2r2
            # p[2] - p[1] = r1 + r2 <=> r2 = p[2] - 2p1 + p[0] + 2r2
            # r = r2                    r = 2 * (-p[0] + 2p[1] - p[2]) <<<

        # Then I solved for 4 gears, 5 and 6, and noticed that
        # a patern emerges in r when the number of gears is odd or even:
            # len == 3:
            #     r = 2 * (-p[0] + 2p[1] - p[2])
            # len == 4:
            #     r = 2/3 * (-p[0] + 2p[1] - 2p[2] + p[3])
            # len == 5:
            #     r = 2 * (-p[0] + 2p[1] - 2p[2] + 2p[3] - p[4])
            # len == 6:
            #     r = 2/3 * (-p[0] + 2p[1] - 2p[2] + 2p[3] - 2p[4] + p[5])

        # we can simplify and state that if lenght is:
            # even:
                # r = 2/3 * (-p[0] + 2*(sum p1_to_pn_minus2) + p[-1])
            # odd:
                # r = 2 * (-p[0] + 2*(sum p1_to_pn_minus2) + p[-1])

    # Now that we've found a way to determine r
    # in order to determine if it's possible and if so, return the solution
        # we must make sure that:
            # r >= 2, because the minimum radius is 1 and r = 2rn.
            # and also that all the gears have radius >= 1.
                # note: overlaping gears or gears that don't touch, means that there will be gears with radius < 1.

        # if so, return the r in a fraction in its simple form.


from fractions import Fraction

def solution(pegs):

    ## only two gears:
    if len(pegs) == 2:
        # r == 2/3 and r1 == 1/3 of the distance between gears
        r = 2/3.0 * (pegs[1] - pegs[0])

        # and r must be > 2 ->> "(...)from a radius of 1 on up"
        if r < 2:
            return [-1, -1]

    ## more than 2 gears:
    else:
        p = pegs # readability simplification.
        p1_to_pn_minus2 = 0 # store the sum of p's, for every p between p[1] to p[n-2].
        ### s = 1 # firs approach to invert the signal while calculating p1_to_pn_minus2.

        # determine p1_to_pn_minus2:
        # p1_to_pn_minus2 sum inverts the signal (+ or -) for every p[n] between p[1] to p[n-2].
        for i in range(1,len(pegs)-1):
            p1_to_pn_minus2 += ((-1)**(i+1)) * p[i]

            ### first approach to invert +/-:
                ### used -1*s to do so:
                ### p1_to_pn_minus2 += s * p[i]
                ### s *= -1

        # now we can determine r:
        if len(pegs) % 2: # odd
            r = 2 * (-p[0] + 2*(p1_to_pn_minus2) - p[-1])

        else: # even
            r = 2/3.0 * (-p[0] + 2*(p1_to_pn_minus2) + p[-1])

        # again r must allways be > 2 ->> "(...)from a radius of 1 on up"
        if r < 2:
            return [-1,-1]

        # now we only need to check if all the other gears are >= 1
        ri = r
        for i in range(1, len(pegs) ):
            ri = p[i] - p[i-1] - ri
            if ri < 1:
                return [-1,-1]

    # if the configuration is possible
    # we convert r to a fraction "in its simplest form" using limit_denominator:
    r = Fraction(r).limit_denominator()

    return [r.numerator, r.denominator]



if __name__ == '__main__':
    #solution()
    #import timeit as t
    print("solution:", solution([10,50,80,110]))
    #print(t.timeit(solution, number=100))
