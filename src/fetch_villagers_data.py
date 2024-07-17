import os
import requests

# 创建文件夹以存储抓取的数据
raw_data_dir = os.path.join(os.path.dirname(__file__), 'raw')
if not os.path.exists(raw_data_dir):
    os.makedirs(raw_data_dir)

def fetch_villagers_data(url):
    """
    从给定的API URL获取村民数据
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # 返回JSON数据
    else:
        print(f"Failed to retrieve data from {url}")
        return None

def save_content(title, content):
    """
    将抓取的内容保存到raw文件夹中
    """
    filename = f"{title}.json"
    filepath = os.path.join(raw_data_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    url = 'http://127.0.0.1:8000/villagers'
    data = fetch_villagers_data(url)
    if data:
        import json
        title = 'villagers'
        save_content(title, json.dumps(data, indent=4))
        print(f"Saved content for {title}")
    else:
        print(f"Failed to save content for {title}")

if __name__ == "__main__":
    main()
