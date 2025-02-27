## 「Introduction to Python」（Python入門）コースの「説明」を日本語に翻訳しました:

### 説明:

表示される説明は英語です。  
日本人が Python を学びやすいように、日本語に翻訳しました。

---

### セットアップ手順:


#### 1. 「PyCharm」に下記のプラグインをインストールしておきます:

- 「Edu Tools」  
- 「Japanese Language Pack」


#### 2. 「PyCharm」の「Courses」タブで「Introduction to Python」コースを選択し、「Start」をクリックします:

→「~/PycharmProjects/'Introduction to Python'/」フォルダが作成されます。

これはすでに行われているはずです。

#### 3. 念のため、元のファイルを保存してください:

```
$ cp -r ~/PycharmProjects ~/PycharmProjects-ORG
```

#### 4. 作業に使用するファイルを確認します:

次のフォルダに添付ファイルがあるとします:

```
$ cd ~/PycharmProjects/'Introduction to Python'/Translations/
$ ls -1
Delete-md-File.sh
README-ja.md
README.md
ja.patch
screenshot-ja.jpg
```

#### 5. シェルスクリプトを実行可能に設定します:

```
$ chmod +x ./Delete-md-File.sh
```

#### 6. 対象となるファイルを削除するシェルスクリプトを実行します:

```
$ cd ~/PycharmProjects/'Introduction to Python'/
$ ./Translations/Delete-md-File.sh
```

→パッチファイルを適用する際の以下のエラーを回避します:  
"Hunk #1 FAILED at 1 (different line endings)."

および、新しいファイルにすることで、パッチを適用しやすくします。

#### 7. パッチファイルを適用します:

```
$ patch -p1 <Translations/ja.patch
```

→新しいmdファイルが各ファイル階層に作成されます。

---

### 添付ファイル:

(1). 「README.md」 : セットアップ手順。このファイル。  
(2). 「README-ja.md」 : セットアップ手順（日本語版）  
(3). 「screenshot-ja.jpg」 : 「Introduction to Python」を日本語に翻訳した画面  
(4). 「Delete-md-File.sh」  : 対象となるファイルを事前に削除するシェルスクリプト  
(5). 「ja.patch」  : パッチファイル
