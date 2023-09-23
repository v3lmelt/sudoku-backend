class CrossCycleLinkNode(object):
    def __init__(self, x, row):
        self.val = x
        self.row = row
        self.col = self
        self.up = self
        self.down = self
        self.left = self
        self.right = self

    # 删除一整列的操作

    def removeColumn(self):
        node = self
        while True:
            node.left.right = node.right
            node.right.left = node.left
            node = node.down

            if node == self:
                break

    # 恢复一整列的操作

    def restoreColumn(self):
        node = self
        while True:
            node.left.right = node
            node.right.left = node
            node = node.down

            if node == self:
                break

    # 删除一整行的操作

    def removeRow(self):
        node = self
        while True:
            node.up.down = node.down
            node.down.up = node.up
            node = node.right

            if node == self:
                break

    # 恢复一整行的操作

    def restoreRow(self):
        node = self
        while True:
            node.up.down = node
            node.down.up = node
            node = node.right

            if node == self:
                break


def dance_link_warpper(head: CrossCycleLinkNode):
    ans = []
    dance_link(head, ans)

    return ans


def dance_link(head: CrossCycleLinkNode, answer: list):
    if head.right == head:
        return True

    node = head.right
    while True:
        if node.down == node:
            return False
        node = node.right
        if node == head:
            break

    # 从head的右边第一个节点入手，将一列的节点都删除，并将恢复操作压入栈中

    restores = []
    first_col = head.right
    first_col.removeColumn()
    restores.append(first_col.restoreColumn)

    # 遍历first_col上的所有节点，将节点所在的行都删除，并将恢复操作压入栈中 (注意列节点除外)

    node = first_col.down
    while node != first_col:
        if node.right != node:
            node.right.removeRow()
            restores.append(node.right.restoreRow)
        node = node.down

    # 如果答案存在，那么就在移除的这两行之中

    cur_restores_count = len(restores)
    selected_row = first_col.down

    while selected_row != first_col:
        answer.append(selected_row.row)
        if selected_row.right != selected_row:
            row_node = selected_row.right
            while True:
                col_node = row_node.col
                col_node.removeColumn()
                restores.append(col_node.restoreColumn)

                col_node = col_node.down
                while col_node != col_node.col:
                    if col_node.right != col_node:
                        col_node.right.removeRow()
                        restores.append(col_node.right.restoreRow)
                    col_node = col_node.down

                row_node = row_node.right
                if row_node == selected_row.right:
                    break
        # 递归
        if dance_link(head, answer):
            while len(restores):
                restores.pop()()
            return True

        answer.pop()
        while len(restores) > cur_restores_count:
            restores.pop()()
        selected_row = selected_row.down
    while len(restores):
        restores.pop()()
    return False


# 初始化列操作
def initCol(col_count: int):
    head = CrossCycleLinkNode('head', 'column')
    for i in range(col_count):
        col_node = CrossCycleLinkNode(x=i, row=head.row)
        col_node.right = head
        col_node.left = head.left
        col_node.right.left = col_node
        col_node.left.right = col_node
    return head


def appendRow(head: CrossCycleLinkNode, row_id: int, nums: list):
    last = None
    col = head.right
    for num in nums:
        while col != head:
            if col.val == num:
                node = CrossCycleLinkNode(1, row_id)
                node.col = col
                node.down = col
                node.up = col.up
                node.down.up = node
                node.up.down = node
                if last is not None:
                    node.left = last
                    node.right = last.right
                    node.left.right = node
                    node.right.left = node
                last = node
                break
            col = col.right
        else:
            return
