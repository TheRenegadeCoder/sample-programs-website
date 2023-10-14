<style>
    .matrix {
        text-align: center;
    }

    .empty {
        background-color: transparent;
    }

    .right {
        text-align: right;
    }
</style>

In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal; 
that is, it switches the row and column indices of the matrix A by producing another matrix, often 
denoted by A<sup>T</sup>. For example, the following matrix could be the matrix A:

<table class="matrix">
    <tr>
        <th class="empty;">&nbsp;</th>
        <th>column 1</th>
        <th>column 2</th>
        <th>column 3</th>
    </tr>
    <tr>
        <th class="right">row 1</th>
        <td>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <th class="right">row 2</th>
        <td>4</td>
        <td>5</td>
        <td>6</td>
    </tr>
    <tr>
        <th class="right">row 3</th>
        <td>7</td>
        <td>8</td>
        <td>9</td>
    </tr>
</table>

Once transposed, A becomes the following matrix, A<sup>T</sup>:

<table class="matrix">
    <tr>
        <th class="empty">&nbsp;</th>
        <th>column 1</th>
        <th>column 2</th>
        <th >column 3</th>
    </tr>
    <tr>
        <th class="right">row 1</th>
        <td>1</td>
        <td>4</td>
        <td>7</td>
    </tr>
    <tr>
        <th class="right">row 2</th>
        <td>2</td>
        <td>5</td>
        <td>8</td>
    </tr>
    <tr>
        <th class="right">row 3</th>
        <td>3</td>
        <td>6</td>
        <td>9</td>
    </tr>
</table>

The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.
