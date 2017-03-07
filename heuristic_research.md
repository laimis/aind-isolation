# Tournament results

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



## Different heuristic

Prefer the squares closest to the open squares:

*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 385 to 15
  Match 2: ID_Improved vs   MM_Null     Result: 371 to 29
  Match 3: ID_Improved vs   MM_Open     Result: 272 to 128
  Match 4: ID_Improved vs MM_Improved   Result: 264 to 136
  Match 5: ID_Improved vs   AB_Null     Result: 329 to 71
  Match 6: ID_Improved vs   AB_Open     Result: 240 to 160
  Match 7: ID_Improved vs AB_Improved   Result: 230 to 170


Results:
----------
ID_Improved         74.68%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 389 to 11
  Match 2:   Student   vs   MM_Null     Result: 368 to 32
  Match 3:   Student   vs   MM_Open     Result: 309 to 91
  Match 4:   Student   vs MM_Improved   Result: 298 to 102
  Match 5:   Student   vs   AB_Null     Result: 340 to 60
  Match 6:   Student   vs   AB_Open     Result: 265 to 135
  Match 7:   Student   vs AB_Improved   Result: 266 to 134


Results:
----------
Student             79.82%

A really good result, almost 4% improvement. Let's see what head to head matches look like

Here is head to head matches over 400 games:

Playing Matches:
----------
  Match 1:   Student   vs ID_Improved   Result: 238 to 162


Results:
----------
Student             59.50%

### combination of the above: prefer away from the walls and the closest to the open fields.

*************************
 Evaluating: ID_Improved
*************************

Playing Matches:
----------
  Match 1: ID_Improved vs   Random      Result: 379 to 21
  Match 2: ID_Improved vs   MM_Null     Result: 371 to 29
  Match 3: ID_Improved vs   MM_Open     Result: 280 to 120
  Match 4: ID_Improved vs MM_Improved   Result: 272 to 128
  Match 5: ID_Improved vs   AB_Null     Result: 332 to 68
  Match 6: ID_Improved vs   AB_Open     Result: 256 to 144
  Match 7: ID_Improved vs AB_Improved   Result: 232 to 168


Results:
----------
ID_Improved         75.79%

*************************
   Evaluating: Student
*************************

Playing Matches:
----------
  Match 1:   Student   vs   Random      Result: 387 to 13
  Match 2:   Student   vs   MM_Null     Result: 365 to 35
  Match 3:   Student   vs   MM_Open     Result: 302 to 98
  Match 4:   Student   vs MM_Improved   Result: 297 to 103
  Match 5:   Student   vs   AB_Null     Result: 354 to 46
  Match 6:   Student   vs   AB_Open     Result: 259 to 141
  Match 7:   Student   vs AB_Improved   Result: 243 to 157


Results:
----------
Student             78.82%
