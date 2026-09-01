<h2><a href="https://leetcode.com/problems/minimum-moves-to-clean-the-classroom">3568. Minimum Moves to Clean the Classroom</a></h2><h3>Medium</h3><hr><p>You are given an <code>m x n</code> grid <code>classroom</code> and an integer <code>energy</code>.</p>

<p>The classroom grid contains the following characters:</p>
<ul>
	<li><code>'S'</code>: The starting position.</li>
	<li><code>'L'</code>: A litter location that needs to be cleaned.</li>
	<li><code>'R'</code>: A recharge area where you can restore your energy back to <code>energy</code>.</li>
	<li><code>'X'</code>: An obstacle that cannot be stepped on.</li>
	<li><code>'.'</code>: An empty space.</li>
</ul>

<p>You start at <code>'S'</code> with an initial energy of <code>energy</code>. In one move, you can walk to an adjacent cell (up, down, left, or right) if it is not an obstacle <code>'X'</code>. Each move consumes <code>1</code> unit of energy.</p>

<p>If you move into a recharge cell <code>'R'</code>, your energy is immediately restored to <code>energy</code>.</p>

<p>You cannot move if your energy reaches <code>0</code>, unless you are on a recharge cell <code>'R'</code>.</p>

<p>When you visit a litter cell <code>'L'</code>, it is immediately collected. You can revisit cells multiple times.</p>

<p>Return the <strong>minimum number of moves</strong> required to collect all litter items, or <code>-1</code> if it is impossible to collect all of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> classroom = ["S.L","...","L.R"], energy = 4
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> classroom = ["S.X","R.L"], energy = 2
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> classroom = ["S.X","X.L"], energy = 5
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == classroom.length</code></li>
	<li><code>n == classroom[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 20</code></li>
	<li><code>classroom[i][j]</code> is one of <code>'S'</code>, <code>'L'</code>, <code>'R'</code>, <code>'X'</code>, or <code>'.'</code>.</li>
	<li>There is exactly one <code>'S'</code> in the grid.</li>
	<li>The number of <code>'L'</code> cells is at most <code>10</code>.</li>
	<li><code>1 &lt;= energy &lt;= 50</code></li>
</ul>
