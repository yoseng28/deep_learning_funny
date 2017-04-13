import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class OutResult(object):

    def out_file(self, items, out_file_path):
        try:
            with open(out_file_path, 'w', encoding='utf-8') as file:
                file.write('name:value\n\n')
                for item in items:
                    file.write(item['name'] + ':' + str(item['value']) + '\n')
                file.close()
            print("文件生成成功！")
        except IOError:
            print("文件写入失败！")

    def out_image(self, out_file_path):
        print('绘制图像中...')
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        mydata = pd.read_table(out_file_path, sep=':', encoding='utf8')
        label = mydata['name'].T.values
        xtop = mydata['value'].T.values
        idx = np.arange(len(xtop))
        plt.barh(idx, xtop, color='b', alpha=0.6)
        plt.yticks(idx + 0.4, label)
        plt.grid(axis='x')
        plt.xlabel('预测值')
        plt.ylabel('标注名')
        plt.title('Clarifai-图片内容标注')
        plt.show()

    def out_file_image(self, items, out_file_path):
        main = OutResult()
        main.out_file(items, out_file_path)
        main.out_image(out_file_path)
