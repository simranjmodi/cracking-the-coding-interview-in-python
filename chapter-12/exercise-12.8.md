### 12.8 Copy Node

#### Write a method that takes a pointer to a Node structure as a parameter and returns a complete copy of the passed in data structure. The Node data structure contains two pointers to other Nodes. 

**Solution**

The algorithm will maintain a mapping from the node address in the original structure to the corresponding node in the new structure. 
This mapping will allow us to discover previously copied nodes during a traditional depth-first traversal of the algorithm.
Traversals often mark visited nodes - the mark can take many forms, and does not necessarily need to be stored in the node.

Thus, we have a simple recursive algorithm.

<pre>
typedef map<Node*, Node*> NodeMap;

Node * copy_recursive(Node * cur, NodeMap & nodeMap) {
    if (curr == NULL) {
        return NULL;
    }
    
    NodeMap::iterator i = nodeMap.find(cur);
    if (i != nodeMap.end()) {
    return i -> second;
    }
    
    Node * node = new Node;
    nodeMap[cur] = node;
    node -> ptr1 = copy_recursive(cur -> ptr1, nodemMap;
    node -> ptr2 = copy_recursive(cur -> ptr2, nodemMap;
    return node;
}

Node * copy_structure(Node * root) {
    NodeMap nodeMap;
    return copy_recursive(root, nodeMap);
}
</pre>
