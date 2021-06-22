from general_tree import Node


sample = Node(10)
sample.left = Node(20)
sample.right = Node(30)
sample.left.left = Node(40)
sample.left.right = Node(50)
sample.left.right.left = Node(70)
sample.left.right.right = Node(80)
sample.right.right = Node(60)


sample2 = Node(69)


sample3 = None


sample4 = Node(10)
sample4.left = Node(6)
sample4.right = Node(8)
sample4.right.right = Node(7)
sample4.right.right.right = Node(12)
sample4.right.right.left = Node(11)


sample5 = Node(10)
sample5.left = Node(20)
sample5.left.left = Node(8)
sample5.left.right = Node(7)
sample5.left.right.right = Node(15)
sample5.left.right.left = Node(9)
sample5.right = Node(30)
sample5.right.right = Node(6)


sample6 = Node(66)
sample6.left = Node(69)
sample6.left.left = Node(420)
sample6.left.left.left = Node(50)
sample6.left.left.left.left = Node(49)
sample6.left.left.left.left.left = Node(63)


sample7 = Node(66)
sample7.right = Node(69)
sample7.right.right = Node(420)
sample7.right.right.right = Node(50)
sample7.right.right.right.right = Node(49)
sample7.right.right.right.right.right = Node(63)


sample8 = Node(10)
sample8.left = Node(20)
sample8.left.left = Node(40)
sample8.left.right = Node(50)
sample8.right = Node(80)
sample8.right.right = Node(60)


sample9 = Node(30)
sample9.right = Node(50)
sample9.right.left = Node(60)
sample9.right.left.right = Node(10)

sample10 = Node(10)
sample10.left = Node(50)
sample10.right = Node(60)
sample10.right.left = Node(70)
sample10.right.right = Node(20)
sample10.right.left.right = Node(8)


sample11 = Node(20)
sample11.left = Node(8)
sample11.right = Node(12)
sample11.left.left = Node(3)
sample11.left.right = Node(5)
sample11.right = Node(12)

sample12 = Node(3)
sample12.left = Node(1)
sample12.right = Node(2)
sample12.right.left = Node(1)
sample12.right.right = Node(2)
