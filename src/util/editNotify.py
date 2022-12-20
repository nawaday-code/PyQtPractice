
"""
デコレータで
編集宣言
編集終了

難しいのは、いつ変更をmodelに影響させるか
他プログラムでは、
Df編集
dataに編集後のDfを格納
modelにdataを格納<-ここに関数をはさむか

@編集適用デコレータ
データ変更受付関数(view, index, 変更値):
    viewでselectしているindexを受け取り、それを送信したDfのindexとする

    dataに変更部分を適用

    modelにセットされているデータ(Df)のindexを指定して変更

@編集適用デコレータ
データ変更受付関数＿簡易版(変更後Df)
    送信したDfと変更後Dfを比較 変更部分を抽出 <-重いかも
        pandas index = dataframe.compare(dataframe)でいけそう

    dataに変更部分を適用

    modelにセットされているデータのindexを指定して変更
    (比較抽出した変更部分のindexのみDfを変更する)

"""