<h2><a href="https://leetcode.com/problems/stone-game-viii">1872. Stone Game VIII</a></h2><h3>Hard</h3><hr><p>Alice and Bob play a game with stones, with Alice going first.</p>

<p>There are <code>n</code> stones arranged in a row. You are given an integer array <code>stones</code> of length <code>n</code> where <code>stones[i]</code> is the value of the <code>i<sup>th</sup></code> stone from the left.</p>

<p>Alice and Bob take turns consisting of the following player&#39;s move:</p>

<ul>
	<li>Choose an integer <code>x</code> where <code>1 &lt; x &lt;= stones.length</code>.</li>
	<li>Remove the first <code>x</code> stones from the row.</li>
	<li>Place a new stone at the beginning of the row whose value is the sum of the removed stones&#39; values.</li>
	<li>The player&#39;s score increases by the sum of the removed stones&#39; values.</li>
</ul>

<p>The game ends when only one stone remains.</p>

<p>Each player&#39;s objective is to <strong>maximize</strong> the difference between their score and the opponent&#39;s score. Alice wants to maximize <code>(Alice&#39;s score - Bob&#39;s score)</code>, and Bob wants to minimize it (which is equivalent to maximizing <code>(Bob&#39;s score - Alice&#39;s score)</code>). Assuming both players play optimally, return the <em>difference between Alice&#39;s score and Bob&#39;s score.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stones = [-10,-12,35,18,10]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
- Alice merges the first 4 stones so the row becomes [31, 10] and Alice&#39;s score is 31.
- Bob merges the first 2 stones so the row becomes [41] and Bob&#39;s score is 41.
The difference is Alice&#39;s score - Bob&#39;s score = 31 - 41 = -10.
However, if Alice merges all 5 stones:
- Alice merges all 5 stones so the row becomes [41] and Alice&#39;s score is 41.
- Bob cannot make any moves since only one stone remains.
The difference is Alice&#39;s score - Bob&#39;s score = 41 - 0 = 41.
It can be shown that Alice cannot obtain a score difference greater than 5 if Bob plays optimally.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stones = [1,-2,-3,8]
<strong>Output:</strong> 5
<strong>Explanation:</strong>
- Alice merges the first 4 stones so the row becomes [4] and Alice&#39;s score is 4.
- Bob cannot make any moves. Score difference = 4.
- Alice merges the first 3 stones so the row becomes [4, 8] and Alice&#39;s score is -4.
- Bob merges the first 2 stones so the row becomes [12] and Bob&#39;s score is 12. Score difference = -4 - 12 = -16.
- Alice merges the first 2 stones so the row becomes [-1, -3, 8] and Alice&#39;s score is -1.
- Bob merges the first 3 stones so the row becomes [4] and Bob&#39;s score is 4. Score difference = -1 - 4 = -5.
- Alice merges the first 2 stones so the row becomes [-1, -3, 8] and Alice&#39;s score is -1.
- Bob merges the first 2 stones so the row becomes [-4, 8] and Bob&#39;s score is -4.
- Alice merges the first 2 stones so the row becomes [4] and Alice&#39;s score is 4. Score difference = -1 - (-4) + 4 = 7.
It can be shown that Alice cannot obtain a score difference greater than 5 if Bob plays optimally.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stones = [0,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
- Alice merges the first 2 stones so the row becomes [0] and Alice&#39;s score is 0.
- Bob cannot make any moves. Score difference = 0 - 0 = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == stones.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= stones[i] &lt;= 10<sup>4</sup></code></li>
</ul>
