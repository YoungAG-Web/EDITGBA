import sys
import os
from emulator import Emulator  # Replace this with the actual module where your emulator logic resides

def main():
    # Print a banner for the emulator
    print("===================================")
    print("        GBA Emulator Runner        ")
    print("===================================")

    # Check if the user provided a ROM file
    if len(sys.argv) < 2:
        print("Usage: python run_emulator.py <path-to-rom>")
        sys.exit(1)

    rom_path = sys.argv[1]

    # Check if the ROM file exists
    if not os.path.exists(rom_path):
        print(f"Error: ROM file '{rom_path}' does not exist.")
        sys.exit(1)

    try:
        # Initialize the emulator
        emulator = Emulator()

        # Load the ROM
        print(f"Loading ROM from: {rom_path}")
        emulator.load_rom(rom_path)

        # Run the emulator
        print("Starting the emulator. Press Ctrl+C to exit.")
        emulator.run()

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
