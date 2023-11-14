class Solution {
    public boolean isValid(String s) {


        if (s.length() == 0) {
            return false;
        }

        Stack<Character> stack = new Stack<>();

        HashSet<Character> hashSet = new HashSet<>();
        hashSet.add('[');
        hashSet.add('(');
        hashSet.add('{');

        for (int i = 0; i < s.length(); i++) {
            Character character = s.charAt(i);

            if (hashSet.contains(character)) {
                stack.add(character);
            }

            else {

                if (stack.isEmpty()) {
                    return false;
                }

                Character lastElement = stack.lastElement();
                if ((lastElement.equals('[') && character.equals(']')) || (lastElement.equals('(') && character.equals(')')) || (lastElement.equals('{') && character.equals('}'))) {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }

        return stack.isEmpty();




 
    }
}