import os
import json


data = ["asd", "bsd"]
app_name = "test"


def saveData(final_resp, app_name):
    """Saves the data in json format"""

    def write_json(target_path, target_file, data):
        if not os.path.exists(target_path):
            try:
                os.makedirs(target_path)
            except Exception as e:
                print(e)
                raise
        with open(os.path.join(target_path, target_file), "w") as f:
            print(os.path.join(target_path, target_file))
            json.dump(data, f)

    write_json("output", f"{app_name}_data.json", final_resp)


saveData(data, app_name=app_name)
