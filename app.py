from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 获取图像文件夹路径
image_folder = r'D:\nccu_rev2\input'

# 获取图像文件列表
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

@app.route('/')
def index():
    # 将图像文件列表传递给HTML模板
    return render_template('index.html', image_files=image_files)

# 新增路由用于加载图像文件
@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory(image_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)
