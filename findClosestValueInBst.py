abs(target - closest) > abs(target - tree.value):
closest = tree.value
target < tree.value:
	return findClosestValue(tree.right, target, closest)
if target > tree.value:
	return findClosestValue(tree.left, target, closest)
else:
	return closest

	change
	need to create code again
