import numpy as np
from PIL import Image

class Model:
    """Klasa Model obsługująca logikę aplikacji, w tym kompresję obrazów."""

    def load_image(self, file_path):
        """Ładowanie obrazu oraz jego konwersja do macierzy NumPy."""
        try:
            image = Image.open(file_path)
            return np.array(image), image.mode
        except Exception as e:
            raise ValueError(f"Nie można załadować obrazu: {e}")

    def svd_compression(self, image_matrix, mode, r):
        """Kompresja obrazu z wykorzystaniem SVD."""
        try:
            if mode == 'L':  # Skala szarości
                U, S, Vt = np.linalg.svd(image_matrix, full_matrices=False)
                S = np.diag(S[:r])
                compressed = U[:, :r] @ S @ Vt[:r, :]
                return compressed
            elif mode in ['RGB', 'RGBA']:  # Kolor
                channels = []
                for i in range(image_matrix.shape[2]):  # Rozdzielenie kanałów
                    U, S, Vt = np.linalg.svd(image_matrix[:, :, i], full_matrices=False)
                    S = np.diag(S[:r])
                    compressed_channel = U[:, :r] @ S @ Vt[:r, :]
                    channels.append(compressed_channel)
                return np.stack(channels, axis=2)
            else:
                raise ValueError("Nieobsługiwany tryb obrazu.")
        except Exception as e:
            raise ValueError(f"Błąd podczas kompresji obrazu: {e}")
