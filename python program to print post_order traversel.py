class TN:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def poot(root):
    answer=[]
    pootUtil(root,answer)
    return answer
def pootUtil(root,answer):
    if root is None:
        return
    pootUtil(root.left,answer)
    pootUtil(root.right,answer)
    answer.append(root.val)
    return
root=TN(1)
root.left=TN(2)
root.right=TN(3)
root.left.left=TN(4)
root.left.right=TN(5)
print(poot(root))