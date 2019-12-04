<!DOCTYPE html>

### About

- アプリケーション名：汎用家計簿

- 開発言語・フレームワーク：Python3 Django2 

- htmlページ作成：bootstrap4

- デプロイ環境　-AWS EC2  +Gunicorn +Nginx(常時ホスト)
  
  ーデプロイは[https://qiita.com/tachibanayu24/items/b8d73cdfd4cbd42c5b1d](https://qiita.com/tachibanayu24/items/b8d73cdfd4cbd42c5b1d)を参考にいたしました。

リンク  
課題用Webアプリ[http://18.191.24.11/accounts/login/](http://18.191.24.11/accounts/login/)

---

### ファイル構成について

以下のような構成になっています

.

├── about.html

├── db.sqlite3

├── kakeibo

│   ├── __init__.py

│   ├── __pycache__

│   │   ├── __init__.cpython-37.pyc

│   │   ├── settings.cpython-37.pyc

│   │   ├── urls.cpython-37.pyc

│   │   └── wsgi.cpython-37.pyc

│   ├── settings.py

│   ├── urls.py #    アプリケーションとURLの関係を指定しています。

│   └── wsgi.py

├── kakeibo_tuto　#今回はこのファイル以下で定義されたアプリケーションを実行しています

│   ├── _ _init__.py

│   ├── _ _pycache__

│   │   ├── __init__.cpython-37.pyc

│   │   ├── admin.cpython-37.pyc

│   │   ├── forms.cpython-37.pyc

│   │   ├── models.cpython-37.pyc

│   │   ├── urls.cpython-37.pyc

│   │   └── views.cpython-37.pyc

│   ├── admin.py

│   ├── apps.py

│   ├── forms.py

│   ├── migrations

│   │   ├── 0001_initial.py

│   │   ├── _ _init__.py

│   │   └── _ _pycache__

│   │    ├── 0001_initial.cpython-37.pyc

│   │    └── __init__.cpython-37.pyc

│   ├── models.py

│   ├── templates　#Webページにアクセスした際に表示されるhtml    テンプレートが入っています

│   │   ├── 404.html

│   │   ├── 500.html

│   │   ├── kakeibo_tuto　

│   │   │   ├── **Suitoh_confirm_delete.html**

│   │   │   ├── **Suitoh_form.html**

│   │   │   ├──**Suitoh_list.html**

│   │   │   ├── **Sumbycat.html**

│   │   │   ├── **base.html**　#エラーページ以外のページの継承元です。

│   │   │   ├── **calen.html**

│   │   │   ├──**create_done.html**

│   │   │   ├── **delete_done.html**

│   │   │   ├──**update_done.html**

│   │   │   └── **randcat.html**

│   │   └── registration

│   │    └── login.html

│   ├── tests.py

│   ├── urls.py

│   └── views.py　#各ページにアクセスした際に実行される関数またはクラスが定義されています。

├── manage.py

└── readme.md #このファイルです。

### データテーブルについて

#### Suitoh（メインデータテーブル）

'Suitoh'(models.Suitoh) と定義されており、db.sqlite3内にあります。 
構成カラム 

| data(日付)   | cat(カテゴリ) | out-cost(金額) | meimoku(名目) | rank（重要度 |
| ---------- | --------- | ------------ | ----------- | -------- |
| yyyy/mm/dd | touple    | 整数値          | 入力          | 高/中/低    |

> ＊cat,rankはそれぞれ`models.Ranks(高/中/低)`,`models.Category`をForeignKeyとして持ちます。
> 
> メインページ（/kakeibo_tuto/Suitoh_list/）に(views.SuitohListView)一覧表示されるようなっており、Listviewによって表示されています。  
> データフレームで定義された5カラムの他に、修正・削除ボタン(後述)が実装されています。 

#### Category

同様にdb.sqlite3内にあり、SuitohのcatカラムのForeignKeyとなっています。

カテゴリが登録されており、adminページから操作が可能です。

#### Ranks

SuitohのrankカラムのForeignKeyとなっています。

データの重要度、高/中/低が登録されており、adminページから操作が可能です。

今回提出する内容では利用しませんでした。支出の重要度別の集計などへの利用を想定しています。

---

### 機能一覧

`kakeibo_tuto/views.py`内にclassまたは関数として定義されています。  
Webページ上のリンクは/urls.py内の `urlpatterns`内で定義されています。  
例えば、出納表一覧(SuitohListView)は  
`path('Suitoh_list/', views.SuitohListView.as_view(), name='Suitoh_list')`  
と定義されており、  
/kakeibo_tuto/Suitoh_listでアクセスできます。  

各機能に対応するページ(テンプレート)はファイル内/templates/kakeibo_tuto内にあります。  
いずれもbase.htmlをテンプレートとして利用しており、bootstrap4によって作成されています。  

例えば/Suitoh_listにアクセスするとSuitoh_list.htmlが表示されるとともに  
/views.py内で定義されたclass SuitohListViewが呼び出され、実行結果をreturnでSuitoh_list.htmlに渡します。  

殆どの機能はDjango汎用ビューにを使っています。  

> 各機能表記例
> 
> 機能名（views.関数/class名,templates/kakeibo_tuto/htmlファイル）  

***

### 開発要件の最低要件に関する機能

 すべてmodels.Suitohモデルで定義されたデータテーブルとして利用し、Djangoの汎用ビューを用いて作成されています。

##### 出納表一覧(SuitohListView,Suitoh_list.html)   ページ内path:/Suitoh_list

> **出納表カード**  
> 汎用ビューであるListViewを利用しています。  
> db.sqlite3内に登録されているデータを一覧表示します。  
> Suitoh_list.html内  で定義されており、カラム名のあとに。  
> `SuitohListView`で出納表の全件データを取得してobject_listに渡しています。  
> これをSuitoh_list.html内の  
> `{% for item in object_list %}`によって、すべてのデータを一行ずつ表示しています。  
> base.html内の `jQuery(function($){}`によってデータテーブルの検索、ページング、ソート、件数切り替えの機能を有効にしています。 

```
jQuery(function($){
      $.extend( $.fn.dataTable.defaults, {
           language: {
              url:"http://cdn.datatables.net/plugins/9dcbecd42ad/i18n/Japanese.json"
             }
              });
       $("#Suitoh").DataTable({
          "searching": true,     //検索機能
           "paging":   true,      //ページング機能
           "ordering": true,      //ソート機能
           "lengthChange": true,  //件数切り替え機能
          }).columns.adjust().draw();
          });
```

> また更新・削除ボタンを各行ごとにもち、それぞれ対応する機能へのリンクボタンです。'

> '<td class="text-center" width="140"><a class="btn btn-primary" href="{%url 'kakeibo_tuto:Suitoh_update' item.pk %}">修正</a></td>
> '<td class="text-center" width="140"><a class="btn btn-danger" href="{% url 'kakeibo_tuto:Suitoh_delete' item.pk %}">削除</a></td>

> href内でリンク先を指定しています。
> `url 'kakeibo_tuto:Suitoh_update'`はkakeibo_tuto/Suitoh_updateへのリンクを表し　`item.pk`で各列に表示されているデータのpkを渡します。

**機能カード**  

> 他の機能へのリンクボタンが配置されています。  
> 
>  '<div class="card-body">
> 以下で定義されています。

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

#### 削除・削除完了(SuitohDeleteView.delete_done)   ページ内path:/update/<pk>

> Suitoh_list.html内の更新ボタンからアクセスできます。   汎用ビューであるUpdateViewをりようしています。   新規登録と同じSuitoh_formを利用します。   更新ボタンが押されると対応するデータのプライマリキーPKが渡され、Suitoh_formに反映されます。  
> 
> 更新完了後のurlはviews.SuitohCreateView内の  
> success_url = reverse_lazy('kakeibo_tuto:create_done')  
> によって定義されており  
> create_done.htmlを呼び出します。  

### 

---

### その他必要だと思った機能

2つのページに渡ります。いずれも汎用ビューなどは使用せずに作成しました。

#### 種類ごと合計(Sumbycat,Submycat.html)

 いくつかの機能を持ちます。それぞれについて    ソースコードと共に説明します。

##### カテゴリごとの支出額合計

家計簿のデータを    カテゴリごとに集計し表と円グラフで表示します。

コード

```python
def Sumbycat(request):
    s_data =Suitoh.objects.all()
    total = 0
    for item in s_data:
        total += item.out_cost
```

一行目でSuitoh    データテーブルの全データを取得します。

for構文を回して    データテーブルの[out_cost]カラムの合計をtotalに入れます。

```python
category_list = []
 category_data = Category.objects.all()
 for item in category_data:
 　category_list.append(item.category_name)
```

次に    Categoryテーブルに保存されているカテゴリをすべて取得します。Suitohの全データを取得したものとほぼ同じです。    カテゴリ名はCategory.categry_nameにあるので

for文で.category_nameをリストに格納しています。
この次にカテゴリごとの合計と円グラフのために割合を求めます。

```python
 dict = {}
    for i, item in enumerate(category_list):
        category_total = Suitoh.objects.filter(cat__category_name=category_list[i]).aggregate(sum=models.Sum('out_cost'))['sum']
        if category_total != None:
            a = {'total':category_total, 'ratio': round((category_total/total)*100, 2)}
            dict[item]= a
        else:
            a = {'total': 0, 'ratio': 0}
            dict[item] = a
```

はじめに

```
for i, item in enumerate(category_list):
        category_total = Suitoh.objects.filter(cat__category_name=category_list[i]).aggregate(sum=models.Sum('out_cost'))['sum']
```

でcategoryすべてをfor文に入れ、各カテゴリ名でフィルタリング`.filter(cat__category_name=category_list[i])`したSuitohデータの金額を合計します。
  次にif文で合計額が０かどうかを確認します。
  もし0(Noneとなります)でなければ`if category_total != None:`、
  辞書aに{total:カテゴリ名の合計金額,ratio:全体合計金額に対する割合％}　の形式で追加します。
  0出会った場合は{total:0,ratio:0}と追加します
 最後にはじめに定義していた辞書dictに`dict[カテゴリ名]={total:カテゴリ名の合計金額,ratio:全体合計金額に対する割合％}`として追加します。
  for文が終了した時点で次のようなデータができていることが期待されます。

```python
  dict = {カテゴリ名:{total:カテゴリ名の合計金額,ratio:全体合計金額に対する割合％},
          カテゴリ名:{total:カテゴリ名の合計金額,ratio:全体合計金額に対する割合％},
          ︙
          }
```

次に月ごとの集計です。基本的にはカテゴリごとの集計と同じです。

```
  date_list = []
    for i in s_data:
        date_list.append((i.data.strftime('%Y/%m/%d')[:7]))


    date_list_s = list(set(date_list))
    date_list_s.sort(reverse=False)
```

はじめにカテゴリごとの合計で利用した`s_data`から、日付を抽出します。
`.strftime('%Y/%m/%d')[:7]`で日付を取り出しています。
それを重複を取り除き`date_list_s = list(set(date_list))`、
昇順でソート`date_list_s.sort(reverse=False)`しています。

```
      for i in date_list_s:
        y,m = i.split("/")
        month_range = calendar.monthrange(int(y), int(m))[1]
        first_date = y + '-' + m +'-' + '01'
        last_date = y + '-' + m + '-' + str(month_range)
        total_of_month = Suitoh.objects.filter(data__range=(first_date, last_date)).aggregate(sum=models.Sum('out_cost'))['sum']
        sumbym ={'y':y,'m':m,'total':total_of_month}
        sumbymonth[i] = sumbym
```

  完成したリストを用いて指定範囲の合計金額をSuitohからもとメルコードです。
  `.filter(data__range=(first_date, last_date))`では、first_date~last_dateのSuitoh列を抽出、`.aggregate(sum=models.Sum('out_cost'))['sum']`で金額の合計を求めています。
  求めた金額は辞書sumbymに`{'y':年,'m':月,'total':対象期間の合計}`の形式で保存し、
  sumbymonth[i] に格納します。
  for文が終わった時点で次のような辞書が完成していることを期待しています。

```
  sumbymonth = {i :{'y':年,'m':月,'total':対象期間の合計},
  i :{'y':年,'m':月,'total':対象期間の合計},
  }
```

  求められたデータは
  `con = {'dict': dict,'sbm':sumbymonth}`の形でSumbycat.htmlに渡されます。

  Sumbycat.htmlでは次のような処理をします。
  円グラフ描画のために事前にbase.htmlに以下のコードを追加しています。

```
   <script>
         var ctx = document.getElementById('CircleChart').getContext('2d');
         var data = [
                     [
                      {% for key, value in dict.items%}
                       '{{key}}',
                      {% endfor %}
                     ],

                     [
                     {% for key, value in dict.items%}
                        {{value.ratio}},
                     {% endfor %}
                     ]]
         var myChart = new Chart(ctx, {
           type: 'pie',

           data: {
             labels: data[0],
             datasets: [{
               data:  data[1],
               backgroundColor: ["rgba(255,241,15,0.8)","rgba(54,164,235,0.8)",
               "rgba(0,255,65,0.8)","rgba(214,216,165,0.8)","rgba(255,94,25,0.8)",
               "rgba(84,77,203,0.8)","rgba(140,140,140,0.8)","rgba(171,255,127,0.8)",
               "rgba(50,204,18,0.8)","rgba(234,210,173,0.8)"],
             },
           ] }
         });
   </script>
```

  関数からreturnされたデータを処理する箇所は

```
   var data = [
                     [
                      {% for key, value in dict.items%}
                       '{{key}}',
                      {% endfor %}
                     ],

                     [
                     {% for key, value in dict.items%}
                        {{value.ratio}},
                     {% endfor %}
                     ]]
```

  です、dictに格納されたカテゴリ名`dict.key`と割合`value.ratio`を別々にfor文で回し、２元配列に格納しています。

  それ以外のコードは色の指定などです。
  `labels: data[0],`でカテゴリ名を取り出し、` data:  data[1],`で値を取り出しています。その円グラフを

```
          <div class="chart_container">
             <canvas id='CircleChart' style="position: relative; height:1vh; width:1vw"></canvas>
           </div> 
```

  で呼び出しています。

一覧表についてはSuitoh_listと同じようにfor文で`dict.key``dict.value.total`をそれぞれ一行ずつ書いています。

##### 月ごとの合計

月ごとの合計は線グラフで描画しました。
  円グラフと同様にbase.htmlで折れ線グラフを定義しておきます。

```
  <script>
  var ctx = document.getElementById("LineChart").getContext('2d');
  var DiskChart = new Chart(ctx, {
  type: 'line',
    data: {
      labels: [
      {% for key ,value in sbm.items %}
        '{{key}}',
      {% endfor %}
      ],
      datasets: [
      {
        label: "月ごと合計",
        fill: false,
        borderColor: 'rgb(254,97,132,0.8)',
        backgroundColor : 'rgb(254,97,132,0.5)',
        data: [
      {% for key ,value in sbm.items %}
        '{{value.total}}',
      {% endfor %}
        ],
      }

    ]
  },
});
```

X軸のデータとして年/月のデータを

```
         {% for key ,value in sbm.items %}
        '{{key}}',
      {% endfor %}
```

で渡しています。
Y軸のデータを

```
{% for key ,value in sbm.items %}
        '{{value.total}}',
{% endfor %}
```

で渡しています。

Sumbycat.htmlでは

> <div class="chart_container">
> <canvas id='LineChart' style="position: relative; height:25vh; width:25vw">
> </canvas>
> </div>

で定義した線グラフを呼び出しています。

#####ランダムキャット(randcat,randcat.html)  
家計簿をつけるのに疲れた際に見るためのミニゲーム的なものを作りたいと思いましたが、現在の技術力でそれは叶わなため簡単なスクレイピングでランダムに猫の画像が表示される休憩ページを作りました。
https://qiita.com/tsuro/items/fa7bb3015feca1212732 を参考にいたしました。

```
keyword = '猫かわいい'
    urlKeyword = parse.quote(keyword)
    url = 'https://www.google.com/search?hl=jp&q=' + urlKeyword +　'&btnG=Google+Search&tbs=0&safe=off&tbm=isch'

    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0", }
    requesta = req.Request(url=url, headers=headers)
    page = req.urlopen(requesta)

    html = page.read().decode('utf-8')
    html = bs4.BeautifulSoup(html, "html.parser")
    elems = html.select('.rg_meta.notranslate')
    counter = 0
    cats = []
    for ele in elems:
        ele = ele.contents[0].replace('"', '').split(',')
        eledict = dict()
        for e in ele:
            num = e.find(':')
            eledict[e[0:num]] = e[num + 1:]
        catU = eledict['ou']
        cats.append(catU)
    i = random.randrange(len(cats)-1)
    return render(request, 'kakeibo_tuto/randcat.html', {'cat':cats[i],'keyword':keyword})
```

beatuifulsoupを使ってGoogleの画像検索結果から画像のURLを取り出します。
検索キーワードはkeywordで定義されています。ヘッダーの偽装をした上でrequestをで取り出します。
beautifulsoupでhtmlを取得、抽出したリンクをcatsリストに格納しています。
最後に乱数を使ってリストからランダムに一つURLを取り出し、randcat.htmlに渡します。

ページが読み込まれるたびにスクレイピング→リスト格納→ランダムに抽出が行われます。
連続でリロードを行うとスクレイピング→リスト格納の処理が間に合わずエラーページに飛びます。
ただ、リンクを取り出すときにリンクの末尾が.jpgや.pngかどうかの判定をしていないため、時々htmlで表示できないものが送られることがあり、改良の余地があります。
randcat.htmlページの主な機能は以下のとおりです。

```

<img src='{{cat}}'　 class="img-fluid">

<div class="alert alert-info" role="alert">{{cat}}</div>
```

src='{{cat}}'で関数から渡されたURLを読み込みimgとして表示します。画像サイズもレスポンシブデザインに対応させるために`class="img-fluid"`クラスを指定しています。これにより使用しているデバイスの横幅いっぱいに猫の画像が表示されます。



---

### 最後に

他にも    カレンダー機能などの実装をしたかったのですが叶いませんでした。今回始めてDjangoとBootstrapを扱ったので、もっと勉強を重ねて思い通りの機能とデザインのページを作ってゆきたいです。

課題については以上になります。どうぞよろしくお願い致します。



### 参考・引用

[https://qiita.com/tachibanayu24/items/b8d73cdfd4cbd42c5b1d](https://qiita.com/tachibanayu24/items/b8d73cdfd4cbd42c5b1d)

[https://qiita.com/maboy/items/bbfea777544b96b57cda](https://qiita.com/maboy/items/bbfea777544b96b57cda)

[https://note.com/shinya_hd/n/nae21691a3f84](https://note.com/shinya_hd/n/nae21691a3f84)

[https://qiita.com/felyce/items/7d0187485cad4418c073](https://qiita.com/felyce/items/7d0187485cad4418c073)

[https://cccabinet.jpn.org/bootstrap4/components/buttons](https://cccabinet.jpn.org/bootstrap4/components/buttons)

[https://codor.co.jp/django/making-login](https://codor.co.jp/django/making-login)

[https://it-engineer-lab.com/archives/544](https://it-engineer-lab.com/archives/544)




