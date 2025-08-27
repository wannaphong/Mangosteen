import json
from datasets import load_dataset
# get Croatian data
fw = load_dataset("HuggingFaceFW/fineweb-2", name="tha_Thai", split="train", streaming=True)

def create_jsonl_file(data: list, filename: str) -> None:
    """
    Creates a JSONL file from a list of dictionaries.

    A JSONL (JSON Lines) file is a plain text file where each line
    is a valid JSON object, separated by a newline character.

    Args:
        data (list): A list of dictionaries to write to the file.
        filename (str): The name of the JSONL file to create.
    """
    try:
        # Open the file in write mode ('w'). Using 'with' ensures the file is
        # automatically closed even if errors occur.
        with open(filename, 'w', encoding='utf-8') as f:
            # Iterate through each item (dictionary) in the provided list.
            for item in data:
                # Serialize the dictionary to a JSON formatted string.
                # The `json.dumps` function converts a Python dictionary to a JSON string.
                json_string = json.dumps(item, ensure_ascii=False)
                
                # Write the JSON string to the file, followed by a newline character.
                # The newline is crucial for maintaining the JSONL format.
                f.write(json_string + '\n')
        
        print(f"Successfully created {filename}")

    except IOError as e:
        print(f"An error occurred while writing the file: {e}")
    except TypeError as e:
        print(f"Invalid data format. Please provide a list of dictionaries. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

n=0
data=[]

for i in fw:
    if n+1>100:
        break
    _d={}
    _d["text"]=i["text"]
    _d["metadata"]={"url":i["url"]}
    _d["id"]=i["id"]
    data.append(_d)
    n+=1

create_jsonl_file(data, "fw2.jsonl")