<h2><a href="https://leetcode.com/problems/maximize-active-section-with-trade-i">3499. Maximize Active Section with Trade I</a></h2><h3>Medium</h3><hr><p>You are given a binary string <code>s</code> consisting of '0's and '1's.</p>

<p>A <strong>trade</strong> consists of the following steps in order:</p>
<ol>
    <li>Choose a contiguous block of '1's that is <strong>surrounded</strong> by '0's and convert all its characters to '0's.</li>
    <li>Convert a contiguous block of '0's that is <strong>surrounded</strong> by '1's to all '1's.</li>
</ol>

<p>You can perform at most one trade. Return the <strong>maximum</strong> number of '1's that can be achieved in the string <code>s</code> after performing at most one trade.</p>

<p><strong>Note:</strong></p>
<ul>
    <li>For the purpose of identifying "surrounded" blocks, the string <code>s</code> is treated as if it has a '1' at both ends (i.e. <code>t = '1' + s + '1'</code>). These virtual '1's do not count towards the final count of '1's in <code>s</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "000100"</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p>By trading the '1' at index 3, we can convert the '0' blocks at indices 0-2 and 4-5. The string becomes "111110", which has 5 '1's.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "10101"</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p>No trade is needed. The string already has 3 '1's, and we can achieve 5 '1's by trading the '0' at index 1 and the '0' at index 3.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either '0' or '1'.</li>
</ul>
