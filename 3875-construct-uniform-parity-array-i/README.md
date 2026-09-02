<h2><a href="https://leetcode.com/problems/construct-uniform-parity-array-i">3875. Construct Uniform Parity Array I</a></h2><h3>Easy</h3><hr><p>You are given an array <code>nums1</code> of <code>n</code> <strong>distinct</strong> integers.</p>

<p>You want to construct an array <code>nums2</code> of length <code>n</code> such that all elements in <code>nums2</code> have the <strong>same parity</strong> (either all odd or all even).</p>

<p>For each index <code>i</code> (<code>0 &lt;= i &lt; n</code>), you must choose <strong>exactly one</strong> of the following:</p>

<ul>
	<li><code>nums2[i] = nums1[i]</code></li>
	<li><code>nums2[i] = nums1[i] - nums1[j]</code> where <code>j != i</code></li>
</ul>

<p>Return <code>true</code> if it is possible to construct such an array, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [2,4,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>We can set <code>nums2 = nums1 = [2,4,6]</code>. All elements are even, so they have the same parity.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 100</code></li>
	<li>All elements of <code>nums1</code> are distinct.</li>
</ul>
