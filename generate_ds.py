import json
import random

def read_file(fileName):
    with open(fileName, 'r') as json_file:
        json_list = list(json_file)
    return json_list

def write_file(json_list, miniName, smallName):
    length = len(json_list)
    mini_index = random.sample(range(length), int(length/40))
    small_index = random.sample(range(length), int(length/20))
    with open(miniName, 'w') as outfile1:
        for i in mini_index:
            json_string = json_list[i]
            outfile1.write(json_string)
    with open(smallName, 'w') as outfile2:
        for i in small_index:
            json_string = json_list[i]
            outfile2.write(json_string)


if __name__ == "__main__":
    json_list = read_file("dev.jsonl")
    write_file = write_file(json_list, "dev_mini.jsonl", "dev_small.jsonl")
