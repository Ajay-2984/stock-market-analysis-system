def line():

    print("=" * 65)


def title(text):

    line()

    print(text.center(65))

    line()


def success(message):

    print("\n" + "=" * 65)

    print(("✓ " + message).center(65))

    print("=" * 65)


def error(message):

    print("\n" + "=" * 65)

    print(("✗ " + message).center(65))

    print("=" * 65)


def pause():

    input("\nPress Enter to continue...")
