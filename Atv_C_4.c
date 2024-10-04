/*4) Faça um algoritmo que receba três notas e seus respectivos pesos, calcule e mostre a
média ponderada dessas notas.*/

#include <stdio.h>
#include <math.h>

int main()
{
    float media1;
    float peso1;
    float media2;
    float peso2;
    float media3;
    float peso3;
    //
    printf("Digite a primeira nota: ");
    scanf("%f", &media1);
    printf("Digite o peso dessa nota: ");
    scanf("%f", &peso1);
    //
    printf("Digite a segunda nota: ");
    scanf("%f", &media2);
    printf("Digite o peso dessa nota: ");
    scanf("%f", &peso2);
    //
    printf("Digite a terceira nota: ");
    scanf("%f", &media3);
    printf("Digite o peso dessa nota: ");
    scanf("%f", &peso3);
    //
    printf("A media ponderada dessas tres notas e: %f", (media1 + media2 + media3)/(peso1 + peso2 + peso3));
    return 0;
}