import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Erstelle eine Figur und eine Achse mit festgelegter Fenstergröße
fig, ax = plt.subplots(figsize=(1.0, 1.0))  # Fenstergröße: 120x120 Pixel

# Füge den kompletten Kreis hinzu (grüne Hälfte)
circle_green = patches.Wedge((0.5, 0.5), 0.4, 0, 180, edgecolor='black', facecolor='green', linewidth=2)
ax.add_patch(circle_green)

# Füge die weiße Hälfte hinzu
circle_white = patches.Wedge((0.5, 0.5), 0.4, 180, 360, edgecolor='black', facecolor='white', linewidth=2)
ax.add_patch(circle_white)

# Setze die Achsenbegrenzung und gleiche Skalierung
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Entferne Gitterlinien, Achsen und Ticks
ax.axis('off')

# Zeige die Figur
plt.show()
