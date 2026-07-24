<h2><a href="https://leetcode.com/problems/number-of-unique-xor-triplets-ii">3514. Number of Unique XOR Triplets II</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>An <strong>XOR triplet</strong> is defined as the result of <code>nums[i] ^ nums[j] ^ nums[k]</code> for any indices <code>i</code>, <code>j</code>, and <code>k</code> such that <code>i &lt;= j &lt;= k</code>.</p>

<p>Return the total number of <strong>unique</strong> values produced by these XOR triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2, 1, 3]</span></p>
<p><strong>Output:</strong> <span class="example-io">4</span></p>
<p><strong>Explanation:</strong></p>
<p>The possible XOR triplets are:</p>
<ul>
    <li>For <code>i = j = k = 0</code>: <code>2 ^ 2 ^ 2 = 2</code></li>
    <li>For <code>i = j = 0, k = 1</code>: <code>2 ^ 2 ^ 1 = 1</code></li>
    <li>For <code>i = j = 0, k = 2</code>: <code>2 ^ 2 ^ 3 = 3</code></li>
    <li>For <code>i = 0, j = 1, k = 2</code>: <code>2 ^ 1 ^ 3 = 0</code></li>
</ul>
<p>The unique values obtained are 0, 1, 2, and 3. So, the output is 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1, 2, 4, 8]</span></p>
<p><strong>Output:</strong> <span class="example-io">15</span></p>
<p><strong>Explanation:</strong></p>
<p>Any combination of XOR triplets produces a unique value because all elements in the input are powers of two.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= nums.length &lt;= 1500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1500</code></li>
</ul>
