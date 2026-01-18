[Edouard Zeckendorf][3] was a Belgian amateur mathematician who proposed a
[Theorem][1] that states that every non-negative integer (_N_) can be
represented as a sum of distinct non-consecutive [Fibonacci Numbers][2]. In
other words,

* _N_ = _F_<sub>_c_<sub>1</sub></sub> + _F_<sub>_c_<sub>2</sub></sub> + ... + _F_<sub>_c_<sub>_n_</sub></sub>

where:

* _F_<sub>_i_</sub> is the _i_<span>th</span> Fibonacci number
* _c_<sub>_i_</sub> &ge; 2
* _c_<sub>_i_</sub> &lt; _c_<sub>_i_</sub> + 1

Each Fibonacci number (_F_<sub>_i_</sub>) is the sum of the previous two Fibonacci
numbers:

* _F_<sub>0</sub> = 0
* _F_<sub>1</sub> = 1
* _F_<sub>2</sub> = _F_<sub>1</sub> + _F_<sub>0</sub> = 0 + 1 = 1
* _F_<sub>3</sub> = _F_<sub>2</sub> + _F_<sub>1</sub> = 1 + 1 = 2
* ...
* _F_<sub>_i_</sub> = _F_<sub>_i_ - 1</sub> + _F_<sub>_i_ - 2</sub>

This relationship is the reason why non-consecutive Fibonacci numbers are used.

To find the Fibonacci numbers that add up to _N_:

* Find all the Fibonacci numbers up to and including _N_, starting at
  _F_<sub>2</sub>.
* Going from largest to smallest, select each Fibonacci number such that the
  sum of all the selected values is less than or equal to _N_.

For example, for _N_ = 67, these are the Fibonacci numbers up to 67:

* 1, 2, 3, 5, 8, 13, 21, 34, 55

Therefore:

| :Trial Sum: | :Fibonacci Number: | Selected |
| 0           | 55                 | Yes      |
| 55          | 34                 | No       |
| 55          | 21                 | No       |
| 55          | 13                 | No       |
| 55          | 8                  | Yes      |
| 63          | 5                  | No       |
| 63          | 3                  | Ye       |
| 66          | 2                  | No       |
| 66          | 1                  | Yes      |

Therefore, using the selected numbers, _N_ can be represented as:

* 67 = 55 + 8 + 3 + 1

A possible optimization for this proceedure would be to skip Fibonacci
numbers that are consecutive to the last selected value and to terminate
the loop as soon as the sum is equal to _N_.

[1]: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
[2]: https://en.wikipedia.org/wiki/Fibonacci_sequence
[3]: https://en.wikipedia.org/wiki/Edouard_Zeckendorf
