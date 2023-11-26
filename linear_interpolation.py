import cv2
import numpy as np
import os

def linear_interpolation(x, x1, frame1_path, x2, frame2_path, output_path):
    # Carrega os frames
    frame1 = cv2.imread(frame1_path).astype(float)
    frame2 = cv2.imread(frame2_path).astype(float)

    if x1 == x2:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais para a interpolação linear.")


    interpolated_frame = frame1 + (x - x1) * (frame2 - frame1) / (x2 - x1)
    interpolated_frame = np.nan_to_num(interpolated_frame, nan=-999999999, posinf=999999999, neginf=-999999999)

    # Converte o resultado de volta para o tipo de dados adequado
    interpolated_frame = interpolated_frame.astype(np.uint8)
    
    cv2.imwrite(output_path, interpolated_frame)

# Restante do código permanece o mesmo
current_working_directory = os.getcwd()
x1, frame1_path = 1, f"{current_working_directory}/frames/frame_0001.png"
x2, frame2_path = 24, f"{current_working_directory}/frames/frame_0024.png"
x_interpolate = 12
output_path = f"{current_working_directory}/frames/frame_0012_interpolate.png"

linear_interpolation(x_interpolate, x1, frame1_path, x2, frame2_path, output_path)