import pyautogui
import ollama
import time
import argparse
import json
import os
import sys

def load_config(config_path="config.json"):
    """从 JSON 文件加载配置，失败则退出程序"""
    if not os.path.exists(config_path):
        print(f"错误: 配置文件 '{config_path}' 不存在，请创建后再运行。")
        sys.exit(1)
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"✓ 已加载配置文件: {config_path}")
            return config
    except json.JSONDecodeError as e:
        print(f"错误: 配置文件格式不正确 - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: 无法读取配置文件 - {e}")
        sys.exit(1)

def get_screenshot_path(region_type, custom_region=None):
    """根据配置截取指定区域"""
    screen_width, screen_height = pyautogui.size()
    
    if region_type == "right_half":
        region = (screen_width // 2, 0, screen_width // 2, screen_height)
    elif region_type == "left_half":
        region = (0, 0, screen_width // 2, screen_height)
    elif region_type == "full":
        region = (0, 0, screen_width, screen_height)
    elif region_type == "custom" and custom_region:
        region = tuple(custom_region[:4])
    else:
        raise ValueError(f"未知的截图区域类型: {region_type}")
    
    screenshot = pyautogui.screenshot(region=region)
    temp_path = "temp_screenshot.png"
    screenshot.save(temp_path)
    return temp_path

def screenshot_and_ask(config):
    print(f"📸 {config['delay']}秒后截图（区域: {config['region']}），请调整好窗口...")
    time.sleep(config['delay'])
    
    temp_image_path = get_screenshot_path(config['region'], config.get('custom_region'))
    print("🤖 正在询问 AI，请稍等...")

    try:
        res = ollama.chat(
            model=config['model'],
            messages=[{
                'role': 'user',
                'content': config['prompt'],
                'images': [temp_image_path]
            }]
        )
        answer = res['message']['content']
        print("\n========== AI 的回答 ==========")
        print(answer)
        print("================================\n")
        
        if config.get('output_file'):
            with open(config['output_file'], 'a', encoding='utf-8') as f:
                f.write(f"{time.ctime()}\n{answer}\n\n")
                
    except Exception as e:
        print(f"❌ 出错: {e}")

def main():
    parser = argparse.ArgumentParser(description="自动截图问 AI（Ollama 本地版）")
    parser.add_argument("--config", default="config.json", help="配置文件路径（默认 config.json）")
    args = parser.parse_args()
    
    # 只从配置文件加载，无默认值
    config = load_config(args.config)
    
    # 检查必需字段
    required_keys = ["model", "prompt", "region", "delay"]
    for key in required_keys:
        if key not in config:
            print(f"错误: 配置文件中缺少必需字段 '{key}'")
            sys.exit(1)
    
    print("本程序会截图并询问本地的 AI 模型。")
    print(f"当前配置: 模型={config['model']}, 区域={config['region']}, 延迟={config['delay']}秒")
    
    while True:
        input("👉 按回车键开始新一轮截图...")
        screenshot_and_ask(config)

if __name__ == "__main__":
    main()