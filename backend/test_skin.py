from skin_tone import get_skin_tone as detect_skin_tone

# CHANGE THIS to your image file name
image_path = r"E:/Capstone/backend/test1.jpg"

result = detect_skin_tone(image_path)

print("RESULT:", result)