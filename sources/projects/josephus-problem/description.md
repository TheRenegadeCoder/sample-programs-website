There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.

### Example

__Input:__

n = 5 (total number of people in circle)

k = 2 (number of people - 1 are skipped and kth person is killed)

__Output__: (Number of people in the circle currently, number of people to skip, index of the person to be killed or removed)

[1, 2, 3, 4, 5] 1 0

[1, 3, 4, 5] 1 1

[1, 3, 5] 1 2

[3, 5] 1 0

3

At the end, 3rd person stays alive.
