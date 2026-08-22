<h2><a href="https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product">3622. Check Divisibility by Digit Sum and Product</a></h2><h3>Easy</h3><hr><p>You are given a positive integer <code>n</code>.</p>

<p>An integer is divisible by the sum of its digits and the product of its digits combined if <code>n % (digit_sum + digit_product) == 0</code>.</p>

<p>Return <code>true</code> if <code>n</code> is divisible by the sum and product of its digits combined, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 99</span></p>
<p><strong>Output:</strong> <span class="example-io">true</span></p>
<p><strong>Explanation:</strong></p>
<ul>
    <li>Digit sum = <code>9 + 9 = 18</code>.</li>
    <li>Digit product = <code>9 * 9 = 81</code>.</li>
    <li>Sum of digit sum and digit product = <code>18 + 81 = 99</code>.</li>
    <li>Since 99 is divisible by 99, we return <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 23</span></p>
<p><strong>Output:</strong> <span class="example-io">false</span></p>
<p><strong>Explanation:</strong></p>
<ul>
    <li>Digit sum = <code>2 + 3 = 5</code>.</li>
    <li>Digit product = <code>2 * 3 = 6</code>.</li>
    <li>Sum of digit sum and digit product = <code>5 + 6 = 11</code>.</li>
    <li>Since 23 is not divisible by 11, we return <code>false</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>
