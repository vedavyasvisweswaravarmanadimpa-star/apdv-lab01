# Method 1: pop() removes the last item
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus", "Pluto"]
planets.pop()
print("Method 1:", planets)

# Method 2: pop(-1) removes the item at the last position (-1 means "last")
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus", "Pluto"]
planets.pop(-1)
print("Method 2:", planets)

# Method 3: remove("Pluto") removes the item by its name
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus", "Pluto"]
planets.remove("Pluto")
print("Method 3:", planets)