# Rest-API-Random-Forest

**Daftar Isi**<br>
1. [Skema Rest-API](#skema)
2. [Detail penggunaan REST-API](#detail)
3. [Pengaplikasian](#pengaplikasian)<br>
3.1. [Python](#python)<br>
3.2. [Postman](#postman)<br>
3.2.1. [Headers](#headers)<br>
3.2.2. [Body](#body)<br>

# 1. Skema Rest-API<a name="skema"></a>
Skema yang digunakan pada pembangunan REST-API sebagai berikut:<br>
![skema](https://raw.githubusercontent.com/nurlailiis/Analytics-Model-Developments/master/image/Simple%20Data%20Flow.PNG)

# 2. Detail penggunaan REST-API<a name="detail"></a>
End Point<nbsp>: <code>http://dzvlfi.pythonanywhere.com/predicts</code><br>
Method<nbsp>: <code>.POST</code> <br>
Headers: <code>"Content-Type": application/json</code><br>
Body: `Raw`<br>
Dengan format sebagai berikut
a. Prediksi 1 data<br>
> [{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1}]<br>
b. Prediksi n data<br>
> [{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1},<br>
{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1},<br>
{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1},<br>
{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1},<br>
...]<br>

**Keterangan:**<br>
LIMIT_BAL = Batas maksimum kredit (30000 berarti Rp 30000)<br>
EDUCATION = Pendidikan terakhir calon pelanggan (1: S2/S3, 2: S1, 3: SMA, 4: Lainnya)<br>
SEX = Jenis kelamin calon pelanggan (1: Pria, 2: Wanita)<br>
AGE = Umur peminjam<br>
PAY_1 = Tenur 1 pembayaran (0: Tepat waktu, 1: Tidak tepat waktu)<br>
PAY_2 = Tenur 3 pembayaran (0: Tepat waktu, 1: Tidak tepat waktu)<br>
PAY_3 = Tenur 3 pembayaran (0: Tepat waktu, 1: Tidak tepat waktu)<br>

# 3. Pengaplikasian<a name="pengaplikasian"></a>
Pengaplikasian pada REST-API bisa pada berbagai platform, dari mulai *python*, *website*, *mobile apps*, dan lain-lain. Pada kali ini hanya menggunakan Python dan Postman saja untuk penggunaannya.<br>

## 3.1. Python.<a name="python"></a>
Pada python, request yang dibuat cukup mudah dan sederhana. Contoh *code*-nya bisa dilihat pada [request.py](https://github.com/dzvlfi/Rest-API-Random-Forest/blob/master/Code/request.py) atau sebagai berikut:<br>
``import requests``
``url = 'http://dzvlfi.pythonanywhere.com/predicts'``

``r = requests.post(url,json=[{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1}])``
``print(r.json())``

## 3.2. [Postman](https://www.getpostman.com/).<a name="postman"></a>
Jika di postman, kita hanya perlu membuat *request* yang lalu me-*set* *method*-nya menjadi ``POST``. Setelah method berubah menjadi post, kita tambahkan value headernya dengan *key* ``Content-Type`` dan *value* ``application/json``, lalu kita beralih pada tab body dan pilih ``raw``, dan isikan body kita seperti pada contoh berikut:

  ### 3.2.1. Headers<a name="headers"></a>
  ![Header](https://raw.githubusercontent.com/dzvlfi/Rest-API-Random-Forest/master/image/headers.PNG)
     Detail pada pengisian key dan value pada Headers.
     
  ### 3.2.1. Body<a name="body"></a>
  ![Body](https://raw.githubusercontent.com/dzvlfi/Rest-API-Random-Forest/master/image/body.PNG)
     Detail pada pengisian body.
     
<a name="author"></a>
### Author
``Dzulfiqar Ridha, Astra Data Scientist Bootcamp 2019.``<br>
``Dzulfiqar.Ridha@ai.astra.co.id``
