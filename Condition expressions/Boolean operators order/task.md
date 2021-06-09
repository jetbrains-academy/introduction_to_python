## Boolean operators order

Python evaluates expressions from left to right. Notice that while evaluating an 
assignment, the right-hand side is evaluated before the left-hand side.

The table below should give you an idea about the operator precedence in Python, 
from highest precedence (most binding) to lowest (least binding). Operators 
in the same box have the same precedence and group left to right (except for 
exponentiation, which groups right to left).

Note that comparisons, membership tests, and identity tests, all have the 
same precedence and have a left-to-right chaining feature. Also note that this table is
incomplete - there are other operators in Python! If you want to learn more, visit 
<a href="https://docs.python.org/3/reference/expressions.html#evaluation-order">this</a> and 
<a href="https://docs.python.org/3/reference/expressions.html#comparisons">this</a> page.

| Operator                           | Description                   |
|------------------------------------|-------------------------------|
| `()`, `[]`, `{}`                   | Binding or parenthesized expression, list display, dictionary display, set display)        |
|`x[index:index]`, `x[index]`, `x(arguments...)`, `x.attribute` | Slicing, subscription, call, attribute reference |
| `**`                               | Exponentiation                | 
| `-x`, `+x`, `~x`                   | Positive, negative, bitwise not |
| `*`, `@,` `/,` `//`, `%`           | Multiplication, matrix multiplication, division, floor division, remainder|
| `+`, `-`                           | Addition and subtraction|
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, including membership tests and identity tests |
| `not x`                            | Boolean NOT |
| `and`                              | Boolean AND |
| `or`                               | Boolean OR |
| `if – else`                        | Conditional expression |
| `:=`                               | Assignment expression |


Check if `name` is `"Ellis"` or if it's not true that `name` is `"John"` and he is `17` years old at the same time.  

<div class='hint'>Combine <code>is</code>, <code>and</code>, <code>or</code>, <code>not</code> and <code>==</code> operators.</div>

<div class='hint'>Use brackets to combine operations you need to be evaluated first, just like in math equations.</div>

<style>
table, th, td {
  border: 1px solid dimgray;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
}
table td:nth-child(1) {
    text-align: center;
}
</style>