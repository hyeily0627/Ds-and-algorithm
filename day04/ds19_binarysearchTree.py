# file : ds19_binarysearchTree.py
# desc : 이진 검색 트리 구현

# 트리 노드 클래스 선언 
class TreeNode():
    left = None
    data = None
    right = None

    def __init(self) -> None:
        self.left = self.rihgt = self.data = None

# 중위순회 함수
def inorder(node):
    if node == None : return

    inorder(node.left)
    print(node.data, end = ' -> ')
    inorder(node.right)

# 전역변수 선언 
root = None
groupList = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

# 메인 
node = TreeNode()
node.data = groupList[0]
root = node

for name in groupList[1:] : # 레드벨벳부터 끝까지~
    node = TreeNode()
    node.data = name
    
    curr = root
    while True :
        if name < curr.data: # 왼쪽 트리로
            if curr.left == None : # 왼쪽에 트리가 미구성일 경우 
                curr.left = node 
                break 
            else : 
                curr = curr.left 
        else : # 오른쪽 트리로 
            if curr.right == None: 
                curr.right = node
                break
            else : 
                curr = curr.right

print('이진트리 구성 완료❗')

findName = '걸스데이'

curr = root
level = 0
while True : 
    if findName == curr.data : 
        print(f'{curr.data} / Level {level} 을(를) 찾음')
        break 
    elif findName < curr.data : # 왼쪽 트리로
        if curr.left == None : 
            print(f'{findName}이 트리에 없음')
            break
        else : 
            curr = curr.left
            level += 1
    else : # 오른쪽 트리로
        if curr.right == None:
            print(f'{findName}이 트리에 없음')   
            break
        else : 
            curr = curr.right
            level += 1

curr = root
print('중위 순회 : ', end='')
inorder(curr)
print('끝')

# 데이터 삭제
deleteName = '마마무'
curr = root 
parent = None 

while True : 
    if deleteName == curr.data : 
        if curr.left == None and curr.right == None :
            if parent.left == curr : # 내가 부모의 왼쪽에 붙어있다면 
                parent.left = None
            else : # 내가 부모의 오른쪽에 붙어 있으면
                parent.right = None

            del(curr) # 연결이 끊어진 노드를 완전 삭제
        elif curr.left != None and curr.right == None: # 내 노드 왼쪽에 자식노드가 있다면 
            if parent.left == curr: # 부모노드 왼쪽에 내가 있으면 
                parent.left == curr.left
            else : # 부모노드의 오른쪽에 내가 있으면
                parent.right = curr.left

            del(curr) 
        elif curr.left == None and curr.right !=None : # 내노드 오른쪽에 자식노드가 있으면
            if parent.left == curr:
                parent.left == curr.right
            else : 
                parent.right = curr.right

            del(curr)
        print(f'{deleteName}이(가) 삭제됨')
        break    

    elif deleteName < curr.data :
        if curr.left == None : 
            print(f'{deleteName}이 트리에 없습니다')
            break 
        else :
            parent = curr
            curr = curr.left 
    else : # 오른쪽으로 
        if curr.right == None :
            print(f'{deleteName}이 트리에 없음')
            break
        else : 
            parent = curr
            curr = curr.right

curr = root
print('중위 순회 : ', end='')
inorder(curr)
print('끝')