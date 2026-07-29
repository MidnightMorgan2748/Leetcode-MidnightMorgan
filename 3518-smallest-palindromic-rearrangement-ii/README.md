<h2><a href="https://leetcode.com/problems/smallest-palindromic-rearrangement-ii">3518. Smallest Palindromic Rearrangement II</a></h2><h3>Hard</h3><hr><p>You are given a palindromic string <code>s</code> and an integer <code>k</code>.</p>

<p>Return the <code>k<sup>th</sup></code> lexicographically smallest palindromic permutation of <code>s</code>. If there are fewer than <code>k</code> distinct palindromic permutations of <code>s</code>, return an empty string <code>""</code>.</p>

<p>Note that if two rearrangements yield the same palindromic string, they are not distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "aabb", k = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">"abba"</span></p>
<p><strong>Explanation:</strong></p>
<p>The distinct palindromic permutations of "aabb" are:</p>
<ol>
    <li>"abba"</li>
    <li>"baab"</li>
</ol>
<p>The 1<sup>st</sup> smallest is "abba".</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "aabb", k = 3</span></p>
<p><strong>Output:</strong> <span class="example-io">""</span></p>
<p><strong>Explanation:</strong></p>
<p>There are only 2 distinct palindromic permutations of "aabb", so we return <code>""</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "ab", k = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">""</span></p>
<p><strong>Explanation:</strong></p>
<p>No palindromic permutation can be formed from "ab".</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> is a palindrome.</li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
