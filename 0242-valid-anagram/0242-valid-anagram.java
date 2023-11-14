class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (hashMap.containsKey(s.charAt(i))) {
                int value = hashMap.get(s.charAt(i));
                hashMap.put(s.charAt(i), value + 1);
            } else {
                hashMap.put(s.charAt(i) , 1); 
            }
        }

        for (int j = 0; j < t.length(); j++) {
            
            if (hashMap.containsKey(t.charAt(j)) == false) {
                return false; 
            }
            
            if (hashMap.get(t.charAt(j)) == 0) {
                return false; 
            } 
            else {
                int value = hashMap.get(t.charAt(j));
                hashMap.put(t.charAt(j), value - 1);
            }
        }
        return true;
    }
}