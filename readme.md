<!DOCTYPE html>

<html lang="en">  
<head>  
 <meta charset="UTF-8">  
 <title>Title</title>  
</head>  
<body>

#About  
課題として作成した家計簿アプリです。一時的に一般公開しています。  

開発言語・フレームワーク　-Python3 Django2 Bootstrap4  
デプロイ環境　-AWS EC2  

リンク  
課題用Webアプリ[http://18.191.24.11/accounts/login/](http://18.191.24.11/accounts/login/)

kakeibo/kakeibo_tutoにアプリケーション構成ファイルがあります。  

### データテーブルについて

'suitoh'(models.Suitoh)  
構成カラム 

| data(日付)   | cat(カテゴリ) | out-cost(金額) | meimoku(名目) | rank（重要度 |
| ---------- | --------- | ------------ | ----------- | -------- |
| yyyy/mm/dd | touple    | 整数値          | 入力          | 高/中/低    |

    重要度

日付,カテゴリ,金額,名目,重要度  

<font color="Black">

> ＊cat,rankはそれぞれ`models.Ranks(高/中/低)`,`models.Category`で定義されています。  
> 
> メインページ（/kakeibo_tuto/Suitoh_list/）に(views.SuitohListView)一覧表示されるようなっており、Listviewによって表示されています。  
> データフレームで定義された5カラムの他に、修正・削除ボタン(後述)が実装されています。 

</font>

### 機能一覧

`/views.py`内にclassまたは関数として定義されています。  
Webページ上のリンクは/urls.py内の `urlpatterns`内で定義されています。  
例えば、出納表一覧(SuitohListView)は  
`path('Suitoh_list/', views.SuitohListView.as_view(), name='Suitoh_list')`  
と定義されており、  
/kakeibo_tuto/Suitoh_listでアクセスできます。  

各機能に対応するページ(テンプレート)はファイル内/templates/kakeibo_tuto内にあります。  
いずれもbase.htmlをテンプレートとして利用しており、bootstrap4によって作成されています。  

例えば/Suitoh_listにアクセスするとSuitoh_list.htmlが表示されるとともに  
/views.py内で定義されたSuitohListViewが呼び出され、実行結果をreturnでSuitoh_list.htmlに渡します。  

殆どの機能はDjango汎用ビューにを使っています。  

> 各機能表記凡例
> 
> 機能名（views.関数/class名,templates/kakeibo_tuto/htmlファイル）  

#### 開発用県内の最低要件に関する機能

 すべてmodels.Suitohモデルで定義されたデータテーブルとして利用し、Djangoの汎用ビューを用いて作成されています。

##### 出納表一覧(SuitohListView,Suitoh_list.html)   ページ内path:/Suitoh_list

> **出納表カード**  
> 汎用ビューであるListViewを利用しています。  
> db.sqlite3内に登録されているデータを一覧表示します。  
> Suitoh_list.html内  で定義されており、カラム名のあとに。  
> `SuitohListView`で出納表の全件データを取得してobject_listに渡しています。  
> これをSuitoh_list.html内の  
> `{% for item in object_list %}`によって、すべてのデータを一行ずつ表示しています。  
> 
> また更新・削除ボタンを各行ごとにもちます。  
> 
> base.html内の `jQuery(function($){}`によってデータテーブルの検索、ページング、ソート、件数切り替えの機能を有効にしています。  
> 
> **機能カード**  
> 他の機能へのリンクボタンが配置されています。  

#### 

#### 新規登録(SuitohCreateView,Suitoh_form.html)   ページ内path:/Suitoh_create

> Suitoh_list.html内の追加ボタンからアクセスできます。  
> 
> 汎用ビューであるCreateViewをりようしています。   html内の{{ form|bootstrap }}がメインフォームです、データテーブルに対応した項目を入力できます。   `|bootstrap`によってスタイルを調整しています.
> 
> kakeibo/db.sqlite3内のSuitohデータテーブルに追加されます。  
> 
> 登録完了後のurlは`views.SuitohCreateView`内の  
> `success_url = reverse_lazy('kakeibo_tuto:create_done') ` 
> によって定義されており  
> create_done.htmlを呼び出します。  

#### 更新・更新完了(SuitohUpdateView,update_done)   ページ内path:/update/<pk>

> Suitoh_list.html内の更新ボタンからアクセスできます。   汎用ビューであるUpdateViewを利用しています。   新規登録と同じSuitoh_formを利用します。   更新ボタンが押されると対応するデータのプライマリキーPKが渡され、Suitoh_formに反映されます。  
> 
> 更新完了後のurlは`views.SuitohCreateView`内の  
> `success_url = reverse_lazy('kakeibo_tuto:create_done') ` 
> によって定義されており  
> create_done.htmlを呼び出します。  

削除・削除完了(SuitohDeleteView.delete_done)  
ページ内path:/update/<pk>  
Suitoh_list.html内の更新ボタンからアクセスできます。  
汎用ビューであるUpdateViewをりようしています。  
新規登録と同じSuitoh_formを利用します。  
更新ボタンが押されると対応するデータのプライマリキーPKが渡され、Suitoh_formに反映されます。  

更新完了後のurlはviews.SuitohCreateView内の  
success_url = reverse_lazy('kakeibo_tuto:create_done')  
によって定義されており  
create_done.htmlを呼び出します。  

種類ごと合計(Sumbycat,Submycat.html)  
出納表のカテゴリごとの金額を表示します。  

コード説明  
    def Sumbycat(request):  
    s_data =Suitoh.objects.all()　でSuitohデータテーブルの全件を取得します  

    total = 0  
    for item in s_data:  
        total += item.out_cost　  
    
    ここで取得した全データをforで回し、データテーブルのitem.out_costカラムの合計をtotalに代入します  
    
    
    category_list = []  
    category_data = Category.objects.all()  
    
    for item in category_data:  
        category_list.append(item.category_name)  
    dict = {}  
    for i, item in enumerate(category_list):  
        category_total = Suitoh.objects.filter(cat__category_name=category_list[i]).aggregate(sum=models.Sum('out_cost'))['sum']  
        if category_total != None:  
            a = {'total':category_total, 'ratio': round((category_total/total)*100, 2)}  
            dict[item]= a  
        else:  
            a = {'total': 0, 'ratio': 0}  
            dict[item] = a  
    
    
    
    con = {'dict': dict}  
    
    return render(request, 'kakeibo_tuto/Sumbycat.html', con)  

</body>  
</html>
