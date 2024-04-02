import json
import pandas as pd
import os
from config import DATA_CONFIG

def remove_api_params_and_save(file_path, new_file_path):
    try:
        # 读取 JSON 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 删除每个条目中的 'api_params' 字段
        for item in data:
            if 'api_params' in item:
                del item['api_params']

        # 将修改后的数据写入新的 JSON 文件
        with open(new_file_path, 'w', encoding='utf-8') as new_file:
            json.dump(data, new_file, indent=4, ensure_ascii=False)

        print("Data successfully written to new file.")
    except Exception as e:
        print(f"Error in remove_api_params_and_save: {e}")

def json_to_csv(json_file_path, csv_file_path):
    try:
        # 读取 JSON 文件
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 从 JSON 数据创建 DataFrame
        df = pd.DataFrame(data)

        # 将 DataFrame 保存到 CSV 文件
        df.to_csv(csv_file_path, index=False)

        print("JSON converted to CSV successfully.")
    except Exception as e:
        print(f"Error in json_to_csv: {e}")

# 直接调用这个就可以了
def one_step_to_csv(json_file_path, new_file_path, csv_file_path):
    try:
        remove_api_params_and_save(json_file_path, new_file_path)
        json_to_csv(new_file_path, csv_file_path)
    except Exception as e:
        print(f"Error in one_step_to_csv: {e}")

def update_api_csv():
    json_file = DATA_CONFIG['api_json_file']
    csv_file = DATA_CONFIG['api_csv_file']
    temp_file = "data/tmp/api.json"

    one_step_to_csv(json_file, temp_file, csv_file)

    # 删除临时文件
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print("removed temp file")

    print("API CSV file updated successfully.")
