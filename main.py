from patterns.star_patterns import generate_right_angle_pattern

def main():
    """
    Main entry point for the star pattern generator.
    """
    print("Star Pattern Generator")
    print("-" * 22)
    
    try:
        rows = 5
        print(f"Right-Angle Pattern with {rows} rows:")
        pattern = generate_right_angle_pattern(rows)
        print(pattern)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
