class Node(): #기본적인 노드 클래스 구현
    def __init__(self, data): #인스턴스를 만드는 동시에 초깃값 부여
        self.data = data
        self.Left = None
        self.Right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

#탐색 메서드
    def search(self, key):
        return self.search_key(self.root, key) #search_key의 인스턴스 root,key를 반환

    def search_key(self, root, key):
        if root is None: #만약 루트가 비어있다면
            return print("탐색한 숫자가 존재하지 않습니다.",end='')
        elif root.data == key: #루트의 데이터가 넣으려는 key와 같다면
            return root,print("탐색한 숫자%d"%key,end='')
        elif key < root.data : #루트의 데이터보다 key값이 작다면 return 시켜줘서 함수를 다시 사용함으로써 왼쪽서브트리로 이동한 뒤, 다시 키값을 찾는다
            return self.search_key(root.Left, key)
        else: #루트의 데이터보다 key값이 크면 return 시켜줘서 함수를 다시 사용함으로써 오른쪽으로 이동한 뒤, 다시 키값을 찾는다
            return self.search_key(root.Right, key)

#삽입 메서드
    def insert(self, data):
        self.root = self.insert_value(self.root, data)
        return self.root is not None,print("삽입된 노드는 %d"%data)

    def insert_value(self, node, data):
        if node is None: # 노드가 비어있을경우
            node = Node(data) #노드의 데이터가 노드로 삽입된다
        elif node.data == data:
            print("탐색 되었으므로 삽입 실패")
        else:
            if data <= node.data: # 노드데이터보다 데이터가 작으면 왼쪽 서브트리로 이동한다.
                node.Left = self.insert_value(node.Left, data)
            else: # 노드데이터보다 데이터가 크면 오른쪽 서브트리로 이동한다.
                node.Right = self.insert_value(node.Right, data)
        return node

#삭제 메서드
    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    def delete_value(self, node, key):
        if node is None: #만일 노드의 값이 존재하지 않는다면
            return node, print("삭제할 노드%d가 존재하지 않습니다."%key, end='')

        if key == node.data: #노드의 데이터와 삭제하려는 key값이 일치하면
            delete = print("선택한 노드%d가 지워졌습니다"%key,node, end='')
            if node.Left or node.Right: #삭제할 노드의 자식 노드가 하나인 경우
                node = node.Left or node.Right  #삭제한 노드의 왼쪽이나 오른쪽의 자식 노드
            elif node.Left and node.Right: #삭제할 노드의 자식 노드가 두 개인 경우
                parent, child = node, node.Right #노드는 부모가 되고 오른쪽에 있는 자식은 자식이 된다.
                if child.Left is not None: #만약 왼쪽서브트리의 노드가 존재한다면
                    parent, child = child, child.Left
                child.Left = node.Left
            else: #삭제할 노드가 단말 노드인 경우
                node = None
        elif key < node.data:
            node.Left, delete = self.delete_value(node.Left, key)
        else:
            node.Right, delete = self.delete_value(node.Right, key)
        return node, delete




array = [20, 5, 3, 10, 7, 6, 12, 15, 13, 17, 23, 25, 29, 29]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)
print("------------------------------------------------------------------------")

print(bst.search(20))
print(bst.search(3))
print(bst.search(6))
print(bst.search(13))
print(bst.search(10))
print(bst.search(12))
print(bst.search(29))
print(bst.search(29))
print(bst.search(30))
print("------------------------------------------------------------------------")

print(bst.delete(10))
print(bst.delete(111))





