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


## Trying out sticking to the center board more
*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 388 to 12
  Match 2: ID_Improved vs   MM_Null     Result: 364 to 36
  Match 3: ID_Improved vs   MM_Open     Result: 270 to 130
  Match 4: ID_Improved vs MM_Improved   Result: 264 to 136
  Match 5: ID_Improved vs   AB_Null     Result: 346 to 54
  Match 6: ID_Improved vs   AB_Open     Result: 250 to 150
  Match 7: ID_Improved vs AB_Improved   Result: 226 to 174


Results:
----------
ID_Improved         75.29%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 382 to 18
  Match 2:   Student   vs   MM_Null     Result: 376 to 24
  Match 3:   Student   vs   MM_Open     Result: 298 to 102
  Match 4:   Student   vs MM_Improved   Result: 271 to 129
  Match 5:   Student   vs   AB_Null     Result: 338 to 62
  Match 6:   Student   vs   AB_Open     Result: 252 to 148
  Match 7:   Student   vs AB_Improved   Result: 232 to 168


Results:
----------
Student             76.75%

This is very close to ID_Improved, at the same time it does look like a tiny improvement over it.

To examine further, let's pit the two algos against each other:

Playing Matches:
----------
  Match 1:   Student   vs ID_Improved   Result: 205 to 195

Results:
----------
Student             51.25%


Playing Matches:
----------
  Match 1:   Student   vs ID_Improved   Result: 323 to 277

Results:
----------
Student             53.83%

As the number of games increases, the advantage seems to hold up even though again, it is not incredible high.

