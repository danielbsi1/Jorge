/*5) Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
a) o número digitado ao quadrado;
b) o número digitado ao cubo;
c) a raiz quadrada do número digitado;
d) a raiz cúbica do número digitado.*/

#include <stdio.h>
#include <math.h>

int main()
{
    int num;
    printf("Digite o numero desejado:");
    scanf("%d", &num);
    printf("O numero %d ao quadrado e : %d \n", num, num * num);
    printf("O numero %d ao cubo e: %d \n", num, num * num * num);
    printf("A raiz quadrada do numero %d e: %lf \n", num, sqrt(num));
    printf("A raiz cubica do numero %d e: %lf \n", num, cbrt(num));
    return 0;
}