class Pipeline:
    def __init__(self, preprocess, feature, model):
        self.pre = preprocess
        self.fea = feature
        self.model = model

    def fit(self, X_train):
        df1 = self.pre.transform(X_train)
        df2 = self.fea.transform(df1)
        df3 = self.model.fit(df2)
        return self

    def transform(self, X_test):
        df1 = self.preprocess.transform(X_test)
        df2 = self.feature.transform(df1)
        df3 = self.model.predict(df2)
        return df3

class Preprocess():
    def __init__(self, *args):
        self.args = args

    def transform(self, dataframe):
        pass

class Feature():
    def __init__(self, *args):
        self.args = args

    def transform(self, dataframe):
        pass