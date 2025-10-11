int subtractProductAndSum(int n) {
    int num1 =0 , num2=0, product = 1,sum = 0;
    while(n != 0){
        num1 = n % 10;
        num2 = n / 10;
        product = product * num1;
        sum = sum + num1;
        n = num2;
    }
    return (product - sum);
}
