class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        HashMap<Integer, Integer> numOfSmaller = new HashMap<>();
        int[] sortedNums = Arrays.copyOf(nums,nums.length);
        Arrays.sort(sortedNums);
        int rank = 0;
        int repCount = 0;
        for(int i=0;i<sortedNums.length;i++){
            if(i > 0 && sortedNums[i] > sortedNums[i-1]){
                rank = rank + 1 +  repCount;
                repCount=0;
            }
            if(i > 0 && sortedNums[i] == sortedNums[i-1]){
                repCount++;
            }
            numOfSmaller.put(sortedNums[i], rank);
        }

        for(int i=0;i<nums.length;i++){
            nums[i] = numOfSmaller.get(nums[i]);
        }
        return nums;
    }
}