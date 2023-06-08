#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    result = 0
    for a in range(len(sys.argv) - 1):
        result = sum(int(arg))
        result += int(sys.argv[a + 1])
    print("{}".format(result))

"""import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments

    result = sum(int(arg) for arg in argv)
    print(result)"""
