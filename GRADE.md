Dear Student,

I regret to inform you that you've received only **4** out of 10 points for this assignment.
<details><summary>You have already managed to pass 3 tests, so that is encouraging!</summary>&emsp;☑&nbsp;[1p] Tableau properly determines optimal solutions<br>&emsp;☑&nbsp;[1p] Tableau properly chooses entering variable<br>&emsp;☑&nbsp;[2p] Tableau properly chooses leaving variable</details>

There still exist some issues that should be addressed before the deadline: **2023-03-29 07:59:00 CEST (+0200)**. For further details, please refer to the following list:

<details><summary>[1p] Tableau properly checking if unbounded &gt;&gt; tableau is unable to detect unbounded problem:</summary>- for column with coefficients [-1, -2, 3] it should've returned False, it has not :(</details>
<details><summary>[3p] Tableau properly pivots &gt;&gt; tableau incorrectly pivots a table:</summary>- init table:<br>[[ 0. -1. -2.  0.  0.  0.  0.  0.  0.]<br>&nbsp;[ 1.  1.  0.  0.  0.  0.  0.  0.  1.]<br>&nbsp;[ 0. -1.  1.  0.  0. -1.  0.  0.  2.]<br>&nbsp;[-1.  0.  1.  0.  0.  0. -1.  0.  3.]<br>&nbsp;[-1.  0. -1.  0.  0.  0.  0.  0.  4.]<br>&nbsp;[ 0. -1.  1.  1.  0.  0.  0.  0.  5.]<br>&nbsp;[ 1.  0. -1.  0.  1.  0.  0.  0.  6.]<br>&nbsp;[-1.  1.  0.  0.  0.  0.  0. -1.  0.]]<br>- pivot coords (2, 2)<br>- expected result:<br>[[ 0. -3.  0.  0.  0. -2.  0.  0.  4.]<br>&nbsp;[ 1.  1.  0.  0.  0.  0.  0.  0.  1.]<br>&nbsp;[ 0. -1.  1.  0.  0. -1.  0.  0.  2.]<br>&nbsp;[-1.  1.  0.  0.  0.  1. -1.  0.  1.]<br>&nbsp;[-1. -1.  0.  0.  0. -1.  0.  0.  6.]<br>&nbsp;[ 0.  0.  0.  1.  0.  1.  0.  0.  3.]<br>&nbsp;[ 1. -1.  0.  0.  1. -1.  0.  0.  8.]<br>&nbsp;[-1.  1.  0.  0.  0.  0.  0. -1.  0.]]<br>- got:<br>[[ 0. -1. -2.  0.  0.  0.  0.  0.  0.]<br>&nbsp;[ 1.  1.  0.  0.  0.  0.  0.  0.  1.]<br>&nbsp;[ 0. -1.  1.  0.  0. -1.  0.  0.  2.]<br>&nbsp;[-1.  0.  1.  0.  0.  0. -1.  0.  3.]<br>&nbsp;[-1.  0. -1.  0.  0.  0.  0.  0.  4.]<br>&nbsp;[ 0. -1.  1.  1.  0.  0.  0.  0.  5.]<br>&nbsp;[ 1.  0. -1.  0.  1.  0.  0.  0.  6.]<br>&nbsp;[-1.  1.  0.  0.  0.  0.  0. -1.  0.]]</details>
<details><summary>[1p] Example 02 finds correct solution &gt;&gt; model does not have constraints</summary></details>
<details><summary>[1p] Example 03 finds unbounded problem &gt;&gt; model does not have constraints</summary></details>

-----------
I remain your faithful servant\
_Bobot_