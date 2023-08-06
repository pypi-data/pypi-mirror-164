# 导入相关模块
import pandas as pd
import numpy as np

from catboost import CatBoostClassifier, CatBoostRegressor, Pool
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics

from IPython.display import display
import plotly
import plotly.express as px
import shap
import matplotlib.pyplot as plt
import seaborn as sns

# 读入数据
def getCSVFile(filePath):
    try:
        df = pd.read_csv(filePath)
        return df
    except:
        print('文件读入异常')

# 数据预处理
def dataCleaning(work_df, del_cols):
    # 删除列
    work_df.drop(del_cols, axis=1, inplace=True)
    # 类别型特征
    cat_feas, con_feas = [], []
    for col in work_df.columns:
        if work_df[col].dtype is np.dtype('float') or work_df[col].dtype is np.dtype('int'):
            con_feas.append(col)
        else:
            cat_feas.append(col)
    # 处理缺失值
    for f in cat_feas:
        work_df[f] = work_df[f].fillna('0')
        work_df[f] = work_df[f].apply(lambda x: '0' if x == '0.0' else x)
    for f in con_feas:
        work_df[f] = work_df[f].fillna(0)
    return work_df

def feature_en_cn(feature_name_file_path):
    # feature中英文对照
    feature_name_df = pd.read_csv(feature_name_file_path)
    feature_dic = {}
    for i in range(feature_name_df.shape[0]):
        feature_dic[feature_name_df['name_en'][i]] = feature_name_df['name_cn'][i]
    return feature_dic

def catboostModel(model_df, label_feature, feature_dic):
    train, val, test = np.split(model_df.sample(frac=1, random_state=42), [int(.6*len(model_df)), int(.8*len(model_df))])
    train_y1, val_y1, test_y1 = train[label_feature], val[label_feature], test[label_feature]
    train1, val1, test1 = train.drop([label_feature], axis=1), val.drop([label_feature], axis=1), test.drop([label_feature], axis=1)

    cat_feas, con_feas = [], []
    for col in model_df.columns:
        if model_df[col].dtype is np.dtype('float') or model_df[col].dtype is np.dtype('int'):
            con_feas.append(col)
        else:
            cat_feas.append(col)
    data_cols = model_df.columns
    cat_features = [item for item in cat_feas if item in data_cols]
    con_features = [item for item in con_feas if item in data_cols]

    # 训练模型
    params = {'learning_rate':0.05, 'iterations':200}
    clf = CatBoostClassifier(eval_metric='AUC', **params)
    pool = Pool(train1, train_y1, cat_features=cat_features)
    clf.fit(pool, eval_set=(val1, val_y1), use_best_model=True, early_stopping_rounds=20, verbose=10)

    sns.set_theme()
    plt.rcParams['font.family'] = 'Heiti TC'

    # 对模型文件model进行解释
    X = train1
    clf_r = clf
    samp_cols = X.columns
    samp_cols_cn = []
    for i in samp_cols:
        if i in feature_dic.keys():
            samp_cols_cn.append(feature_dic[i])
        else:
            samp_cols_cn.append(i)
    explainer = shap.Explainer(clf_r)
    X.columns = samp_cols_cn
    shap_values = explainer(X)
    sample_data = X
    # 计算所有特征的影响
    shap.summary_plot(shap_values, sample_data, max_display=80, show=False)

    plt.savefig('/Users/user/Desktop/shap_summary.png')
    print('桌面图片保存成功')

    return clf

def shapValue(clf, feature_dic):
    plt.figure(figsize=(12,8))

    # html显示
    dfimportance = clf.get_feature_importance(prettified=True)
    dfimportance_plot = dfimportance.sort_values(by = "Importances", ascending=True).iloc[-100:]
    dfimportance_plot.columns = ['feature_name', 'importances']
    dfimportance_plot['feature_name_coded'] = dfimportance_plot['feature_name'].apply(lambda x: x if x not in feature_dic.keys() else feature_dic[x])

    fig_importance = px.bar(dfimportance_plot,x="importances",y="feature_name_coded",title="Feature Importance", width=1200, height=1000)
    return fig_importance

def main(file_path, del_cols, label_feature, feature_name_file_path, root, jpg_name):
    work_df = getCSVFile(file_path)
    model_df = dataCleaning(work_df, del_cols)
    feature_dic = feature_en_cn(feature_name_file_path)
    clf = catboostModel(model_df, label_feature, feature_dic)
    jpgFile = shapValue(clf, feature_dic)
    path = root + jpg_name + '.html'
    plotly.offline.plot(jpgFile, filename='path')
    print('文件保存成功')

