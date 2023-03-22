Dear Student,

I regret to inform you that you've received only **2** out of 10 points for this assignment.
<details><summary>You have already managed to pass 2 tests, so that is encouraging!</summary>&emsp;☑&nbsp;[1p] Tableau properly determines optimal solutions<br>&emsp;☑&nbsp;[1p] Tableau properly chooses entering variable</details>

There still exist some issues that should be addressed before the deadline: **2023-03-29 07:59:00 CEST (+0200)**. For further details, please refer to the following list:

<details><summary>[1p] Tableau properly checking if unbounded &gt;&gt; tableau is unable to detect unbounded problem:</summary>- for column with coefficients [-1, -2, 3] it should've returned False, it has not :(</details>
<details><summary>[2p] Tableau properly chooses leaving variable &gt;&gt; tableau is unable to choose leaving variable properly:</summary>- for column [0, -2, 1000001] and bounds column [0, 1, 9] it should've returned 2, instead it has produced -1</details>
<details><summary>[3p] Tableau properly pivots &gt;&gt; Tested code raises NotImplementedError in tableau.py:125</summary></details>
<details><summary>[1p] Example 02 finds correct solution &gt;&gt; model does not have constraints</summary></details>
<details><summary>[1p] Example 03 finds unbounded problem &gt;&gt; model does not have constraints</summary></details>

-----------
I remain your faithful servant\
_Bobot_