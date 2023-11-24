import cv2
import os

def extract_frames(video_path, output_folder):
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)

    # Verifica se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    # Cria a pasta de saída se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Inicializa algumas variáveis
    frame_count = 0

    # Loop para extrair os frames
    while True:
        # Lê o próximo frame
        ret, frame = cap.read()

        # Verifica se chegou ao final do vídeo
        if not ret:
            break

        # Salva o frame como uma imagem
        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

    # Libera o objeto de captura de vídeo
    cap.release()

    print(f"{frame_count} frames extraídos com sucesso.")

# Exemplo de uso:
video_path = "/home/celin/Desktop/interpolation/example.mp4"
output_folder = "/home/celin/Desktop/interpolation/frames"

extract_frames(video_path, output_folder)
