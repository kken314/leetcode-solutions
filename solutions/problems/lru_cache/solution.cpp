class Node {
public:
    Node* next;
    Node* prev;
    int key;
    int val;

    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
};

class LRUCache {
private:
    int cap; // capacity
    unordered_map<int, Node*> map; // key -> Node
    Node* left;
    Node* right;

    void remove(Node* node){
        Node* prev_node = node->prev;
        Node* next_node = node->next;
        prev_node->next = next_node;
        next_node->prev = prev_node;
    }

    void insert_back(Node* node) {
        Node* top = right->prev;
        node->next = right;
        node->prev = top;
        top->next = node;
        right->prev = node;

    }
public:

    LRUCache(int capacity) {
        this->cap = capacity;
        this->left = new Node(0, 0);
        this->right = new Node(0, 0);
        left->next = right;
        right->prev = left; 
    }
    
    int get(int key) {
        if (map.contains(key)) {
            remove(map[key]);
            insert_back(map[key]);
            return map[key]->val;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if (map.contains(key)) {
            remove(map[key]);
            insert_back(map[key]);
            map[key]->val = value;
        } else {

            if (map.size() >= cap) {
                map.erase(left->next->key);
                remove(left->next);
            }

            map[key] = new Node(key, value);
            insert_back(map[key]);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */