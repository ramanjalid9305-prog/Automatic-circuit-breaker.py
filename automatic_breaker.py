import random
import time
from datetime import datetime

# Protection limits
MAX_CURRENT = 20.0       # Amps
MAX_VOLTAGE = 250.0      # Volts

BREAKER_ON = True


def read_sensor_data():
    """
    Simulate voltage and current measurements.

    In a real system, replace this function with appropriately
    isolated and rated measurement hardware.
    """

    voltage = random.uniform(220, 260)
    current = random.uniform(5, 30)

    return voltage, current


def check_fault(voltage, current):
    """Check whether a protection limit has been exceeded."""

    faults = []

    if current > MAX_CURRENT:
        faults.append("OVER CURRENT")

    if voltage > MAX_VOLTAGE:
        faults.append("OVER VOLTAGE")

    return faults


def trip_breaker():
    """Trip the circuit breaker."""

    global BREAKER_ON

    BREAKER_ON = False
    print("⚠ CIRCUIT BREAKER: TRIPPED")


def reset_breaker():
    """Reset the circuit breaker."""

    global BREAKER_ON

    BREAKER_ON = True
    print("✓ CIRCUIT BREAKER: ON")


def main():

    global BREAKER_ON

    print("=" * 60)
    print("          AUTOMATIC CIRCUIT BREAKER SYSTEM")
    print("=" * 60)

    try:

        while True:

            if not BREAKER_ON:
                print("\nBreaker is OFF.")
                print("Reset the system manually to continue.")
                break

            voltage, current = read_sensor_data()

            faults = check_fault(
                voltage,
                current
            )

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            print("\n--------------------------------------------")
            print(f"Time     : {timestamp}")
            print(f"Voltage  : {voltage:.2f} V")
            print(f"Current  : {current:.2f} A")
            print(f"Breaker  : {'ON' if BREAKER_ON else 'OFF'}")

            if faults:

                print("\n⚠ FAULT DETECTED")

                for fault in faults:
                    print(f"  - {fault}")

                trip_breaker()

            else:

                print("Status   : NORMAL")

            print("--------------------------------------------")

            time.sleep(3)

    except KeyboardInterrupt:

        BREAKER_ON = False
        print("\nSystem stopped safely.")
        reset_breaker()


if __name__ == "__main__":
    main()
