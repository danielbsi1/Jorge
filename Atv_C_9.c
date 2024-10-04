/*9) Leia uma quantidade de chuva dada em polegadas e imprima o equivalente em milímetros*/

#include <stdio.h>
#include<math.h>

int main(){
    float pol;
    printf("Digite a quantidade de chuva em polegada: ");
    scanf("%f", &pol);
    printf("Essa quantia de chuva em milimetro e: %f", pol *27.4);
    return 0;
}