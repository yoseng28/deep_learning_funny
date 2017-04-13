class ClarifaiPredict(object):

    # 通过本地图片，调用相应model进行预测
    def predict_by_file_name(self, model, file_name):
        print('调用model：开始')
        result = model.predict_by_filename(file_name)
        print('返回json：\n', result)
        arr = result['outputs']
        items = arr[0]['data']['concepts']
        print('调用model：结束')
        return items

    # 通过图片URL，调用相应model进行预测
    def predict_by_file_url(self, model, file_url):
        print('调用model：开始')
        result = model.predict_by_url(file_url)
        print('返回json：\n', result)
        arr = result['outputs']
        items = arr[0]['data']['concepts']
        print('调用model：结束')
        return items
