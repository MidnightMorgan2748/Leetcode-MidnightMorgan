<h2><a href="https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target">3720. Lexicographically Smallest Permutation Greater Than Target</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>s</code> and <code>target</code> of the same length.</p>

<p>Return the <strong>lexicographically smallest</strong> permutation of <code>s</code> that is <strong>strictly greater</strong> than <code>target</code>. If there is no such permutation, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abc", target = "bba"</span></p>

<p><strong>Output:</strong> <span class="example-io">"bca"</span></p>

<p><strong>Explanation:</strong></p>

<p>The permutations of <code>s</code> are <code>"abc"</code>, <code>"acb"</code>, <code>"bac"</code>, <code>"bca"</code>, <code>"cab"</code>, and <code>"cba"</code>. The smallest permutation strictly greater than <code>"bba"</code> is <code>"bca"</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "leet", target = "code"</span></p>

<p><strong>Output:</strong> <span class="example-io">"eelt"</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest permutation of <code>"leet"</code> strictly greater than <code>"code"</code> is <code>"eelt"</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "baba", target = "bbaa"</span></p>

<p><strong>Output:</strong> <span class="example-io">""</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no permutation of <code>s</code> strictly greater than <code>target</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>target</code> consist only of lowercase English letters.</li>
</ul>
