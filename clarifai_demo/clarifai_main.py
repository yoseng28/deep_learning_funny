from clarifai.rest import ClarifaiApp
from clarifai_demo import clarifai_predict, config, out_result, clarifai_train, files_tools


class ClarifaiMain(object):
    def __init__(self):
        self.my_result = out_result.OutResult()
        self.my_predict = clarifai_predict.ClarifaiPredict()
        self.my_train = clarifai_train.ClarifaiTrain()
        self.my_files = files_tools.FilesTools()

    # 通过本地图片进行预测
    def predict_by_image_file(self, model):
        result = self.my_predict.predict_by_file_name(model, config.Predict_File_Name)
        self.my_result.out_file_image(result, config.Out_File_Path)

    # 通过图片URL进行预测
    def predict_by_image_url(self, model):
        result = self.my_predict.predict_by_file_url(model, config.Predict_File_url)
        self.my_result.out_file_image(result, config.Out_File_Path)

    # 图片预测入口
    def predict_main(self, app, model_name, *status):
        if not status:
            model = app.models.get(config.Public_Model_Name[model_name])
        else:
            model = app.models.get(config.Own_Model_Name[model_name])
        self.predict_by_image_file(model)
        # self.predict_by_image_url(model)

    # 模型训练1---上传图片，创建concept
    def train_create_concepts(self, app, concept_name, files_path):
        files = self.my_files.get_files_list(files_path)
        self.my_train.create_concepts(app, concept_name, files, files_path)

    # 模型训练2---创建模型
    def train_create_model(self, app, model_id, concept_name):
        self.my_train.create_model(app, model_id, concept_name)

    # 模型训练3---添加concepts
    def train_add_concepts(self, app, model_id, concept_name):
        self.my_train.add_concepts(app, model_id, concept_name)

    # 模型训练4---训练模型
    def train_model(self, app, model_id):
        self.my_train.train_model(app, model_id)


if __name__ == '__main__':
    print('连接API...')
    app = ClarifaiApp(config.Client_Id, config.Client_Secret)
    run = ClarifaiMain()

    # 预测，own为使用自己的模型，为可选参数
    #run.predict_main(app, 'nba', 1)
    run.predict_main(app, 'nsfw')

    # 训练
    # run.train_create_concepts(app, 'liuxiang', 'images/train/liuxiang/')
    # run.train_create_model(app, 'china', 'yaoming')
    # run.train_add_concepts(app, 'china', 'liuxiang')
    # run.train_model(app, 'china')
