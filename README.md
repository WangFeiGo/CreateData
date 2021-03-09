**追加功能记录：**

2021年03月09号
    添加pdf转picture的公共方法
        CreateData\common\Pdf2Picture.py
    添加pdf转picture的业务方法
        CreateData\read_document\Pdf2Picture.py
    添加pdf转word的公共方法
        CreateData\common\Pdf2Word.py
    添加pdf转word的业务方法
        CreateData\read_document\Pdf2Word.py
    添加获取百度文库下载链接的utils
        CreateData\utils\GetBaiDuDownloadUrl\GetBaiDuDownloadUrl.py
        
2021年03月04号 
    添加代码，可以把word中的文字提取出来，做来比对       
        CreateData\read_document\CreateReadDocumentData.py

2021年02月04号
    添加文件上传到ftp的公共方法
        CreateData\common\FtpToFile.py
    添加word上传到ftp的业务方法
        CreateData\read_document\UploadDocToFtp.py
    添加pdf上传到ftp的业务方法
        CreateData\read_document\UploadPdfToFtp.py
    添加爬虫工具，采集百度图库的图片
        CreateData\utils\CrawlerPictures.py

2020年12月28号
    添加执行pgsql的脚本
        CreateData\common\ExcutePGSQL.py
    添加制造大量数据的脚本，100s约50万数据
        DCreateData\insert_more_datas\InsertMoreDatas.py
            
2020年12月17号
    添加word转pdf的公共方法
        CreateData\common\Word2Pdf.py