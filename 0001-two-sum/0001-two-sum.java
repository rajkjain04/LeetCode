import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[] output = new int[2];
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hashMap.containsKey(target - nums[i])) {
                int index = hashMap.get(target - nums[i]); 
                output[0] = index;
                output[1] = i; 
                return output; 
                
            } else {
                hashMap.put(nums[i], i); 
            }
            
        }


        return output; 
    }
}