# Rest-API-Random-Forest

End Point<nbsp>: <code>http://dzvlfi.pythonanywhere.com/predicts</code><br>
Method<nbsp>: <code>.POST</code> </br>
Headers: <code>"Content-Type": application/json</code><br>
Body: `Raw`<br>
Dengan format seperti pada dibawah
> [{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1}]
  
Keterangan:<br>
| Key       | Keterangan      |   |
|-----------|-----------------|---|
| LIMIT_BAL | Batasan balance |   |
| EDUCATION | Pendidikan      |   |
| SEX       | Jenis Kelamin   |   |
| AGE       |                 |   |
| PAY_1     |                 |   |
| PAY_2     |                 |   |
| PAY_3     |                 |   |
<br>
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
