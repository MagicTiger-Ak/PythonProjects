def km_per_hr_to_m_per_sec(speed_kmph):
    return (speed_kmph * 5) / 18

def m_per_sec_to_km_per_hr(speed_mps):
    return (speed_mps * 18) / 5
def time_from_speed_and_distance(speed, distance):
    return distance/speed

def distance_from_speed_and_time(speed, time):
    return speed*time
def time_ratio_from_speed_ratio(speed_ratio_a, speed_ratio_b):
    return 1 / speed_ratio_a, 1 / speed_ratio_b

def average_speed_for_equal_distance(speed1, speed2):
    return (2 * speed1*speed2) / (speed1 + speed2)

speed_kmph = float(input("Enter speed in km/hr: "))
speed_mps = km_per_hr_to_m_per_sec(speed_kmph)

print("\nConverted Speed: ")
print(f"{speed_kmph} km/hr is equal to  {speed_mps:.2f} m/s\n")

distance = float(input("Enter distance in km: "))
time = time_from_speed_and_distance(speed_kmph, distance)

print("\n Calculated Time :")
print(f"Time taken to cover {distance} km at {speed_kmph} km/hr is {time:.2f} hours\n")

time_ratio_a = float(input("Enter the speed ratio (a) for object A : "))
time_ratio_b = float(input("Enter the speed ratio (b) for objects B : "))

time_ratio_a, time_ratio_b = time_ratio_from_speed_ratio(time_ratio_a, time_ratio_b)

print("\n Time Ratio : ")
print(f"The ratio of times taken by A and B is {time_ratio_a} : {time_ratio_b}\n")

speed1 = float(input("Enter speed for the first part ofthe journey in km/hr: "))
speed2 = float(input("Enter speed for the seciond part of the journy in km/hr: "))

average_speed = average_speed_for_equal_distance(speed1, speed2)

print("\n Average Speed")
print(f"The average speed for the whole journey is {average_speed:.2f} km/hr")