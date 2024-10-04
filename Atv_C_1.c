/*1) Escrever um algoritmo que pergunta um valor em metros e imprime o correspondente em decímetros,
 centímetros e milímetros.*/

#include <stdio.h>
#include <math.h>

int main()
{
    int numero = 0;
    printf("Digite o valor em metros que sera convertido: ");
    scanf("%d", &numero);
    printf("O valor %d convertido em decimetros e: %d", numero, numero * 10);
    printf("O valor %d convertido em decimetros e: %d", numero, numero * 100);
    printf("O valor %d convertido em decimetros e: %d", numero, numero * 1000);
    return 0;
}