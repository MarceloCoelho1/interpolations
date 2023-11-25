import cv2
import numpy as np

def linear_interpolation(x, x1, frame1_path, x2, frame2_path):
    # Carrega os frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    if x1 == x2:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais para a interpolação linear.")

    # Realiza a interpolação linear
    interpolated_frame = frame1 + (x - x1) * (frame2 - frame1) / (x2 - x1)
    return interpolated_frame.astype(np.uint8)

# Exemplo de uso:
x1, frame1_path = 2, "/home/celin/Desktop/interpolation/frames/frame_0002.png"
x2, frame2_path = 5, "/home/celin/Desktop/interpolation/frames/frame_0005.png"
x_interpolate = 3

result = linear_interpolation(x_interpolate, x1, frame1_path, x2, frame2_path)
cv2.imwrite('/home/celin/Desktop/interpolation/frames/frame_0003_interpolate.png', result)
