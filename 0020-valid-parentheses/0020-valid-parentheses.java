class Solution {
    public boolean isValid(String s) {

        HashSet<Character> set = new HashSet<>();
        set.add('(');
        set.add('[');
        set.add('{');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            if (set.contains(s.charAt(i))) {
                stack.add(s.charAt(i));
            } else {

                if (stack.isEmpty()) {
                    return false;
                }

                Character lastElement = stack.lastElement();
                char currentElement = s.charAt(i);

                if ((lastElement == '(' && currentElement == ')') || (lastElement == '[' && currentElement == ']') || (lastElement == '{' && currentElement == '}')) {
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