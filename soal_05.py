from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        self.antrian.append(pelanggan)

    def keluar(self):
        if self.is_empty:
            raise ('Antrian kosong')
        answer = self._antrian[self.front]
        return answer