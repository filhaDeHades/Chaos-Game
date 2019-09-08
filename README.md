# The Chaos Game

Leia esse arquivo em [português](https://github.com/filhaDeHades/Chaos-Game/blob/master/README_pt-BR.md)

The chaos game it's a game that allows you to make diferents fractals forms using random numbers and a few rules. My purpose is to make some of the diferents version of the game.

## Librarys and References:

It was used the **pygame** library for the graphics and the **random** library for the numbers.
The set of color available on code is based in the 16-colors palette of [pyxel](https://github.com/kitao/pyxel).

For know more about the chaos game I recommend this two videos:
* [Chaos Game - Numberphile](https://www.youtube.com/watch?v=kbKtFN71Lfs)
* [Coding Challenge #123.1:Chaos Game Part 1](https://www.youtube.com/watch?v=7gNzMtYo9n4)

### **1. Sierpinsky's Triangle**:
After defined the three vertices of the triangle is defined randomly another point.
1. It's chosen one of the three vertices randomly.
2. It's calculated the half distance of the vertice and the point and the result will be next point.
3. Repeat the first step.

#### Functions:
* **drawPoint(cor, x, y)** - Take the color of the point and your position in a XY plane to draw it in the screen.
* **loop(current, points)** - Take the actual position of the point and the vector with the 3 initial point to randomly choose a direction and define the next point to be draw.
* **chaos()** - Define the 3 initial points of the triangle, also define the first position of the point to be draw.