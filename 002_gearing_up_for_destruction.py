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

from fractions import Fraction

def solution(pegs):

    if len(pegs) == 2:
        # keeping in mind that we have "gears of any size, from a radius of 1 on up"
        # and that r0 = 2rn, we know that r0 must be at least 2 and rn at least 1.
        # therefore, in order to acomodate the minimum gears possible, the diference between p0 and p1 must be at least 3.
            ## wich is the same of checking if r >= 2.
        if (pegs[1] - pegs[0]) >= 3:
            r = 2/3 * (pegs[1] - pegs[0])
            r = Fraction(r).limit_denominator()
            return [r.numerator, r.denominator]
        # if it's not:
        else:
            return [-1, -1]


    else: #len list >=3
        len_pegs = len(pegs)
        s = 1
        p = pegs
        p1_to_pn_minus2 = 0

        for i in range(1,len_pegs-1):
            p1_to_pn_minus2 += s * p[i]
            s *= -1

        if len_pegs % 2: # Odd - IMPAR
            r = 2 * (-p[0] + 2*(p1_to_pn_minus2) - p[-1])
            #r = Fraction(r).limit_denominator()

        else: # Even - PAR
            r = 2/3 * (-p[0] + 2*(p1_to_pn_minus2) + p[-1])
            #r = Fraction(r).limit_denominator()

        # now that we now r we must check if it's bigger than 2 like we do when len == 2.
        if r < 2:
            return [-1,-1]

        # now we only need to check if the gears touch eachother and don't overlap
        else:
            #print ("r :", r)
            ri = r
            for i in range(1, len_pegs):
                #print ("ri : ", ri)
                #print ("i :", i)
                ri = p[i] - p[i-1] - ri
                #print ("rii :", rii)
###!!!!
                if ri < 1 or "cross the next!":
                    return [-1,-1]

        #print ("r : ", r)
        #print ("ri : ", ri)
        #if (r/2 != ri):
        #    print('over')
        #    return [-1,-1]


        r = Fraction(r).limit_denominator()
        return [r.numerator, r.denominator]


if __name__ == '__main__':
    #solution()
    #import timeit as t
    print("solution:", solution([0, 40, 80, 90]))
    #print(t.timeit(solution, number=100))
