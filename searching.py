import os, json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, "lecture_searching", file_name)
    with open(file_path, mode="r") as file:
        data = json.load(file)
        for key, value in data.items():
            if key == field:
                return value
            else:
                continue
        return None

def main():
    sequential_data = read_data(file_name="sequential.json", field="unordered_numbers")
    print(sequential_data)
    


if __name__ == '__main__':
    main()