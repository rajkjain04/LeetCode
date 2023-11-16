class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        HashSet<List<Integer>> unique = new HashSet<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            int valueOne = nums[i];

            int leftPointer = i + 1;
            int rightPointer = nums.length - 1;

            while (leftPointer < rightPointer) {
                int valueTwo = nums[leftPointer];
                int valueThree = nums[rightPointer];

                if (valueOne + valueTwo + valueThree == 0) {
                    List<Integer> target = new ArrayList<>();
                    target.add(valueOne);
                    target.add(valueTwo);
                    target.add(valueThree);

                    if (!unique.contains(target)) {
                        output.add(target);
                        unique.add(target);
                    }
                    
                    leftPointer += 1; 
                    rightPointer -= 1; 
                    
                } else if (valueOne + valueTwo + valueThree > 0) {
                    rightPointer -= 1;
                } else {
                    leftPointer += 1;
                }
            }
        }
        return output;
    }
}