#include<stdio.h>
int main(){
    int locks,stocks, barrels, tlocks, tstocks, tbarrels;
    float lprice, sprice, bprice, lsales, ssales, bsales, sales, comm;
    lprice = 45;
    sprice = 30;
    bprice = 25;
    tlocks=0;
    tstocks=0;
    tbarrels=0;
    printf("\n Enter number of locks = ");
    scanf("%d",&locks);
    while(locks!=-1){
        printf("\n Enter number of stocks & barrels");
        scanf("%d %d",&stocks, &barrels);
        tlocks=tlocks+locks;
        tstocks=tstocks+stocks;
        tbarrels=tbarrels+barrels;
        printf("\n Enter the number of locks ");         scanf("%d", &locks);
    }
    printf("\n Total number of locks = %d", tlocks);
    printf("\n Total number of stocks = %d", tstocks);
    printf("\n Total number of barrels = %d", tbarrels);
    lsales=locks*lprice;
    ssales=stocks*sprice;
    bsales=barrels*bprice;
    sales=lsales+ssales+bsales;
    printf("\n Total sales = %f", sales);
    if(sales > 1800){
        comm = 0.10*1000;
        comm = comm + 0.15*800;
        comm = comm + 0.15*(sales-1800);
    }
    else if(sales>1000){
        comm = 0.10*1000;
        comm = comm + 0.15*(sales-1000);
    }
    else
        comm = 0.10*sales;
    printf("The commission is = %f ", comm);
    return 0;
}
