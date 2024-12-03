

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        result = []
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        
        # Join with commas for clarity
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        # Split the string into a list
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1
        
        while q:
            node = q.popleft()
            if index < len(nodes) and nodes[index] != "null":
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1
            if index < len(nodes) and nodes[index] != "null":
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        
        return root


