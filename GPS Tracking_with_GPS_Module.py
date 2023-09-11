import gpsd

def main():
    # Connect to the local gpsd service
    gpsd.connect()

    try:
        while True:
            packet = gpsd.get_current()
            print(f"Latitude: {packet.latitude}, Longitude: {packet.longitude}")
    except KeyboardInterrupt:
        print("GPS tracking stopped.")

if __name__ == "__main__":
    main()
