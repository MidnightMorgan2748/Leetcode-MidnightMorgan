<h2><a href="https://leetcode.com/problems/stone-game-v">1563. Stone Game V</a></h2><h3>Hard</h3><hr><p>There are several stones <strong>arranged in a row</strong>, and each stone has an associated value which is an integer given in the array <code>stoneValue</code>.</p>

<p>There is a game played with these stones. In each turn, Alice divides the row into two <strong>non-empty</strong> rows (i.e. left row and right row).</p>

<p>Bob then calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice&#39;s score increases by the value of the remaining row. If the value of the two rows are equal, Alice decides which row to throw away and which row to keep. The next turn starts with the remaining row.</p>

<p>The game ends when only one stone remains. Alice&#39;s initial score is 0.</p>

<p>Return the maximum score that Alice can obtain.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [6,2,3,4,5,5]
<strong>Output:</strong> 18
<strong>Explanation:</strong> In the first turn, Alice divides the row to [6,2,3] and [4,5,5]. The left row has value 11 and the right row has value 14. Bob throws away the right row and Alice&#39;s score is now 11.
In the second turn, Alice divides the row to [6] and [2,3]. This time Bob throws away the left row and Alice&#39;s score becomes 11 + 5 = 16.
In the third turn, Alice divides the row to [2] and [3]. Bob throws away the right row and Alice&#39;s score becomes 16 + 2 = 18. The game ends because only one stone remains in the row.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [7,7,7,7,7,7,7]
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [4]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 500</code></li>
	<li><code>1 &lt;= stoneValue[i] &lt;= 10<sup>6</sup></code></li>
</ul>
