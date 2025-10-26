There are `n` people standing in a circle waiting to be executed. The counting out begins
at some point in the circle and proceeds around the circle in a fixed direction. In each
step, a certain number of people are skipped and the next person is executed. The
elimination proceeds around the circle (which is becoming smaller and smaller as the
executed people are removed), until only the last person remains, who is given freedom.
Given the total number of persons `n` and a number `k` (the step count) which indicates
that `k-1` persons are skipped and `k`th person is killed in circle. The task is to find
out which person will survive.

### Example

In this example, 5 people are placed in a circle (`n = 5`), and the step count is 2 (`k = 2`).

<pre>
      [1]
     /   \
  [5]     [2]
   |       |
  [4]-----[3]
</pre>

The count starts at person 1, and person 2 is executed:

<pre>
      [1]
     /   \
  [5]     <span style="color: red">[2] X</span>
   |       |
  [4]-----[3]
</pre>

The count now starts at person 3, and person 4 is executed:

<pre>
      [1]
     /   \
  [5]     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

The count now starts a person 5, and person 1 is executed:

<pre>
      <span style="color: red;">[1] X</span>
     /   \
  [5]     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

The count now starts at person 3, and person 5 is executed:

<pre>
      <span style="color: red;">[1] X</span>
     /   \
<span style="color: red;">X [5]</span>     <span style="color: red;">[2] X</span>
   |       |
<span style="color: red;">X [4]</span>-----[3]
</pre>

At the end, person 3 is the survivor.
