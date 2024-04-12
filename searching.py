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
    print(linear_search(sequence=sequential_data, element= 0))
   
def linear_search(sequence, element):
    """
    Searches through sequence to get the element using naive algorithm 
    input: 
        sequence: sequence of elements
        element: desired element of the sequence
    output: lin_dict (dict): dictionary containing keys: index and count
    """
    count = 0
    lin_dict = dict()
    idx_list = list()

    for idx, item in enumerate(sequence):
        if item == element:
            count += 1   
            idx_list.append(idx)

    lin_dict = {"index":idx_list, "count": count}
        
    return lin_dict

if __name__ == '__main__':
    main()