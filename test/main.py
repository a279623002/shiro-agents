input_ids = [[1,2,3]]
output_ids = [[7,8,9],[10,11]]
paired = zip(input_ids, output_ids)
print()
print(paired)
ids = [
    j[len(i):] for i, j in paired
]
print(ids)

