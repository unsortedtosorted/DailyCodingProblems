"""
Serialize Deserialize a binary Tree

Runtime : O (N)
Space : O(N)

"""



from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.l = ""
        
        def preOrder(root):
            
            if root:
                self.l=self.l+","+str(root.val)
                preOrder(root.left)
                preOrder(root.right)
            
            else:
                self.l=self.l+",$"
        
        preOrder(root)
        return str(self.l)
                
                 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        self.l =data.split(",")
        self.l = deque(self.l[1:])
        
        def preOrder():
            
            if len(self.l)>=0:
                
                if self.l[0] == '$':
                    self.l.popleft()
                    return None
                
                root = TreeNode(self.l[0])
                self.l.popleft()
                root.left =  preOrder()
                root.right =  preOrder()
                
                return root

        root = preOrder()
        return root
