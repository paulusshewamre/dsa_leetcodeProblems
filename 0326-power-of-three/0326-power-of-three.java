class Solution {
    public boolean isPowerOfThree(int n) {
        return pow(n);
    }
    static boolean pow(int n){
        if(n==1){
            return true;
        }
        else if(n%3 == 0 && n!=0){
            n=n/3;
            return pow(n);
        }
        return false;
    }
}