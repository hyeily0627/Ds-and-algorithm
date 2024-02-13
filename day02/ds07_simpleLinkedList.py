# file : ds07_simpleLinkedList.py
# desc : 단순 연결리스트 일반 구현

memory = [] # 컴퓨터 메모리를 유사구성
head, curr, pre = None, None, None
# head, curr, pre는 일반 변수

class Node():
    # data, link 2개의 멤버 변수 존재(함수 X)
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

def printNodes (start):
    curr = start
    if curr == None: return # 함수를 빠져나감
    print(curr.data, end=' -> ')
    while curr.link != None : 
        curr = curr.link # 내 노드 다음의 노드가 current가 됨 
        print(curr.data, end=' -> ') #end -> 로 해서 enter이 없음
    print () #enter 추가                                                                

dataArray = ['다현','정연','쯔위','사나','지효']

# 메인  
if __name__ == '__main__' :
    node = Node(dataArray[0])
    head = node # 첫번째 값을 head가 가리킴 
    memory.append(node) # 가짜메모리에 집어넣음

    for data in dataArray[1:] : # 두번째 노드보다 끝
        prev = node
        node = Node(data) # 정연~
        prev.link = node
        memory.append(node)
    
    printNodes(head)