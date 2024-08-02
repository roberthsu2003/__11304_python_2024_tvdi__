import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score,confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
import seaborn as sns

from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel



data =pd.read_csv('1.csv')

def KNeighbors():
    tdf= pd.DataFrame()

    tdf['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 'Buy', 'Sell')
    
    # 根据需求处理第一个时间点的情况，这里假设默认为 'Sell'
    tdf.loc[0, 'Target'] = 'Sell'

    x = data.iloc[:, 1:-1].values  # 假設需要排除第一列（日期）和最後兩列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4,random_state=39830)

    # 使用 KNeighborsClassifier 進行訓練和評分
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(x_train, y_train)
    score = knn.score(x_test, y_test)
    print(f"knn 最佳準確率: {score}")

def GridSearch():
    tdf= pd.DataFrame()

    tdf['Target'] = np.where(data['Close'].diff() > 0, 'Buy', 'Sell')

    x = data.iloc[:, 1:-1].values  # 假設需要排除第一列（日期）和最後兩列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量

    x_train , x_test , y_train , y_test = train_test_split(
    x,y, test_size=0.4,random_state=39830)
    param = {'n_neighbors':[3,5,8,10],
            'weights':['uniform','distance']}
    knn = KNeighborsClassifier()
    gc = GridSearchCV(knn, param_grid=param, cv=5)
    gc.fit(x_train,y_train)
    print('網格 最佳準確率：')
    print(gc.best_score_)
    print('網格 最佳參數組合：')
    print(gc.best_estimator_)

def Decision_tree(random_state):
    
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    f = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    x = data[f].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=random_state)

    dec = DecisionTreeRegressor(random_state=random_state)
    dec.fit(x_train, y_train)

    # 在测试集上评估模型
    y_pred = dec.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Decision_tree 均方誤差: {mse}")
    print(f"Decision_tree R^2 分數: {r2}")

    return mse, r2

def Decision_tree_graph():
    features = ['High','Low','Open','Adj Close','EMA12']
    X = data[features]

    tdf= pd.DataFrame()
    tdf['Target'] =data['Close']
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量
    
    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(X, y)
    tree.plot_tree(classifier)
    plt.show()

def Linear_regression():
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    f =['Open','High','Low','Adj Close','EMA12']
    x = data[f].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x = data.iloc[:, 1:-1].values  # 假設需要排除第一列（日期）和最後兩列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4,random_state=39830)
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    print('權重值：{}'.format(lr.coef_))
    print('偏置值：{}'.format(lr.intercept_))

    y_predict = std_y.inverse_transform(lr.predict(x_test))
    y_real = std_y.inverse_transform(y_test)
    for i in range(50):
        print('預測值：{}，真實值：{}'.format(y_predict[i], y_real[i]))

    merror = mean_squared_error(y_real, y_predict)
    print('平均方差：{}'.format(merror))

    x_last_predict = x[-10].reshape(1, -1)
    
    y_last_predict = std_y.inverse_transform(lr.predict(std_x.transform(x_last_predict)))
    print('預測值：', y_last_predict[0].round(4))
    print(type(x_last_predict))

def DR_Linear_regression():
    tdf= pd.DataFrame()

    tdf['Target'] = data['Close']

    f =['Open','High','Low','Adj Close','EMA12']
    x = data[f].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4,random_state=39830)
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))
    sgd = SGDRegressor()
    sgd.fit(x_train, y_train)
    print('權重值：{}'.format(sgd.coef_))
    print('偏置值：{}'.format(sgd.intercept_))
    y_predict = std_y.inverse_transform(sgd.predict(x_test).reshape(-1, 1))
    y_real = std_y.inverse_transform(y_test)
    for i in range(20):
        print('DR_預測值：{}，DR_真實值：{}'.format(y_predict[i], y_real[i]))
    merror = mean_squared_error(y_real, y_predict)
    print('DR_平均方差：{}'.format(merror))

def Logisticregression():
    tdf= pd.DataFrame()

    tdf['Target'] = np.where(data['Close'].diff() > 0, 'Buy', 'Sell')

    x = data.iloc[:, 1:-1].values  # 假設需要排除第一列（日期）和最後兩列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4,random_state=39830)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    score = estimator.score(x_test, y_test)
    print("Logistic 準確率：{}".format(score))

def classificationreport():
    tdf = pd.DataFrame()
    tdf['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 'Buy', 'Sell')
    
    # 根据需求处理第一个时间点的情况，这里假设默认为 'Sell'
    tdf.loc[0, 'Target'] = 'Sell'

    x = data.iloc[:, 1:-1].values  # 假設需要排除第一列（日期）和最後兩列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作為目標變量

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=39830)

    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    y_pre = estimator.predict(x_test)

    le = LabelEncoder()
    y_test = le.fit_transform(y_test)
    y_pre = le.fit_transform(y_pre)

    ret = classification_report(y_test, y_pre, labels=(0, 1),
                                target_names=("買", "賣"), zero_division=0)
    print(ret)

def svc():
    tdf = pd.DataFrame()
    tdf['Target'] = np.where(data['Close'].diff() > 0, 'Buy', 'Sell')

    f =['Open','High','Low','Adj Close','EMA12']
    x = data[f].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4,random_state=39830)
    clf = SVC(kernel='linear', gamma='scale', C=1, degree=3)
    clf.fit(x_train,y_train)
    score = clf.score(x_test, y_test)
    print("準確率：{}".format(score))

def svcandpca():
    tdf = pd.DataFrame()
    tdf['Target'] = np.where(data['Close'].diff() > 0, 'Buy', 'Sell')

    features = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    x = data[features].values
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=39830)

    pca = PCA(svd_solver='randomized', n_components=5, whiten=True)
    pca.fit(x_train)
    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)

    clf = SVC(kernel='rbf', C=100, gamma='auto')
    clf.fit(x_train_pca, y_train)

    score = clf.score(x_test_pca, y_test)
    print("準確率：{}".format(score))

    predictions = clf.predict(x_test_pca)
    for i in range(20):
        print('預測值：{}，真實值：{}'.format(predictions[i], y_test[i]))

def svr_and_pca():
    print(data)
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    features = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    # x = data.iloc[:, 1:-1].values
    x = data[features].values
    # feature_data = data.iloc[:, 1:-1]
    feature_data=data[features]
    feature_names = feature_data.columns
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=39830)

    pca = PCA(svd_solver='randomized', n_components=5, whiten=True)
    pca.fit(x_train)
    
    print('主成分:')
    print(pca.components_)

    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)

    svr = SVR(kernel='rbf', C=100, gamma='auto')
    svr.fit(x_train_pca, y_train)

    score = svr.score(x_test_pca, y_test)
    print("R-squared score:", score)

    predictions = svr.predict(x_test_pca)

    merror = mean_squared_error(y_test, predictions)
    print('平均方差：{}'.format(merror))

    # 计算均方根误差
    rmse = np.sqrt(merror)
    print('均方根误差 (RMSE): {}'.format(rmse))

    # 计算平均绝对误差
    mae = mean_absolute_error(y_test, predictions)
    print('平均绝对误差 (MAE): {}'.format(mae))

    # 计算 R-squared score 使用 r2_score
    r2 = r2_score(y_test, predictions)
    print("R-squared score (使用 r2_score):", r2)

    tolerance_percentage = 0.03  # 5%

    # 计算容忍度阈值
    tolerance_threshold = tolerance_percentage * np.abs(y_test)

    # 计算绝对误差
    absolute_errors = np.abs(predictions - y_test)

    # 计算在容忍度范围内的正确比率
    correct_within_tolerance = np.mean(absolute_errors <= tolerance_threshold)

    # 输出正确比率
    print(f'在容忍度 {tolerance_percentage*100}% 范围内的正确比率: {correct_within_tolerance:.2f}%')

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, color='blue', label='Predicted vs Actual')
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='45 Degree Line')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Scatter Plot of Predicted vs Actual Values')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 建立主成分與特徵的 DataFrame
    components_df = pd.DataFrame(pca.components_, columns=feature_names, index=[f'主成分 {i+1}' for i in range(pca.n_components_)])
    
    # 顯示每個主成分的最重要特徵
    for i in range(pca.n_components_):  # PCA 中的主成分數量
        print(f'\n主成分 {i+1} 的最重要特徵:')
        top_features = components_df.loc[f'主成分 {i+1}'].abs().sort_values(ascending=False)
        print(top_features.head(5))  # 顯示影響最大的兩個特徵

def svr_and_pca_with_cv():
    tdf = pd.DataFrame()
    tdf['Target'] = data['CloseY']

    x = data.iloc[:, 1:-1].values
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=39830)

    best_n_components = 0
    best_score = -float('inf')
    best_predictions = None
    best_top_features = None

    for i in range(1, x.shape[1] + 1):
        pca = PCA(svd_solver='randomized', n_components=i, whiten=True)
        pca.fit(x_train)
        
        x_train_pca = pca.transform(x_train)
        x_test_pca = pca.transform(x_test)

        svr = SVR(kernel='rbf', C=100, gamma='auto')
        
        # 使用交叉驗證來評估模型性能
        scores = cross_val_score(svr, x_train_pca, y_train, cv=5, scoring='r2')
        score = np.mean(scores)
        
        print(f"For {i} components, Cross-validated R-squared score: {score}")

        if score > best_score:
            best_score = score
            best_n_components = i
            
            # 在找到最佳成分數後，使用整個訓練集重新訓練模型
            svr.fit(x_train_pca, y_train)
            best_predictions = svr.predict(x_test_pca)

            # Get the top features for the best component
            best_pca = PCA(svd_solver='randomized', n_components=i, whiten=True)
            best_pca.fit(x_train)
            best_components = best_pca.components_
            top_features_indices = np.argsort(np.abs(best_components[-1]))[::-1][:best_n_components]
            
            # Map indices to original feature names
            best_top_features = data.columns[1:-1][top_features_indices].tolist()
    
    print(f"Best Cross-validated R-squared score: {best_score} with {best_n_components} components")
    print(f"Top features: {best_top_features}")

    # Calculate mean squared error for best predictions
    merror = mean_squared_error(y_test, best_predictions)
    print('平均方差：{}'.format(merror))

    # Retrain SVR on full training set with best PCA components
    svr = SVR(kernel='rbf', C=100, gamma='auto')
    pca = PCA(svd_solver='randomized', n_components=best_n_components, whiten=True)
    x_train_pca = pca.fit_transform(x_train)
    svr.fit(x_train_pca, y_train)

    # Transform test data for prediction
    x_test_pca = pca.transform(x_test)
    y_pred = svr.predict(x_test_pca)

    # Plotting PCA components with SVR regression line
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(x_train_pca[:, 0], x_train_pca[:, 1], c=y_train, cmap='viridis', label='Data points')
    plt.title('Scatter Plot of PCA Components')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')

    plt.colorbar(scatter, label='Target')
    plt.legend()
    plt.grid(True)
    plt.show()


def svm():
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    f =['Open','High','Low','Adj Close','EMA12']
    x = data[f].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.4,random_state=39830)
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))
    y_test = std_y.transform(y_test.reshape(-1, 1))
    clf = SVR(kernel='rbf', C=1, gamma='auto')
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    y_predict = std_y.inverse_transform(y_predict.reshape(-1, 1))
    y_real = std_y.inverse_transform(y_test)
    for i in range(min(20, len(y_predict))):  # 打印前20个元素或者数组的长度，取两者中较小的值
        print('預測值：{}，真實值：{}'.format(y_predict[i][0], y_real[i][0]))
    merror = mean_squared_error(y_real, y_predict)
    print('平均方差：{}'.format(merror))

def pca_feature_selection():
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    # features = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    features=data.columns[1:-1]
    x = data[features].values
    
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=39830)

    best_n_components = 0
    best_score = -float('inf')
    best_top_features = None
    best_pca = None

    print("Feature matrix (x):")
    print(x)
    
    for i in range(1, x.shape[1] + 1):
        pca = PCA(n_components=i, whiten=True)
        pca.fit(x_train)
        
        # Calculate some score metric (e.g., explained variance ratio)
        score = np.sum(pca.explained_variance_ratio_[:i])
        
        # Get the top features for the current number of components
        # Summarize the loadings of the components
        components = pca.components_
        feature_loadings = np.abs(components).mean(axis=0)
        top_features_indices = np.argsort(feature_loadings)[::-1][:i]
        top_features = [features[idx] for idx in top_features_indices]
        
        print(f"For {i} components, Explained variance ratio: {score}")
        print(f"Top features for {i} components: {top_features}")

        if score > best_score:
            best_score = score
            best_n_components = i
            best_top_features = top_features
            best_pca = pca
    
    print(f"Best Explained variance ratio: {best_score} with {best_n_components} components")
    print(f"Top features: {best_top_features}")

    return best_top_features, best_pca

def svr():
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    features,pca=pca_feature_selection()

    # features = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    x = data[features].values
    # x = data.iloc[:, 1:-1].values
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=39830)

    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)

    svr = SVR(kernel='rbf', C=100, gamma='scale')
    svr.fit(x_train_pca, y_train)

    score = svr.score(x_test_pca, y_test)
    print("R-squared score:", score)

    predictions = svr.predict(x_test_pca)
    # for i in range(20):
    #     print('Predicted value: {}, True value: {}'.format(predictions[i], y_test[i]))

    merror = mean_squared_error(y_test, predictions)
    print('平均方差：{}'.format(merror))

def svr_and_pca2():
    print(data)
    tdf = pd.DataFrame()
    tdf['Target'] = data['Close']

    # features = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    features=['Low', 'Open', 'High', 'EMA26', 'Adj Close', 'rsi', 'Signal_Line', 'upperband', 'lowerband', 'MACD', 'EMA12']
    # x = data.iloc[:, 1:-1].values
    x = data[features].values
    # feature_data = data.iloc[:, 1:-1]
    feature_data=data[features]
    feature_names = feature_data.columns
    y = tdf['Target'].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=39830)

    pca = PCA(svd_solver='randomized', n_components=3, whiten=True)
    pca.fit(x_train)
    
    print('主成分:')
    print(pca.components_)

    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)

    svr = SVR(kernel='rbf', C=100, gamma='auto')
    svr.fit(x_train_pca, y_train)

    score = svr.score(x_test_pca, y_test)
    print("R-squared score:", score)

    predictions = svr.predict(x_test_pca)

    merror = mean_squared_error(y_test, predictions)
    print('平均方差：{}'.format(merror))

    # 计算均方根误差
    rmse = np.sqrt(merror)
    print('均方根误差 (RMSE): {}'.format(rmse))

    # 计算平均绝对误差
    mae = mean_absolute_error(y_test, predictions)
    print('平均绝对误差 (MAE): {}'.format(mae))

    # 计算 R-squared score 使用 r2_score
    r2 = r2_score(y_test, predictions)
    print("R-squared score (使用 r2_score):", r2)

    tolerance_percentage = 0.01  # 5%

    # 计算容忍度阈值
    tolerance_threshold = tolerance_percentage * np.abs(y_test)

    # 计算绝对误差
    absolute_errors = np.abs(predictions - y_test)

    # 计算在容忍度范围内的正确比率
    correct_within_tolerance = np.mean(absolute_errors <= tolerance_threshold)

    # 输出正确比率
    print(f'在容忍度 {tolerance_percentage*100}% 范围内的正确比率: {correct_within_tolerance:.2f}%')


def Decision_tree_Classifier():
    
    tdf = pd.DataFrame()
    tdf['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 'Buy', 'Sell')
    feature = ['Open', 'High', 'Low', 'Adj Close', 'EMA12']
    x = data[feature].values  # 排除第一列（日期）和最后两列（Target和Close）
    y = tdf['Target'].values  # 使用 'Target' 作为目标变量

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=39830)

    dec = DecisionTreeClassifier(random_state=39830)
    dec.fit(x_train, y_train)

    x_last_predict = data.iloc[-1][feature].values.reshape(1, -1)
    y_model_pred = dec.predict(x_last_predict)
    score = dec.score(x_test, y_test)
    y_pred=dec.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    conf_matrix = confusion_matrix(y_test, y_pred, labels=dec.classes_)
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Reds', xticklabels=dec.classes_, yticklabels=dec.classes_)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # 计算准确率
    accuracy = accuracy_score(y_test, y_pred)
    # 计算精确率
    precision = precision_score(y_test, y_pred, average='weighted', labels=dec.classes_)
    # 计算召回率
    recall = recall_score(y_test, y_pred, average='weighted', labels=dec.classes_)
    # 计算 F1 分数
    f1 = f1_score(y_test, y_pred, average='weighted', labels=dec.classes_)

    print(score)
    print(accuracy)

    return score,y_model_pred[0],f1

# pca_feature_selection()
# KNeighbors()
# GridSearch()
# Decision_tree(39830)
# Linear_regression()
# pca_feature_selection()
# DR_Linear_regression()
# Logisticregression()
# classificationreport()
# svc()
# svcandpca()
svr_and_pca2()
# svr_and_pca_with_cv()
# svm()
# svr()
# pca_feature_analysis()
# Decision_tree_Classifier()

# best_score = -1
# best_random_state = None

# for random_state in range(100000):  # 尝试多个随机种子
#     score = Decision_tree(random_state)
#     if score > best_score:
#         best_score = score
#         best_random_state = random_state

# print(f'在 random_state={best_random_state} 下的最佳准确率为: {best_score:.4f}')

# Decision_tree_graph()