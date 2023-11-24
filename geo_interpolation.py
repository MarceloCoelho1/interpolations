import cv2

def geo_interpolation(x, x1, frame1_path, x2, frame2_path, output_path):
    # Carrega os frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    if x1 == x2 or 0 in frame1.shape or 0 in frame2.shape:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais, e as imagens não podem ter dimensões nulas para a interpolação geométrica.")

    # Realiza a interpolação geométrica
    alpha = (x - x1) / (x2 - x1)
    interpolated_frame = cv2.pow(frame2 / frame1, alpha) * frame1

    # Salva o frame interpolado
    cv2.imwrite(output_path, interpolated_frame)

# Exemplo de uso:
x1, frame1_path = 1, "/home/celin/Desktop/interpolation/frames/frame_0001.png"
x2, frame2_path = 100, "/home/celin/Desktop/interpolation/frames/frame_0100.png"
x_interpolate = 50
output_path = "/home/celin/Desktop/interpolation/frames/frame_0050geo_interpolate.png"


geo_interpolation(x_interpolate, x1, frame1_path, x2, frame2_path, output_path)
