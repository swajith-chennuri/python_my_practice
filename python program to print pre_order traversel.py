class TN:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def pot(root):
    answer=[]
    potUtil(root,answer)
    return answer
def potUtil(root,answer):
    if root is None:
        return
    answer.append(root.val)
    potUtil(root.left,answer)
    potUtil(root.right,answer)
    return
root=TN(1)
root.left=TN(2)
root.right=TN(3)
root.left.left=TN(4)
root.left.right=TN(5)
print(pot(root))