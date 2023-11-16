class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int leftPointer = 0;
        int rightPointer = numbers.length - 1;
        int[] output = new int[2];

        while (leftPointer < rightPointer) {

            int valueOne = numbers[leftPointer];
            int valueTwo = numbers[rightPointer];

            if (valueOne + valueTwo == target) {
                output[0] = leftPointer + 1;
                output[1] = rightPointer + 1;
                return output;
            } else if (valueOne + valueTwo > target) {
                rightPointer -= 1;
            } else {
                leftPointer += 1;
            }

        }
        
        return output; 
    }
}