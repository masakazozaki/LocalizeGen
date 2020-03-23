import sys, csv, urllib.request, ssl, os

args = sys.argv

if len(args) < 4:
    raise Exception("引数にPlatform、GoogleSpreadSheetId、出力パスを指定する必要があります")

#Google Spread SheetからCSVの取得
ssl._create_default_https_context = ssl._create_unverified_context #SSL証明書エラーの回避
url = 'https://docs.google.com/spreadsheets/d/{}/export?format=csv'.format(args[2])
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read().decode('utf-8')

#CSVのパース
csvData = csv.reader(body.strip().splitlines())
header = next(csvData) #タイトル行の読み飛ばし
dataList = [ e for e in csvData ]


#Android用メソッド
def generateAndroid(fileName):
    with open(dirName + '/strings.xml', 'w') as f:
        print('<?xml version="1.0" encoding="UTF-8"?>\n<resources>',file=f)
        print('\t<string name="app_name">{}</string>'.format(args[4]), file=f)
        for j in range(len(dataList)):
            print('\t<string name=\"{}\">{}</string>'.format(dataList[j][1],dataList[j][i]),file=f)
        print('</resources>',file=f)

#ファイルを作る
for i in range(2,len(header)):
    if args[1] == "ios":
        folderName = header[i]+".lproj"
        dirName = args[3] + folderName
        os.makedirs(dirName, exist_ok=True)
        with open(dirName + '/Localizable.strings', 'w') as f:
            for j in range(len(dataList)):
                print('\"{}\" = \"{}\";'.format(dataList[j][1],dataList[j][i]),file=f)

    elif args[1] == "android":
        folderName = "values-" + header[i]
        dirName = args[3] + folderName
        os.makedirs(dirName, exist_ok=True)
        generateAndroid(folderName)

if args[1] == "ios":
    folderName = "Base.lproj"
    dirName = args[3] + folderName
    os.makedirs(dirName, exist_ok=True)
    with open(dirName + '/Localizable.strings', 'w') as f:
        for j in range(len(dataList)):
            print('\"{}\" = \"{}\";'.format(dataList[j][1],dataList[j][i]),file=f)
elif args[1] == "android":
    folderName = "values"
    dirName = args[3] + folderName
    os.makedirs(dirName, exist_ok=True)
    generateAndroid(folderName)
