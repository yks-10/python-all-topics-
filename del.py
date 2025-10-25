class Contextmangaer:

    def __entry__(self, path, operation):
        try:
            x = open(path, operation)
            return x
         except Exception as FileNotFound:
            return str(e)
        except Exception as e:
            return str(e)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return exce
