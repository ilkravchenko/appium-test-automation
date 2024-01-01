import subprocess
import re


def get_connected_devices():
    try:
        # Run the adb devices command using subprocess and capture the output
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)

        # Extract device information using regular expression
        device_info = re.findall(r'(\S+)\s+device', result.stdout)

        # Extract only the udid from the device information
        udid_list = [info for info in device_info]

        return udid_list[1:]

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []


def get_dynamic_udid():
    # Get the list of connected devices
    devices = get_connected_devices()

    if not devices:
        print("No connected devices found.")
        return None

    # If there's only one device, return its UDID
    if len(devices) == 1:
        return devices[0]

    # If there are multiple devices, prompt the user to select one
    print("Multiple devices found. Please select a device:")
    for i, device in enumerate(devices, start=1):
        print(f"{i}. {device}")

    try:
        # Get user input for device selection
        selection = int(input("Enter the number of the device: "))
        if 1 <= selection <= len(devices):
            return devices[selection - 1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


# Example usage:
udid = get_dynamic_udid()

if udid:
    print(f"Selected UDID: {udid}")
else:
    print("No UDID selected.")
