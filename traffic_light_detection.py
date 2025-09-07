import cv2
import numpy as np

def detect_traffic_light_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV ranges for Red, Yellow, Green
    lower_red1, upper_red1 = np.array([0, 100, 100]), np.array([10, 255, 255])
    lower_red2, upper_red2 = np.array([160, 100, 100]), np.array([179, 255, 255])
    lower_yellow, upper_yellow = np.array([15, 150, 150]), np.array([35, 255, 255])
    lower_green, upper_green = np.array([40, 100, 100]), np.array([90, 255, 255])

    # Create masks for colors
    red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    colors = {
        "RED": cv2.countNonZero(red_mask),
        "YELLOW": cv2.countNonZero(yellow_mask),
        "GREEN": cv2.countNonZero(green_mask)
    }

    detected_color = max(colors, key=colors.get)
    return detected_color, red_mask, yellow_mask, green_mask

def draw_bounding_boxes(frame, mask, color_name, color_bgr):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:  # Ignore small spots
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color_bgr, 2)
            cv2.putText(frame, color_name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_bgr, 2)

cap = cv2.VideoCapture(0)  # Use webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    color, red_mask, yellow_mask, green_mask = detect_traffic_light_color(frame)

    # Draw bounding boxes for each detected color
    draw_bounding_boxes(frame, red_mask, "RED", (0, 0, 255))
    draw_bounding_boxes(frame, yellow_mask, "YELLOW", (0, 255, 255))
    draw_bounding_boxes(frame, green_mask, "GREEN", (0, 255, 0))

    # Show action message based on detection
    if color == "RED":
        message, color_bgr = "STOP 🚫", (0, 0, 255)
    elif color == "YELLOW":
        message, color_bgr = "GET READY ⚠️", (0, 255, 255)
    else:
        message, color_bgr = "GO ✅", (0, 255, 0)

    cv2.putText(frame, f"Traffic Light: {color} | {message}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_bgr, 2)

    cv2.imshow("Traffic Light Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
