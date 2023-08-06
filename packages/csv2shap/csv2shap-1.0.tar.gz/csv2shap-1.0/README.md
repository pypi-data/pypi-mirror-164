# 输入csv文件的路径于引号中，可command+空格键打开聚焦搜索，输入terminal打开终端，
# 将需输入的csv文件拖入终端，即可显示文件路径
file_path = ''
# 在中括号中输入想要删除的特征名，如用户ID，与label强相关的同类特征，需加双引号，
# 特征名之间加逗号（均为英文输入法下的符号）如"user_id","days_active_in_l7d"
del_cols = []
# 输入需要预测的变量名于引号中，即label名，需要为二分类变量，即取值为0或1 
label_feature = ''
# 输入变量中英文对应的csv文件路径于引号中，csv文件格式：第一行为name_en,name_cn
# 其余各行格式为 特征英文名,特征中文名 ；目的是输出的特征重要性图中特征名为中文，
# 如不需要可在文件中只写入第一行，即name_en,name_cn
feature_name_file_path = ''
# 可以不修改，表示html文件输出路径
root = '/Users/user/Desktop/'
# 可以不修改，表示输出html文件名
jpg_name = 'shap_value'
# 无需修改
main(file_path, del_cols, label_feature, feature_name_file_path, root, jpg_name)