# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
destination_distances={
    "pulchwok":1,
    "thapathali":3,
    "dhangadhi": 600,
    "pokhara": 200
}
destination_name=input("Enter your destination..").strip().lower()
if destination_name in destination_distances:
    distance = destination_distances[destination_name]
    print(f"Your distance to {destination_name} is {distance}KM")
    if distance < 3:
        print("You can reach your destination by walking")
    elif distance <= 15:
        print("You can reach your destination by Bike")
    else:
        print("Car is recommeded for you to reach the destination")
