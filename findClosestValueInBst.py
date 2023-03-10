#Finds the Closest Time in a BST
#Best Case: O(log(n)) time | O(log(n)) space
#Average Case: O(log(n)) time | O(log(n)) space
#Worst Case: O(n) time | O(n) space
# Path: findClosestValueInBst.py
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)
def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	elif target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	else:
		return closest

