def input_error(func):
    def inner(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except (KeyError, ValueError, IndexError, TypeError, FileNotFoundError, IOError) as e:
            error_message = str(e) if str(e) else "An error occurred"
            return f"Error: {error_message}"
        except Exception as e:
            return f"Unknown error occurred: {str(e)}"

    return inner
