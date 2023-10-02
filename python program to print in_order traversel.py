class TN:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def iot(root):
    answer=[]
    iotUtil(root,answer)
    return answer
def iotUtil(root,answer):
    if root is None:
        return
    iotUtil(root.left,answer)
    iotUtil(root.right,answer)
    answer.append(root.val)
    return
root=TN(1)
root.left=TN(2)
root.right=TN(3)
root.left.left=TN(4)
root.left.right=TN(5)
print(iot(root))