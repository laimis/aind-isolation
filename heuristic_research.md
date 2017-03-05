# Tournament results

## First pass: number of open moves

*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 16 to 4
  Match 2: ID_Improved vs   MM_Null     Result: 11 to 9
  Match 3: ID_Improved vs   MM_Open     Result: 10 to 10
  Match 4: ID_Improved vs MM_Improved   Result: 9 to 11
  Match 5: ID_Improved vs   AB_Null     Result: 14 to 6
  Match 6: ID_Improved vs   AB_Open     Result: 11 to 9
  Match 7: ID_Improved vs AB_Improved   Result: 12 to 8


Results:
----------
ID_Improved         59.29%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 16 to 4
  Match 2:   Student   vs   MM_Null     Result: 15 to 5
  Match 3:   Student   vs   MM_Open     Result: 10 to 10
  Match 4:   Student   vs MM_Improved   Result: 15 to 5
  Match 5:   Student   vs   AB_Null     Result: 15 to 5
  Match 6:   Student   vs   AB_Open     Result: 10 to 10
  Match 7:   Student   vs AB_Improved   Result: 7 to 13


Results:
----------
Student             62.86%

This is a somewhat lucky result, as reruning again, Student outperforms ID_Improved but only slightly.


## Try random starting position

That performed purely, no surprise. Opening move is important, and at that point it is best to pick a set of opening moves that are advantagous, like a starting point:

*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 15 to 5
  Match 2: ID_Improved vs   MM_Null     Result: 17 to 3
  Match 3: ID_Improved vs   MM_Open     Result: 8 to 12
  Match 4: ID_Improved vs MM_Improved   Result: 14 to 6
  Match 5: ID_Improved vs   AB_Null     Result: 16 to 4
  Match 6: ID_Improved vs   AB_Open     Result: 13 to 7
  Match 7: ID_Improved vs AB_Improved   Result: 14 to 6


Results:
----------
ID_Improved         69.29%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 14 to 6
  Match 2:   Student   vs   MM_Null     Result: 16 to 4
  Match 3:   Student   vs   MM_Open     Result: 9 to 11
  Match 4:   Student   vs MM_Improved   Result: 12 to 8
  Match 5:   Student   vs   AB_Null     Result: 12 to 8
  Match 6:   Student   vs   AB_Open     Result: 13 to 7
  Match 7:   Student   vs AB_Improved   Result: 14 to 6


Results:
----------
Student             64.29%

## Trying out sticking to the center board more
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 17 to 3
  Match 2: ID_Improved vs   MM_Null     Result: 14 to 6
  Match 3: ID_Improved vs   MM_Open     Result: 10 to 10
  Match 4: ID_Improved vs MM_Improved   Result: 13 to 7
  Match 5: ID_Improved vs   AB_Null     Result: 16 to 4
  Match 6: ID_Improved vs   AB_Open     Result: 14 to 6
  Match 7: ID_Improved vs AB_Improved   Result: 13 to 7


Results:
----------
ID_Improved         69.29%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 16 to 4
  Match 2:   Student   vs   MM_Null     Result: 12 to 8
  Match 3:   Student   vs   MM_Open     Result: 11 to 9
  Match 4:   Student   vs MM_Improved   Result: 13 to 7
  Match 5:   Student   vs   AB_Null     Result: 14 to 6
  Match 6:   Student   vs   AB_Open     Result: 13 to 7
  Match 7:   Student   vs AB_Improved   Result: 10 to 10


Results:
----------
Student             63.57%

## Adding heuristic to avoid getting close to the walls:

Results:
----------
Student             72.14%
Student             71.43%
Student             65.43%
Student             70.00%
Student             65.71%

Match 7:   Student   vs AB_Improved   Result: 14 to 6
Match 7:   Student   vs AB_Improved   Result: 13 to 7
Match 7:   Student   vs AB_Improved   Result: 14 to 6
Match 7:   Student   vs AB_Improved   Result: 10 to 10
Match 7:   Student   vs AB_Improved   Result: 13 to 7
Match 7:   Student   vs AB_Improved   Result: 13 to 7