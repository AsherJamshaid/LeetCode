int numberOfSteps(int num) {
    int count = 0,ans=0,ans2=0;
    while(num!=0){
        if(num%2 == 0){
            ans = num / 2;
            count++;
            if(ans % 2 == 0){
                ans2 = ans / 2;
                count++;
                num=ans2;
            }
            else{
            ans2 = ans - 1;
            count++;
            num = ans2;
            }
        }
        else{
            ans = num - 1;
            count++;
            if(ans == 0){
                break;
            }
            ans2 = ans / 2;
            count++;
            num = ans2;
        }
    }
    return count;
}
