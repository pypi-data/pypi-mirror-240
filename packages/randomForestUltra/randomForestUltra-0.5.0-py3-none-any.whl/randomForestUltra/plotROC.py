
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Set up a non-interactive backend !
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc, accuracy_score

def createLongPath(target_path):
    def create_directory(path):
        try:
            os.makedirs(path)
            print("Directory created: ", path)

        except FileExistsError:
            # print("Directory already exists: ", path)
            pass
    target_dir = os.path.split(target_path)[0]
    path_parts = []
    folder = 'test'
    while folder != '':
        target_dir, folder = os.path.split(target_dir)
        if folder != '':
            path_parts.insert(0, folder)
            # print(path_parts)
    for part in path_parts:
        current_path = os.path.join(target_dir, part)
        target_dir = current_path
        # print(current_path)
        create_directory(current_path)

class resultsForROC:
    def __init__(self):
        self.tprs = []
        self.aucs = []
        # self.importances = []
        self.acc = []
        # self.matthews = []
        self.shuffled_acc = []
        self.shuffled_aucs = []
        self.shuffled_tprs = []
        self.mean_fpr = np.linspace(0, 1, 101)
        self.p_val = 0.99

def empiricalPVal(statistic, null_dist):
    ###number of shuffled iterations where performance is >= standard iteration performance
    count = len([val for val in null_dist if val >= statistic])
    p_val = (count + 1 ) /float(len(null_dist) + 1)
    return p_val



def plotROC(target, outPath, title, y_pred, y_true, y_pred_shuffled, y_true_shuffled):
    # 定义阈值
    threshold = 0.5
    dataROC = resultsForROC()
    for i in range(y_pred.shape[0]):
        i_pred = y_pred.iloc[i]
        i_true = y_true.iloc[i]
        i_pred_class = np.where(i_pred > threshold, 1, 0)
        fpr, tpr, _ = roc_curve(i_true, i_pred)
        roc_auc = auc(fpr, tpr)
        acc = accuracy_score(i_true, i_pred_class)

        # dataROC = resultsForROC()
        dataROC.tprs.append(np.interp(dataROC.mean_fpr, fpr, tpr))
        dataROC.tprs[-1][0] = 0.0
        dataROC.aucs.append(roc_auc)
        dataROC.acc.append(acc)

        i_pred = y_pred_shuffled.iloc[i]
        i_true = y_true_shuffled.iloc[i]
        i_pred_class = np.where(i_pred > threshold, 1, 0)
        fpr, tpr, _ = roc_curve(i_true, i_pred)
        roc_auc = auc(fpr, tpr)
        acc = accuracy_score(i_true, i_pred_class)

        dataROC.shuffled_tprs.append(np.interp(dataROC.mean_fpr, fpr, tpr))
        dataROC.shuffled_tprs[-1][0] = 0.0
        dataROC.shuffled_aucs.append(roc_auc)
        dataROC.shuffled_acc.append(acc)

    dataROC.p_val = np.mean([empiricalPVal(stat, dataROC.shuffled_aucs) for stat in dataROC.aucs])


    # print('-----------------------------')
    plt.figure(1, figsize=(6, 6))
    plt.plot([-0.05, 1.05], [-0.05, 1.05], linestyle=':', lw=2, color='k', alpha=.8)
    ##TEST ROC CURVE
    mean_tpr = np.mean(dataROC.tprs, axis=0)
    mean_tpr[-1] = 1.0
    std_tpr = np.std(dataROC.tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    mean_auc = auc(dataROC.mean_fpr, mean_tpr)
    std_auc = np.std(dataROC.aucs)
    # plt.plot(dataROC.mean_fpr, mean_tpr, color='b', label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
    #          lw=2, alpha=0.9)
    plt.plot(dataROC.mean_fpr, mean_tpr, color='b', label=r'Mean ROC (AUC=%0.3f$\pm$%0.3f,P=%0.3f)' % (mean_auc, std_auc, dataROC.p_val),
             lw=2, alpha=0.9)
    plt.fill_between(dataROC.mean_fpr, tprs_lower, tprs_upper, color='b', alpha=.3, label=r'$\pm$ 1 std. dev.')
    ##SHUFFLED ROC CURVE
    shuffled_mean_tpr = np.mean(dataROC.shuffled_tprs, axis=0)
    shuffled_mean_tpr[-1] = 1.0
    std_tpr = np.std(dataROC.shuffled_tprs, axis=0)
    shuffled_tprs_upper = np.minimum(shuffled_mean_tpr + std_tpr, 1)
    shuffled_tprs_lower = np.maximum(shuffled_mean_tpr - std_tpr, 0)
    shuffled_mean_auc = auc(dataROC.mean_fpr, shuffled_mean_tpr)
    shuffled_std_auc = np.std(dataROC.shuffled_aucs)
    plt.plot(dataROC.mean_fpr, shuffled_mean_tpr, color='r',
             label=r'Mean Shuffled-ROC (AUC=%0.3f$\pm$%0.3f)' % (shuffled_mean_auc, shuffled_std_auc), lw=2, alpha=0.9)
    plt.fill_between(dataROC.mean_fpr, shuffled_tprs_lower, shuffled_tprs_upper, color='r', alpha=.3, label=r'$\pm$ 1 std. dev.')
    # plt.annotate(f'p_val = {dataROC.p_val:.3f}', xy=(0.5, 0.1), xycoords='axes fraction', fontsize=12,
    #              ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")

    pngPath = os.path.join(outPath, f'RF_ROCs_{target}.png')
    # createLongPath(pngPath)
    plt.savefig(pngPath, format='png', dpi=300)
    pdfPath = os.path.join(outPath, f'RF_ROCs_{target}.pdf')
    plt.savefig(pdfPath, format='pdf', dpi=300)
    # plt.show()
    plt.close()

    # 保存 dataROC 中的数据
    pathAUC = os.path.join(outPath, f'RF_AUC_{target}.csv')
    AUCs = pd.DataFrame(dataROC.aucs)
    AUCs.columns = [target]
    AUCs = AUCs.T
    AUCs.to_csv(pathAUC)

    pathResult = os.path.join(outPath, f'RF_result_{target}.csv')
    auc_q1 = np.percentile(dataROC.aucs, 25)
    auc_q2 = np.percentile(dataROC.aucs, 50)
    auc_q3 = np.percentile(dataROC.aucs, 75)

    shuffled_auc_q1 = np.percentile(dataROC.shuffled_aucs, 25)
    shuffled_auc_q2 = np.percentile(dataROC.shuffled_aucs, 50)
    shuffled_auc_q3 = np.percentile(dataROC.shuffled_aucs, 75)

    acc_mean = np.mean(dataROC.acc, axis=0)
    acc_std = np.std(dataROC.acc, axis=0)
    shuffled_acc_mean = np.mean(dataROC.shuffled_acc, axis=0)
    shuffled_acc_std = np.std(dataROC.shuffled_acc, axis=0)

    # 创建一个空的数据框
    rfResult = pd.DataFrame()
    # 添加一行数据
    new_row = {'p_val': dataROC.p_val, 'auc_mean': mean_auc, 'auc_std': std_auc,
               'auc_q1': auc_q1, 'auc_q2': auc_q2, 'auc_q3': auc_q3,
               'shuffled_auc_mean': shuffled_mean_auc, 'shuffled_auc_std': shuffled_std_auc,
               'shuffled_auc_q1': shuffled_auc_q1, 'shuffled_auc_q2': shuffled_auc_q2, 'shuffled_auc_q3': shuffled_auc_q3,
               'acc_mean': acc_mean, 'acc_std': acc_std,
               'shuffled_acc_mean': shuffled_acc_mean, 'shuffled_acc_std': shuffled_acc_std}
    rfResult = pd.DataFrame(new_row, index=[0])
    rfResult.set_index(pd.Index([target]), inplace=True)
    rfResult.to_csv(pathResult)


if __name__ == "__main__":
    dataPath = 'D:/BGI/27.MSN/RFUltra/'
    Y_df = pd.read_csv(os.path.join(dataPath, 'data/Y.csv'), index_col=0)
    target_list = list(Y_df.columns)  # 选择有结果的 target 变量
    target_info = pd.read_csv(os.path.join(dataPath, 'data/y_info.csv'), index_col=0)
    for i in range(len(target_list)):
        target = target_list[i]
        pathModelOutput = os.path.join(dataPath, f'result/s_all/ModelOutput/{target}/')
        print(f'{i + 1}, {target}, {pathModelOutput}')
        # 读取数据
        y_pred = pd.read_csv(os.path.join(pathModelOutput, 'y_pred.csv'), index_col=None, header=None)
        y_true = pd.read_csv(os.path.join(pathModelOutput, 'y_true.csv'), index_col=None, header=None)
        y_pred_shuffled = pd.read_csv(os.path.join(pathModelOutput, 'y_pred_shuffled.csv'), index_col=None, header=None)
        y_true_shuffled = pd.read_csv(os.path.join(pathModelOutput, 'y_true_shuffled.csv'), index_col=None, header=None)
        if y_true.isnull().values.any():
            # 有些样本有问题，用0值填充
            print(f'Please pay attention to the real label of {target} !')
            y_true = y_true.fillna(0)
            y_pred = y_pred.fillna(0)
            y_pred_shuffled = y_pred_shuffled.fillna(0)
            y_true_shuffled = y_true_shuffled.fillna(0)

        outPath = os.path.join(dataPath, 'result/s_all/ROCs/')
        createLongPath(outPath)
        title = "Classification of " + target_info.loc[target, "plot_name"]
        plotROC(target, outPath, title, y_pred, y_true, y_pred_shuffled, y_true_shuffled)
