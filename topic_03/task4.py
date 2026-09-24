def find_insert_position(sorted_list, val):
    for i in range(len(sorted_list)):
        if val <= sorted_list[i]:
            return i
    return len(sorted_list)

nums = [10, 20, 30, 40, 50]
val = 25
pos = find_insert_position(nums, val)

print("List:", nums)
print("Position to insert:", pos)
nums.insert(pos, val)
print("Updated list:", nums)
