mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)
print("first destination:", mission_route[0])
print("last destination:", mission_route[-1])
print("total destinations:", len(mission_route))
print("\nmission path:")
for destination in mission_route:
    print(destination)
if "Luna Station" in mission_route:
    print("\nthe luna station is included in the mission route.")
else:
    print("\nthe luna station is not included in the mission route.")