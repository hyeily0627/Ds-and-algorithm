# file : ds08_단순연결리스트이해 
# desc : 연결리스트 학습 다시

## 노드 클래스 선언 
class Node(): # 해당 클래스는 2개의 변수를 가지고 있음(data, link)
    data = None # Node의 데이터 담는 변수
    link = None # Node가 가리키는 다음 노드의 주소를 담는 변수 

    def __init__(self) -> None : 
        self.data = None # 클래스 자신이 self 이므로 클래스 변수 접근을 위해서는 반드시 self! 
        self.link = None 

## start 부터 시작해서 끝까지 node.data 출력 함수
def printNode(start): # start부터 시작해서 끝까지 node.data 출력 
    curr = start # start == head
    if curr == None : return # 참고: break 나 continue도 맞는거 같지만, 이것들은 반복문에서 사용
    while True : 
        if curr.link == None : # 연결할 노드가 더이상 없으며
            print(curr.data) # 자기 데이터만 출력하고 
            break # 반복문 탈출
        else : 
            print(curr.data, end=' -> ') # 연결할 노드가 있으니까 연결표시를 하고 
            curr = curr.link # 자기 뒤의 데이터를 curr 로 바꿔준다. 
    print()

## 노드 삽입 함수 
def insertNode(find, data): 
    global head, prev, curr # 전역변수를 insertNode() 에서 사용하겠다고 선언

    if head.data == find: # 맨 첫번쨰 노드
        node = Node()
        node.data = data
        node.link = head  
        head = node
        return # 함수 탈출 
    
    curr = head
    while curr.link != None : # 중간에 노드 삽입
        prev = curr 
        curr = curr.link
        if curr.data == find : # 데이터를 찾았으면
            node = Node()
            node.data = data
            node.link = curr # 찾은 노드 앞에 새노드 연결 
            prev.link = node # 이전 노드 뒤에 새노드 연결
            return #  함수 탈출 
        
    node = Node() # 맨 마지막에 노드 삽입
    node.data = data
    curr.link = node
    return

## 노드 삭제 함수
def deleteNode(data):
    global head, prev, curr

    if head.data == data:
        curr = head 
        head = head.link
        del(curr)
        return

    curr = head
    while curr.link != None : 
        prev = curr
        curr = curr.link
        if curr.data == data:
            prev.link = curr.link
            del(curr)
            return

## 노드 검색 함수 
def findNode(find):
    global head, curr
    
    curr = head
    if curr.data == find : 
        return curr # 현재 노드를 리턴해주고 함수 탈출
    while curr.link != None :
        curr = curr.link # 다음 노드로
        if curr.data == find: 
            return curr 
    return Node() # 위를 만족못하면 빈 노드 리턴 함수 탈출 

## 전역변수
head, curr, pre = None, None, None
originData = ['다현','정연','쯔위','사나','지효']

## 메인코드 영역
if __name__ == '__main__':
    node = Node()
    node.data = originData[0] # = '다현'
    head = node # head는 node를 가리킴

    for name in originData[1:]: # 1번 인덱스부터 리스트 끝까지 반복
        prev = node
        node = Node()
        node.data = name
        prev.link = node

## 연결리스트 구성 완료
print('최초 구성된 연결리스트')
printNode(head) # 구성된 연결리스트가 맞는지 출력 확인

insertNode('다현', '정국')
print('노드 추가')
printNode(head)

insertNode('사나', '미미')
print('중간 노드 삽입')
printNode(head)

insertNode('재남', 'RM') # 재남이란 노드가 없으니 마지막 삽입 
print('마지막 노드 삽입')
printNode(head)

# 노드검색
fNode = findNode('다현')
printNode(head)
print(f'찾은 노드 : {fNode.data}')

fNode = findNode('쯔위')
printNode(head)
print(f'찾은 노드 : {fNode.data}')


zzzzzzzzzzz


