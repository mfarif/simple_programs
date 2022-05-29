def interval_overlap(self, inv1: list[int], inv2: list[int]) -> bool:
	x1, y1 = inv1[0], inv1[1]
	x2, y2 = inv2[0], inv2[1]

	if max(x1, x2) < min(y1, y2):
	    return True
	return False    
