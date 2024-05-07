def distribute_objects(num_objects):
    if num_objects <= 0:
        return "Number of objects must be greater than zero"
    
    # Calculate the angle for each object
    angles = []
    if num_objects == 1:
        angles.append(90)  # If there's only one object, place it at 90 degrees
    else:
        for i in range(num_objects):
            angle = 90 + (i - (num_objects - 1) / 2) * (180 / (num_objects - 1))
            angles.append(angle)
    
    return angles

# Example usage
num_objects = int(input("Enter the number of objects to distribute along the half circle: "))
result = distribute_objects(num_objects)
print("Angles for each object:", result)
