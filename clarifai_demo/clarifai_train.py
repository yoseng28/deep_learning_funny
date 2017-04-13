class ClarifaiTrain(object):
    # 创建concepts
    def create_concepts(self, app, concept_name, files, files_path):
        print('开始上传图片，创建concept...')
        for file in files:
            print(files_path + file)
            app.inputs.create_image_from_filename(files_path + file, concepts=[concept_name])
        print('创建concept成功！')

    # 创建model
    def create_model(self, app, model_id, concept_name):
        app.models.create(model_id=model_id, concepts=[concept_name])
        print('创建model成功！')

    # 添加concepts到已有模型中
    def add_concepts(self, app, model_id, concept_name):
        model = app.models.get(model_id)
        model.add_concepts([concept_name])
        print('添加concepts成功！')

    # 训练model
    def train_model(self, app, model_id):
        result = app.models.get(model_id)
        result.train()
        print('模型 [', model_id, '] 训练成功！')
