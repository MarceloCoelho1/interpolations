import cv2

def linear_interpolation(x, x1, frame1_path, x2, frame2_path, output_path):
    # Carrega os frames
    frame1 = cv2.imread(frame1_path)
    frame2 = cv2.imread(frame2_path)

    if x1 == x2:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais para a interpolação linear.")

    # Realiza a interpolação linear
    interpolated_frame = cv2.addWeighted(frame1, 1 - (x - x1) / (x2 - x1), frame2, (x - x1) / (x2 - x1), 0)

    # Salva o frame interpolado
    cv2.imwrite(output_path, interpolated_frame)

# Exemplo de uso:
x1, frame1_path = 2, "caminho/do/seu/output/folder/frame_0001.png"
x2, frame2_path = 5, "caminho/do/seu/output/folder/frame_0005.png"
x_interpolate = 3
output_path = "caminho/do/seu/output/folder/interpolated_frame.png"

linear_interpolation(x_interpolate, x1, frame1_path, x2, frame2_path, output_path)
