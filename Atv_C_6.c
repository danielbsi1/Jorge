/*6) Faça um programa que leia um valor representando um número de segundos. Em seguida
converta-o para horas, minutos e segundos na forma:
7322 segundos são 2 horas, 2 minutos e 2 segundos.*/

#include <stdio.h>
#include <math.h>

int main(){
    int seg;
    printf("Digite a quantidade de sgundos: ");
    scanf("%d", &seg);
    printf("%d segundos sao %d horas, %d minutos e %d segundos", seg, seg/3600, (seg%3600)/60, seg%60);
}