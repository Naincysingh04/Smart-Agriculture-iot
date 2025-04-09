from sensor_reader import get_soil_moisture, get_temperature
from irrigation_predictor import IrrigationModel
from notify_user import send_notification
import time

def main():
    model = IrrigationModel()

    while True:
        moisture = get_soil_moisture()
        temp = get_temperature()

        print(f"[Sensor] Moisture: {moisture}%, Temp: {temp}°C")
        prediction = model.predict(moisture, temp)

        if prediction == 1:
            send_notification(f"Irrigation Needed! Soil Moisture: {moisture}%, Temp: {temp}°C")
        else:
            print("Irrigation not needed.")

        time.sleep(300)  # Wait 5 minutes

if __name__ == "__main__":
    main()

