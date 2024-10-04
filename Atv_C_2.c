/*2) Faça um algoritmo que receba quatro números inteiros, calcule e mostre a soma desses
números.*/
// não uso acento nos print pq o vs code ta dando pau no terminal //

#include <stdio.h>
#include <math.h>

int main()
{
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int num4 = 0;
    printf("Digite o primeiro numero: ");
    scanf("%d", &num1);
    printf("Digite o segundo numero: ");
    scanf("%d", &num2);
    printf("Digite o terceiro numero: ");
    scanf("%d", &num3);
    printf("Digite o quarto numero: ");
    scanf("%d", &num4);
    printf("O resultado da soma dos quatro numero digitados e: %d", num1 + num2 + num3 + num4);
    return 0;
}