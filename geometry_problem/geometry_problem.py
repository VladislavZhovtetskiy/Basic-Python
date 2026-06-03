'''
The slant height and lateral edge of a regular triangular pyramid are
Both 25 cm. The apothem of the pyramid is equal to the radius of the
Base of the cone. Calculate the area (in square centimetres) of the
Lateral surface of the pyramid, given that the area of the lateral
Surface of the cone is 500 pi cm²
'''

# Solution
# Generating line of a cone = edge of a regular triangular pyramid.
# The pyramid is regular and triangular, so its lateral edges are
# Equal in length, and its base is a regular triangle.
# Apothem = radius of the base of the cone.
# The lateral surface area of the cone = 500π cm² =>

# Import math
import math

# Static script
def calculate_static_pyramid_area():
    radius = (500 * math.pi) / (25 * math.pi)
    half_of_the_base = math.sqrt((25 ** 2 - 20 ** 2))
    base = half_of_the_base * 2
    lateral_area_pyramid = (base * 3 * radius) / 2
    print(f"Static calculation: The lateral surface area equal {int(round(lateral_area_pyramid, 1))} cm²")





def get_geometry_data():
    while True:
        try:
            generating_line = float(input("Enter the slant height of the cone (L): "))
            side_edge = float(input("Enter the lateral edge of the pyramid (b): "))
            cone_area_coefficient = float(input("Enter the cone lateral area coefficient (before pi): "))
            lateral_surface_cone = cone_area_coefficient * math.pi
        except ValueError:
            print("Please, enter a correct value")
            continue

        if generating_line <= 0 or side_edge <= 0 or lateral_surface_cone <= 0:
            print("Please, write a correct value")
            continue

        radius_of_cone = lateral_surface_cone / (math.pi * generating_line)

        apothem = radius_of_cone

        if side_edge <= apothem:
            print(f"Geometry error: Side edge ({side_edge}) must be greater than the calculated apothem ({apothem:.2f}).")
            continue

        return side_edge, apothem


def calculate_pyramid_lateral_area(side_edge, apothem):
    half_pyramid_base = math.sqrt(side_edge ** 2 - apothem ** 2)

    base_side = half_pyramid_base * 2

    perimeter = base_side * 3

    lateral_area = (perimeter * apothem) / 2
    return lateral_area

def main():
    calculate_static_pyramid_area()
    print("-" * 30)

    print("Interactive Calculation:")
    edge_val, apothem_val = get_geometry_data()
    final_area = calculate_pyramid_lateral_area(edge_val, apothem_val)

    print("\n--- Geometric Results ---")
    print(f"Calculated Apothem (Radius): {apothem_val:.2f} cm")
    print(f"The lateral area of the pyramid is: {final_area:.2f} cm²")

if __name__ == "__main__":
    main()
