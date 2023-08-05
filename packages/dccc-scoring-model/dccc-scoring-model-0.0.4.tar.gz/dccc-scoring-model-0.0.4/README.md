w1: 規劃 project structure by DMLM
w2: 分段寫CODE
w3: tox, pytest
w4: pydantic, lint 
w5: fast api
w6: heroku
w7: CI
w8: CD

開發順序：
1. train_pipeline.py裡的每個步驟：
* 讀資料
* 資料切割
* 資料前處理(特徵工程)
* 模型建立
* 儲存模型

2. predict.py
* 讀模型
* 資料前處理
* 預測

3. config file + core.py
* app config(應用程式相關)
* model config(模型與特徵相關)

4. data_manager
* 讀資料
* 儲存模型、刪除舊模型、讀取模型

5. validation
* 定義有空值的欄位，非在這些清單內，但有空值的欄位，即有錯誤發生。
* 定義欄位值範圍，若不在定義範圍內，即有錯誤發生。

6. build the package
tox -e train
tox -e test_package
working directory下
python -m pip install --upgrade build
python -m build
上傳package至pypi 

7. api
語法架構
tox -e run測試
logging相關

8. heroku佈署
安裝heroku: heroku --version 確認安裝成功
在工作資料夾下 cli: heroku create 
設定heroku: git subtree push --prefix 資料夾名稱 heroku main




process data:
    rename
    column name lower
    recode 類別型 e.g. pay_0

freature engineering:
	# 數值型
	limit_bal
	age
	bill_amt_1
	pay_amt_1

	# 類別型
	sex
	education
	mariage
	pay_0

	# 次數類
    fullpay_l6m, l3m
    revolve_l6m, l3m
    nobill_l6m, l3m
    default_l6m, l3m
    wstpay_l6m, l3m

    # unpaid amt 類
    unpaid_amt_l6m, l3m, l1m

    # bill amt 類
    sum_bill_amt_l6m, l3m
    avg_bill_amt_l6m, l3m
    std_bill_amt_l6m
    max_bill_amt_l6m, l3m
    min_bill_amt_l6m, l3m
    range_bill_amt_l6m, l3m
    min_bill_amt_f3m
    growingrt_bill_amt

    # pay amt 類
	sum_pay_amt_l6m, l3m
	avg_pay_amt_l6m, l3m
	std_pay_amt_l6m
	max_pay_amt_l6m, l3m
	min_pay_amt_l6m, l3m
	range_pay_amt_l6m, l3m

	# 相除類
	avg_ultrt_l6m, l3m, l1m
	avg_revolve_l6m, l3m, l1m

training:
    data split
    model building
    model training with cv
    save model

predict:
   load model
   feature engineering





