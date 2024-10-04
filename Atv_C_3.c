// 3) Faça um algoritmo que receba três notas, calcule e mostre a média aritmética entre elas.//

#include <stdio.h>
#include <math.h>

int main()
{
    float media1 = 0;
    float media2 = 0;
    float media3 = 0;
    printf("Digite a primeira nota: ");
    scanf("%f", &media1);
    printf("Digite a segunda nota: ");
    scanf("%f", &media2);
    printf("Digite a terceira nota: ");
    scanf("%f", &media3);
    printf("A media aritimetica dessas tres nota e: %f", (media1 + media2 + media3) / 3);
    return 0;
}