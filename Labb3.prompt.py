import matplotlib.pyplot as plt

points = []
with open("unlabelled_data.csv", "r") as file:  # Cleaning and dividing data
    for line in file:
        line = line.strip()              # Removes spaces and \n
        parts = line.split(",")          # Split at ,
        x_str = parts[0]
        y_str = parts[1]
        x = float(x_str)                 # Making into floats from str
        y = float(y_str)
        point = (x, y)
        points.append(point)

k = -1.0
m = 0.0

def classify_point(x, y, k=-1.0, m=0.0):
    line_y = k * x + m   # line function y = -x
    if y < line_y:
        return 0
    else:
        return 1

classified_points = []
for point in points:
    x = point[0]
    y = point[1]
    label = classify_point(x, y, k, m)
    new_point = (x, y, label)
    classified_points.append(new_point)

with open("labelled_data.csv", "w") as labelfile:
    for point in classified_points:
        x = point[0]
        y = point[1]
        label = point[2]
        line_text = f"{x},{y},{label}\n" 
        labelfile.write(line_text)

x0 = []
y0 = []
x1 = []
y1 = []

for point in classified_points:
    x = point[0]
    y = point[1]
    label = point[2]

    if label == 0:
        x0.append(x)
        y0.append(y)
    else:
        x1.append(x)
        y1.append(y)

print("Number of class 0:", len(x0))
print("Number of class 1:", len(x1))

plt.scatter(x0, y0, color="blue", label="Class 0 (below/left)")
plt.scatter(x1, y1, color="green", label="Class 1 (above/right)")

# Draw line y = kx + m
x_min = min(x for x, y in points)
x_max = max(x for x, y in points)
y_min = k * x_min + m
y_max = k * x_max + m


plt.plot([x_min, x_max], [y_min, y_max], color="red", label=f"y = {k}x + {m}")

plt.title("Linear Classification Lab 3")
plt.grid(True)
plt.legend()
plt.show()
