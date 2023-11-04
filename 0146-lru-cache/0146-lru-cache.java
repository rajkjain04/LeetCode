import java.util.HashMap;
import java.util.Objects;

class Node {
    public int key;
    public int value;

    public Node prev;
    public Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}



class LRUCache {

    private int cap;
    private HashMap<Integer, Node> hashMap;

    private Node left;
    private Node right;
    public LRUCache(int capacity) {
        this.cap = capacity;
        this.hashMap = new HashMap<>();
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }
    // Remove a particular node from the Doubly Linked List

    public void remove(Node node) {
        Node left = node.prev;
        Node right = node.next;
        left.next = right;
        right.prev = left;
    }
    // Insert a node right at the end of the list
    public void insert(Node node) {
        Node tmp = this.right.prev;
        this.right.prev = node;
        node.next = this.right;
        node.prev = tmp;
        tmp.next = node; 
    }
    public int get(int key) {

        if (hashMap.containsKey(key)) {
            Node node = this.hashMap.get(key);
            this.remove(node);
            this.insert(node);
            return node.value;
        }
        return -1;
    }

    public void put(int key, int value) {

        if (hashMap.containsKey(key)) {
            Node node = this.hashMap.get(key);
            this.remove(node);
            this.hashMap.remove(key);
        }

        Node node = new Node(key, value);
        this.hashMap.put(key, node);
        this.insert(node);

        if (hashMap.size() > this.cap) {
            Node lru = this.left.next;
            this.remove(lru);
            this.hashMap.remove(lru.key);
        }

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */