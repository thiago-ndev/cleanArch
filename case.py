class AlgumaCoisa:
    def __enter__(self):
        print('Estou Dentro')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou Saindo')
