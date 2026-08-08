<h2><a href="https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence">3302. Find the Lexicographically Smallest Valid Sequence</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>word1</code> and <code>word2</code>.</p>

<p>A string <code>x</code> is called <strong>almost equal</strong> to <code>y</code> if we can change at most one character in <code>x</code> to make it equal to <code>y</code>.</p>

<p>A sequence of indices <code>seq</code> of length <code>m</code> is called <strong>valid</strong> if:</p>
<ul>
    <li>The indices are in increasing order (i.e. <code>seq[i] &lt; seq[i+1]</code>).</li>
    <li>The string formed by concatenating the characters at indices <code>seq[0], seq[1], ..., seq[m - 1]</code> of <code>word1</code> is <strong>almost equal</strong> to <code>word2</code>.</li>
</ul>

<p>Return the <strong>lexicographically smallest</strong> valid sequence of indices of length <code>word2.length</code>. If no such sequence exists, return an <strong>empty</strong> array.</p>

<p>Note that the sequence of indices <code>seq1</code> is lexicographically smaller than <code>seq2</code> if at the first index <code>i</code> where they differ, <code>seq1[i] &lt; seq2[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = "vbcca", word2 = "abc"</span></p>
<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>
<p><strong>Explanation:</strong></p>
<p>The lexicographically smallest valid sequence of indices is <code>[0, 1, 2]</code>:</p>
<ul>
    <li>The concatenated string is <code>word1[0] + word1[1] + word1[2] = "vbc"</code>.</li>
    <li><code>"vbc"</code> is almost equal to <code>"abc"</code> (by changing the first character from 'v' to 'a').</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = "bacdc", word2 = "abc"</span></p>
<p><strong>Output:</strong> <span class="example-io">[1,2,4]</span></p>
<p><strong>Explanation:</strong></p>
<p>The lexicographically smallest valid sequence of indices is <code>[1, 2, 4]</code>:</p>
<ul>
    <li>The concatenated string is <code>word1[1] + word1[2] + word1[4] = "acc"</code>.</li>
    <li><code>"acc"</code> is almost equal to <code>"abc"</code> (by changing the second character from 'c' to 'b').</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = "aaaaaa", word2 = "aaabc"</span></p>
<p><strong>Output:</strong> <span class="example-io">[]</span></p>
<p><strong>Explanation:</strong></p>
<p>There is no valid sequence of indices of length 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= word2.length &lt;= word1.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>word1</code> and <code>word2</code> consist only of lowercase English letters.</li>
</ul>
