import yaml
import sys

INPUT_DIR = "./yaml-files"
OUTPUT_DIR = "./output-files"


def main(args) -> None:
    if len(args) > 1:
        filename: str = args[1]
    else:
        raise Exception("No file name provided.")

    with open(f"{INPUT_DIR}/{filename}.yaml", "r") as input_file:
        contents: dict = yaml.safe_load(input_file)

    """
    person:
        name: "Caio"
        age: 21

    Person(
        name="Caio"
        age=21
    )
    """

    with open(f"{OUTPUT_DIR}/{filename}.txt", "w") as output_file:
        output_file.write(f"{filename}(\n")
        for key, value in contents.items():
            output_file.write(f"\t{key}={value!r}\n")
        output_file.write(")")


if __name__ == "__main__":
    main(sys.argv)
