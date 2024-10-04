/*10) O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade
de cada item que você consumiu e calcule a conta final.
Hambúrguer................. R$ 3,00
Cheeseburger.............. R$ 2,50
Fritas........................... R$ 2,50
Refrigerante................. R$ 1,00*/

#include <stdio.h>
#include<math.h>

int main(){
    float ham;
    float chees;
    float fri;
    float refr;
    printf("Quantos hamburguer voce consumiu?: ");
    scanf("%f", &ham);
    printf("Quantos cheesburguers voce consumiu?: ");
    scanf("%f", &chees);
    printf("Quantas fritas voce consumiu?: ");
    scanf("%f", &fri);
    printf("Quantos refrigerantes voce consumiu?: ");
    scanf("%f", &refr);
    printf("Voce consumiu %f R$", (ham * 3)+(chees * 2.5)+(fri * 2.5)+(refr * 1));
    return 0;
}