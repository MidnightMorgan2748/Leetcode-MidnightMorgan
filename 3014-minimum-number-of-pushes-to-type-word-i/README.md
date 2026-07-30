<h2><a href="https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i">3014. Minimum Number of Pushes to Type Word I</a></h2><h3>Easy</h3><hr><p>You are given a string <code>word</code> containing distinct lowercase English letters.</p>

<p>Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be repositioned to form alternative mappings. Some keys such as <code>1</code>, <code>*</code>, <code>#</code>, and <code>0</code> do not map to any letters.</p>

<p>Our goal is to map the letters of <code>word</code> to keys <code>2</code> through <code>9</code> such that each letter is mapped to exactly one key. A key can have any number of letters mapped to it.</p>

<p>Return the <strong>minimum</strong> number of keypresses needed to type <code>word</code> using the mapped keys.</p>

<p><em>Note that the map mapping can be optimal in any way, and characters in <code>word</code> are distinct.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypad1.png" style="width: 329px; height: 313px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "abcde"</span></p>
<p><strong>Output:</strong> <span class="example-io">5</span></p>
<p><strong>Explanation:</strong></p>
<p>The remapped keypad shown in the image gives the minimum pushes.</p>
<p>We type the letters:
- "a" by pressing key 2 once (1 push)
- "b" by pressing key 3 once (1 push)
- "c" by pressing key 4 once (1 push)
- "d" by pressing key 5 once (1 push)
- "e" by pressing key 6 once (1 push)
Total keypresses = 1 + 1 + 1 + 1 + 1 = 5.</p>
</div>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypad2a.png" style="width: 329px; height: 313px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "xycdefghij"</span></p>
<p><strong>Output:</strong> <span class="example-io">12</span></p>
<p><strong>Explanation:</strong></p>
<p>The remapped keypad shown in the image gives the minimum pushes.</p>
<p>We type the letters:
- "c", "d", "e", "f", "g", "h", "i", "j" by pressing keys 2, 3, 4, 5, 6, 7, 8, 9 once respectively (8 pushes)
- "x" by pressing key 2 twice (2 pushes)
- "y" by pressing key 3 twice (2 pushes)
Total keypresses = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 2 = 12.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= word.length &lt;= 26</code></li>
	<li><code>word</code> consists of distinct lowercase English letters.</li>
</ul>
