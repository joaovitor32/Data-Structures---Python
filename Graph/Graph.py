class Node:
    def __init__(self,data):
        self.data=data
        self.edges=[]
        self.search=False
        self.parent=None

    def addEdge(self,neighbor):
        self.edges.append(neighbor)
        neighbor.edges.append(self)

class Graph:
    def __init__(self):
        self.nodes=[]
        self.end=None
        self.start=None

    def addNode(self,node):
        self.nodes.append(node)

    def getNode(self,data):
        return self.nodes[data]

    def setStart(self,index):
        self.start=self.nodes[index]
        return self.start
    
    def setEnd(self,index):
        self.end=self.nodes[index]
        return self.end

    def checkPathBfs(self):
        path=[]
        path.append(self.end)
        next=self.end.parent

        while next is not None:
            path.append(next)
            next=next.parent
        
        txt=''
        for i in range(len(path)-1,0,-1):
            n=path[i]
            txt+=str(n.data)+"---->"
        print(txt)

    def BFS(self):
        queue=[]
        self.start=self.setStart(0)
        self.end=self.setEnd(len(self.nodes)-1)

        self.start.search=True

        queue.append(self.start)
        while len(queue)>0:
            current=queue.pop(0)
            if current == self.end:
                print("Found")
                break
            else:
                edges=current.edges
                for i in range(0,len(edges),1):
                    neighbor=edges[i]
                    if not neighbor.search:
                        neighbor.search=True
                        neighbor.parent=current
                        queue.append(neighbor)

        self.checkPathBfs()

    def DFS(self):
        
        stack=[]
        self.start=self.setStart(0)
        self.end=self.setEnd(len(self.nodes)-1)

        stack.append(self.start)

        while len(stack)>0:
            current=stack.pop(len(stack)-1)
            if not current.search
                current.search=True
                edges=current.edges
                for i in range(0,len(edges),1):
                    neighbor=edges[i]
                    stack.append(neighbor)
            else:
                print(stack)
                print(current)
                break
    

