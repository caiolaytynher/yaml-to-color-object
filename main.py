import yaml
import sys

INPUT_DIR = "./yaml-files"
OUTPUT_DIR = "./output-files"


def main(args: list[str]) -> None:
    if len(args) > 1:
        filename: str = args[1]
    else:
        raise Exception("No file name provided.")

    with open(f"{INPUT_DIR}/{filename}.yaml", "r") as input_file:
        color_pallete: dict = yaml.safe_load(input_file)

    with open(f"{OUTPUT_DIR}/{filename}.txt", "w") as output_file:
        output_file.write(f"ColorScheme(\n")
        for color_type, color_contents in color_pallete.items():
            output_file.write(f"\t{color_type}={color_type.capitalize()}(\n")
            for color_name, color_hex in color_contents.items():
                if color_hex.startswith("0x"):
                    color_hex = f"#{color_hex[2:]}"
                output_file.write(f"\t\t{color_name}={color_hex!r},\n")
            output_file.write(f"\t),\n")
        output_file.write(")")


if __name__ == "__main__":
    main(sys.argv)
