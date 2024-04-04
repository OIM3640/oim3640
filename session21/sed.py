def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    with open(source) as f_read, open(dest, "w") as f_write:
        # s = f_read.read()
        # s = s.replace(pattern, replace)
        # f_write.write(s)
        for line in f_read.readlines():
            words = line.split()  # a list of words in a line
            for i, word in enumerate(words):
                if word == "man":
                    words[i] = "woman"
            line = " ".join(words) + '\n'
            f_write.write(line)


def main():
    pattern = "man"
    replace = "woman"
    source = "data/output.txt"
    dest = "data/output2.txt"
    sed(pattern, replace, source, dest)


if __name__ == "__main__":
    main()
