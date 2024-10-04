/*7) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o
valor correspondente em graus Celsius*/

#include <stdio.h>
#include<math.h>

int main(){
    float fal;
    printf("Digite a temperaturam em Fahrenheit: ");
    scanf("%f", &fal);
    printf("Essa temperatura convertida em Celsius e: %f", (fal-32) * 5/9);
    return 0;
}