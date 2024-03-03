class Album:
    def __init__(self, banda, album, ano, integrantes):
        self.banda = banda
        self.album = album
        self.ano = ano
        self.integrantes = integrantes

    def serialize(self):
        return {
            'banda': self.banda,
            'album': self.album,
            'ano': self.ano,
            'integrantes': self.integrantes
        }
