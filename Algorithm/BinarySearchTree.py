#클래스 생성 및 초기화
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    #탐색 메서드
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        # 만일 root값이 존재하거나 root의 값이 key와 같다면 root 반환
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            # 만일 키값이 root.data보다 작으면 왼쪽 서브트리로 이동하고
            return self._find_value(root.left, key)
        else:
            # 만일 키값이 root.data보다 크면 오른쪽 서브트리로 이동
            return self._find_value(root.right, key)

    #삽입 메서드
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        # 만약 노드가 비어 있으면 data를 노드에 넣어준다.
        if node is None:
            node = Node(data)
        else:
            # 노드데이터보다 데이터가 작으면 왼쪽 서브트리로 이동한다.
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                # 노드데이터보다 데이터가 크면 오른쪽 서브트리로 간다.
                node.right = self._insert_value(node.right, data)
        return node

    #삭제 메서드
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        #deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right: # 삭제할 노드의 자식 노드가 두 개인 경우
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right: #삭제할 노드의 자식 노드가 하나인 경우
                node = node.left or node.right
            else: #삭제할 노드가 단말 노드인 경우
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(40)) # True
print(bst.find(4)) # True
print(bst.find(34)) # True
print(bst.find(45)) # True
print(bst.find(14)) # True
print(bst.find(55)) # True
print(bst.find(48)) # True
print(bst.find(13)) # True
print(bst.find(15)) # True
print(bst.find(49)) # True
print(bst.find(100)) # False

# Delete
#print(bst.delete(55)) # True
print(bst.delete(14)) # True
#print(bst.delete(11)) # False