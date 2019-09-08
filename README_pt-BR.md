# O Jogo do Caos

Read this in [english](https://github.com/filhaDeHades/Chaos-Game/blob/master/README.md)

O jogo do caos é um jogo que permite que você faça diferentes formas fractais usando números aleatórios e algumas regras. Meu objetivo pe fazer algumas das diferentes versões desse jogo.

## Bibliotecas e Referências:

Foi usada a biblioteca **pygame** para os gráficos e a biblioteca **random** para os números.
As cores disponíveis no código são baseadas na paleta de 16 cores do [pyxel](https://github.com/kitao/pyxel).

Para saber mais sobre The Chaos Game eu recomendo esses 2 vídeos:
* [Chaos Game - Numberphile](https://www.youtube.com/watch?v=kbKtFN71Lfs)
* [Coding Challenge #123.1:Chaos Game Part 1](https://www.youtube.com/watch?v=7gNzMtYo9n4)

### **1. Triângulo de Sierpinski**:
Depois de definidos 3 pontos como vértices de um triângulo, um outro ponto é escolhido aleatoriamente.
1. É escolhido um dos 3 vértices do triângulo aleatoriamente.
2. Calcula-se a metade da distância do vértice escolhido ao ponto e seu resultado será a posição do novo ponto.
3. Repete o passo 1.

#### Funções:
* **drawPoint(cor, x, y)** - Recebe a cor do ponto e sua posição no plano XY e desenha o ponto na tela.
* **loop(current, points)** - Pega a posição atual do ponto e o vetor com os 3 pontos iniciais para escolher aleatoriamente uma direção para a movimentação do ponto e definir o próximo ponto a desenhar.
* **chaos()** - Define os 3 pontos iniciais do triangulo, também define a primeira posição do ponto a desenhar.