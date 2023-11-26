import cv2
import numpy as np

def geo_interpolation(x, x1, frame1_path, x2, frame2_path):

    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    if x1 == x2 or 0 in frame1.shape or 0 in frame2.shape:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais, e as imagens não podem ter dimensões nulas para a interpolação geométrica.")


    alpha = (x - x1) / (x2 - x1)
    interpolated_frame = cv2.pow(frame2 / frame1, alpha) * frame1

    return interpolated_frame.astype(np.uint8)

def calculate_second_derivative(frame, x):

    f_xx = frame[x + 1] - 2 * frame[x] + frame[x - 1] if 0 < x < len(frame) - 1 else 0
    return f_xx

def calculate_truncation_error(x, x1, x2, frame1, frame2):

    f_double_prime = (calculate_second_derivative(frame1, x1) + calculate_second_derivative(frame2, x2)) / 2


    error = ((x - x1) / (x2 - x1)) * ((x - x2) / (x1 - x2)) * f_double_prime
    return error

# Exemplo de uso:
x1, frame1_path = 2, "/home/celin/Desktop/interpolation/frames/frame_0002.png"
x2, frame2_path = 5, "/home/celin/Desktop/interpolation/frames/frame_0005.png"
x_interpolate = 3

frame1 = cv2.imread(frame1_path, cv2.IMREAD_COLOR)
frame2 = cv2.imread(frame2_path, cv2.IMREAD_COLOR)

result = geo_interpolation(x_interpolate, x1, frame1_path, x2, frame2_path)


truncation_error = calculate_truncation_error(x_interpolate, x1, x2, frame1, frame2)
print(truncation_error)