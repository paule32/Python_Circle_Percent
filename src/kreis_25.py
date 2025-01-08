import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Erstelle eine Figur und eine Achse mit festgelegter Fenstergröße
fig, ax = plt.subplots(figsize=(1.2, 1.2))  # Fenstergröße: 120x120 Pixel

# Zeichne den vollen grünen Kreis
full_circle = patches.Circle(
    (0.5, 0.5),  # Mittelpunkt
    0.4,         # Radius
    edgecolor='black', facecolor='green', linewidth=2
)
ax.add_patch(full_circle)

# Füge die 3/4-Teilfläche (weiß) hinzu
three_quarter_wedge = patches.Wedge(
    (0.5, 0.5),  # Mittelpunkt
    0.4,         # Radius
    0,           # Startwinkel
    270,         # Endwinkel (3/4-Kreis)
    edgecolor='black', facecolor='white', linewidth=0
)
ax.add_patch(three_quarter_wedge)

# Zeichne die vertikale Linie durch die Mitte
ax.plot([0.5, 0.5], [0.1, 0.9], color='black', linewidth=1)

# Zeichne die horizontale Linie durch die Mitte
ax.plot([0.1, 0.9], [0.5, 0.5], color='black', linewidth=1)

# Setze die Achsenbegrenzung und gleiche Skalierung
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Entferne Gitterlinien, Achsen und Ticks
ax.axis('off')

# Zeige die Figur
plt.show()
