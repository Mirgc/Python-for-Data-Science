import sys

def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(lst)
    progress = 0
    bar_length = 30

    for elem in lst:
        progress += 1
        percent = progress / total
        filled_length = int(bar_length * percent)
        bar = '█' * filled_length + ' ' * (bar_length - filled_length)
        sys.stdout.write(f'\r{percent*100:.2f}% |[{bar}]| {progress}/{total}')
        sys.stdout.flush()
        yield elem # Devuelvo el elemento
    sys.stdout.write('\n')
    sys.stdout.flush()
    return