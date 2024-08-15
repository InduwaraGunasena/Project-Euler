import math, time

start = time.time()

"""
In this code we use a simple technique to solve the problem. Here we consider thea hypotenuse instead of considering perimeter. 
We know that we can create a right-angle triangle inside a circle by its diameter lying on exactly hypotenuse.
By considering that theorem we calculate all the possible integer sides by varying one side(a) along its circumference. 
To reduce same answers and be efficient, we can vary that side(a) to one point only. That point is the upper bound of that a.
That is, we only vary until it creates 45 degree angle. 
"""

p = 1000  # Peremeter limit

answer = {}  # Save all the perimeters inside a dictionary. The keys represent one perimeter and its value represents its count.
c = 3  # We start from a circle which has a 3 units diameter.
# ( We know there are no right-angle triangles which having all the sides are integers and hypotenuse equal to 1 or 2)
while c <= p:
    # Get the maximum value for one side.
    # That is equal when the triangle is an isosceles triangle.(i.e. other two angles equal to 45 degrees each)
    a_max = int(c // (math.sqrt(2)))

    for a in range(1, a_max+1):
        b = math.sqrt(c*c - a*a)
        # check whether b is a decimal number or an integer by checking its remainder after dividing by 1.
        # if it's an integer there is no remainder but if it's decimal it has.
        if b % 1 != 0:
            continue
        else: # if b is an integer only, consider that triangle sides further.
            perimeter = a + b + c
            if perimeter <= p: # perimeter must be less than our limit.
                #answer.append(int(perimeter))
                answer[perimeter] = answer.get(perimeter, 0) + 1
    c += 1 # increase our circle diameter by one

print("answer =", max(answer, key = answer.get), "\n")

end = time.time()
print(end - start)