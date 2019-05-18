# _*_coding:utf-8_*_
__author__ = 'mcy'
__date__ = '2019-05-15 12:10'

import time
from functions import *
from netlaprls1_0rev import NetLapRLS
import pickle

# TODO xyz  y -- 10-5 10-3 10
# TODO beta_d beta_t 生成矩阵 可视化图
# TODO 平均的auc 和 aupr值
# TODO 模型预测 将出现的作用对 标记


def netlaprls_cv_eval(method, dataset, cv_data, X, D, T, cvs, para):
    max_aupr = 0
    prime_beta_t = 0
    prime_beta_d = 0
    for x in np.logspace(-6, 3, 10):  # [-6, 2]
        for y in np.logspace(-6, 3, 10):  # [-6, 2]
            tic = time.clock()
            model = NetLapRLS(beta_d=x, beta_t=y)
            cmd = "Dataset:"+dataset+" CVS: "+str(cvs)+"\n"+str(model)
            print cmd
            aupr_vec, auc_vec = train(model, cv_data, X, D, T)
            aupr_avg, aupr_conf = mean_confidence_interval(aupr_vec)
            auc_avg, auc_conf = mean_confidence_interval(auc_vec)
            print "auc : %.6f, aupr : %.6f, auc_conf : %.6f, aupr_conf : %.6f, Time : %.6f \n" % (auc_avg, aupr_avg, auc_conf, aupr_conf, time.clock()-tic)
            if aupr_avg > max_aupr:
                max_aupr = aupr_avg
                prime_beta_d = x
                prime_beta_t = y
    print 'Best beta_d: %f, beta_t: %f.' % (prime_beta_d, prime_beta_t)