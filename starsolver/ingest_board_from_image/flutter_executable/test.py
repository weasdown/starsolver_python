import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path: str = sys.argv[1]
        print(f'{image_path = }')
        # print(sys.argv[1])
    else:
        raise RuntimeError('An image_path must be provided.')
