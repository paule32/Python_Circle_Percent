import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Erstelle eine Figur und eine Achse mit festgelegter Fenstergröße
fig, ax = plt.subplots(figsize=(1.0, 1.0))  # figsize in Zoll, 1 Zoll = 100 Pixel

# Füge einen Kreis hinzu
circle = patches.Circle((0.5, 0.5), radius=0.4, edgecolor='black', facecolor='green', linewidth=2)

# Kreis zur Achse hinzufügen
ax.add_patch(circle)

# Setze die Achsenbegrenzung und gleiche Skalierung
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

ax.axis('off')
# Zeige die Figur
plt.show()
