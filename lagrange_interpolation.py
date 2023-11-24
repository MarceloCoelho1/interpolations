import numpy as np
import cv2

def lagrange_interpolation_frames(x, frames, x_new, output_path):
    n = len(x)

    # Carrega os frames
    frames_data = [cv2.imread(frame_path) for frame_path in frames]

    # Verifica o número de canais
    num_channels = frames_data[0].shape[2] if len(frames_data[0].shape) == 3 else 1

    L = np.zeros(n)
    for i in range(n):
        numerator = np.prod(x_new - np.delete(x, i))
        denominator = np.prod(x[i] - np.delete(x, i))
        L[i] = numerator / denominator

    # Para cada canal, realiza a interpolação de Lagrange
    for channel in range(num_channels):
        # Calcula o valor interpolado para o novo frame
        interpolated_channel = np.sum(np.array([frame[:, :, channel] * L[i] for i, frame in enumerate(frames_data)]), axis=0)

        # Cria o novo frame com o canal interpolado
        interpolated_frame = frames_data[0].copy()
        interpolated_frame[:, :, channel] = interpolated_channel.astype(np.uint8)

        # Salva o novo frame
        cv2.imwrite(output_path.format(channel=channel), interpolated_frame)

# Exemplo de uso:
x = np.array([2, 100])
frames = ["/home/celin/Desktop/interpolation/frames/frame_0002.png", "/home/celin/Desktop/interpolation/frames/frame_0100.png"]
x_new = 50
output_path = "/home/celin/Desktop/interpolation/frames/frame_050_interpolatedlagrange.png"

lagrange_interpolation_frames(x, frames, x_new, output_path)
