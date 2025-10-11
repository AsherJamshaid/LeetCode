int addDigits(int num) {
    
    int n1 =0,n2 =0,sum =0;

    while(1){
        n1 = num % 10;
        n2 = num / 10;

        sum = n2 + n1;
        if((sum / 10) == 0){
            return sum;
            break;
        }
        else{
            num = sum;
            continue;
        }
    }
}
