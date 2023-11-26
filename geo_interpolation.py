import cv2
import numpy as np
import os

def geo_interpolation(x, x1, frame1_path, x2, frame2_path, output_path):
    
    # Carrega os frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    if x1 == x2 or 0 in frame1.shape or 0 in frame2.shape:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais, e as imagens não podem ter dimensões nulas para a interpolação geométrica.")


    alpha = (x - x1) / (x2 - x1)
    interpolated_frame = cv2.pow(frame2 / frame1, alpha) * frame1
    
    interpolated_frame = np.nan_to_num(interpolated_frame, nan=-999999999, posinf=999999999, neginf=-999999999)

    return interpolated_frame.astype(np.uint8)

def calculate_second_derivative(frame, x):

    f_xx = frame[x + 1] - 2 * frame[x] + frame[x - 1] if 0 < x < len(frame) - 1 else 0
    return f_xx

def calculate_truncation_error(x, x1, x2, frame1, frame2):

    f_double_prime = (calculate_second_derivative(frame1, x1) + calculate_second_derivative(frame2, x2)) / 2


    error = ((x - x1) / (x2 - x1)) * ((x - x2) / (x1 - x2)) * f_double_prime
    return error

# Exemplo de uso:
current_working_directory = os.getcwd()
x1, frame1_path = 50, f"{current_working_directory}/frames/frame_0050.png"
x2, frame2_path = 100, f"{current_working_directory}/frames/frame_0100.png"
x_interpolate = 75
output_path = f"{current_working_directory}/frames/frame_0075_geo_interpolate.png"