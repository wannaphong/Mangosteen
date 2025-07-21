# Mangosteen

Mangosteen: An Open Thai Corpus for Language Model Pretraining

We introduce Mangosteen: a 47 billion‑token Thai corpus built through a Thai-adapted Dolma pipeline that includes custom rule‑based language ID, revised C4/Gopher quality filters, and Thai‐trained content filters, plus curated non‑web sources such as Wikipedia, Royal Gazette texts, OCR‑extracted books, and CC‑licensed YouTube subtitles.

HuggingFace: [All artifacts](https://huggingface.co/collections/aisingapore/wangchanlion-v3-687a362d8f0ea2fe4077c6b3)

## Dataset
We collect datasets from various sources that can be classified into two categories: (i) Common Crawl-Derived Dataset and (ii) Curated Non-Common Crawl. We have a total of 30.1M documents and 47.4B tokens, as shown in Table

| Source                     | Documents | Tokens (B) |
|----------------------------|-----------|------------|
| Common Crawl-Derived       | 29.7M     | 45.9       |
| Curated Non-Common Crawl   | 425,304   | 1.5        |
| Total                      | 30.1M     | 47.4       |


### Common Crawl-Derived Dataset

We merged  two sources, both Common Crawl and FineWeb2 (derived from the Common Crawl dataset) Thai subsets, through our pipeline.

Read more [arXiv [wait]]

### Curated Non-Common Crawl Dataset

We have collected additional Thai text that is unlikely to be included in the common crawl from various sources. The total number of documents collected is as follows:425,304 documents, we deduplicate these Non-Common Crawl documents to later divide them into train sets for further web data and validation set.

| Dataset | Number of documents |
| --- | --- |
| all | 425,304 |
| train set | 397,488 |
| validation set | 4,044 |

**The proportion of data sources is as per the table below.**

| Domain | Source | Number of documents | Number of words |
| --- | --- | --- | --- |
| Encyclopedic | th.wikibooks.org | 1,179 | 756,175 |
|     | th.wikipedia.org | 162,189 | 74,151,797 |
|     | th.wikiquote.org | 929 | 156,910 |
|     | th.wikisource.org | 1,890 | 5,601,908 |
| Finance | airesearch/cmdf_vistec | 86,813 | 348,189,390 |
| Government Document | lift catalog data | 1   | 6,931 |
|     | data.go.th | 9,488 | 2,766,950 |
|     | envilink.go.th | 1   | 10,659 |
|     | government data catalog smart plus | 427 | 5,290,950 |
|     | Royal Gazette | 59,744 | 175,031,218 |
|     | nakhoratchasima data catalog | 1   | 68,000 |
|     | opdc data portal | 3,148 | 598,829 |
|     | open-d | 7   | 284,100 |
|     | royal thai government | 1   | 41,356 |
|     | National Economic and Social Development Board | 1   | 37,663 |
|     | pythainlp/thailand-policy-statements | 60  | 226,087 |
| Legal | pythainlp/thai-cc-license | 6   | 50,727 |
|     | pythainlp/thai-constitution-corpus | 20  | 444,313 |
|     | pythainlp/thailaw-v1.0 | 52,317 | 79,715,118 |
| Academic literature | government data catalog smart plus | 427 | 5,290,950 |
|     | openbase.in.th | 4,173 | 165,909,425 |
|     | platform for social empowerment and transformation | 90  | 209,716 |
|     | pythainlp/thai-it-books | 7   | 174,644 |
|     | pythainlp/thai-tnhc2-books | 353 | 22,002,703 |
|     | pythainlp/tlcv2.0_oa | 361 | 2,970,463 |
|     | TDRI | 25  | 2,801,106 |
|     | Bangkok Open Data | 10  | 2,334 |
|     | Open educational resources repository | 14  | 47,951 |
|     | CMU Journal of Law and Social Sciences | 47  | 37,976 |
|     | E-journal of education studies, Burapha University | 68  | 59,137 |
|     | Chulalongkorn University Law Journal | 64  | 46,425 |
|     | Lanna Journal of Health Promotion and Environmental Health | 53  | 52,320 |
|     | Journal of Educational Studies, Burapha University | 64  | 56,320 |
|     | Journal of Yanasangwon Research Institute | 65  | 47,286 |
|     | Journal of Food and Drug Administration | 79  | 115,541 |
|     | https://github.com/kongruksiamza/ebook-for-education | 8   | 83,432 |
|     | social technology institute | 3   | 11,152 |
| Youtube | youtube | 17,826 | 46,613,632 |

Documents from some sources cannot be directly used or easily processed. It is necessary to use text extraction technology (OCR) to extract the text due to the document format in PDF. The table below shows the number and proportion of documents that required OCR.

| Source | Number of documents | Number of documents required for OCR | Percentage of documents requiring OCR |
| --- | --- | --- | --- |
| [<ins>data.go.th</ins>](http://data.go.th) | 9488 | 18  | 0.189713 |
| government data catalog smart plus | 427 | 198 | 46.370023 |
| ebook construction | 8   | 8   | 100 |
| [<ins>openbase.in.th</ins>](http://openbase.in.th) | 4173 | 3443 | 82.50659 |
| [<ins>opendata.nesdc.go.th</ins>](http://opendata.nesdc.go.th) | 7   | 3   | 42.857143 |
| royal thai government | 1   | 1   | 100 |
| Open educational resources repository | 14  | 2   | 14.285714 |

The model used for text extraction is https://github.com/VikParuchuri/marker

In the future, you should try VLM, such as: https://olmocr.allenai.org/ and [Typhoon OCR](https://opentyphoon.ai/blog/en/typhoon-ocr-release).

Data from various sources can be classified into 6 types as shown in the table below.

| Domain | Count | Proportion |
| --- | --- | --- |
| Encyclopedic | 166187 | 41.34 |
| Finance | 86813 | 21.59 |
| Government | 72,879 | 18.13 |
| Legal | 52,343 | 13.02 |
| YouTube | 17,837 | 4.43 |
| Education | 5,911 | 1.47 |

The additional documents we collect are confirmed to be open source and have a license to allow for redistribution, with the copyright share as shown in the table below.

| License | Count | Proportion |
| --- | --- | --- |
| CC BY-SA 4.0 | 166,187 | 41.388233 |
| CC0 | 112,871 | 28.110088 |
| CC BY 4.0 | 112,407 | 27.994531 |
| CC BY-NC-SA 4.0 | 4,173 | 1.03927 |
| ODC-BY | 3,769 | 0.938655 |
| CC BY-NC 4.0 | 1,853 | 0.461483 |
| CC BY-NC-ND 4.0 | 250 | 0.062262 |
| CC BY 3.0 | 13  | 0.003238 |
| GFDL | 6   | 0.001494 |
| OGL | 3   | 0.000747 |

&nbsp;

The dataset format will be in jsonl format and will have the following fields:

| Field name | Description |
| --- | --- |
| id  | A unique ID for identifying a row of data in the format nonweb_x, where x is the row number. |
| text | The content of the document |
| source | Sources of information |
| metadata | Information about the document, such as the download url and copyright type.  <br><br/>For example  <br><br/>{  <br>“license”: ….  <br>} |

All in all, this gives us a total of 1,539,257,705 tokens, including the meta-llama/Llama-3.2-1B tokenizer.

**List of YouTube keywords:**

```
การรักษาโรค
ภาษาอังกฤษ
การบริหารธุรกิจ
การวิเคราะห์ข้อมูล
สถาปัตยกรรม
การออกแบบกราฟิก
การซ่อมแซมบ้าน
โยคะ
อุตสหกรรม
การพัฒนาตนเอง
มหาวิทยาลัย
ภาษาไทย
การลงทุน
สุขภาพจิต
การวางแผนชีวิต
การสอนออนไลน์
การโรงแรม
พลศึกษา
ข้อมูลขนาดใหญ่
เทคโนโลยี
อนิเมะ
ภาพยนตร์
วัฒนธรรม
การใช้ชีวิต
การทำสวน
สังคมศาสตร์
การเมือง
จิตวิทยา
การเขียนนิยาย
การถ่ายภาพ
เคมี
การพยาบาล
การเรียนรู้ของเครื่อง
งานฝีมือ
การเขียนโค้ด
ปัญญาประดิษฐ์
สาธารณสุข
ชีววิทยา
มังสวิรัติ
เพลงไทย
คอมพิวเตอร์
สิ่งแวดล้อม
ฟิสิกส์
กฎหมาย
การเกษตร
สุขศึกษา
เศรษฐศาสตร์
การทำอาหาร
การออกแบบภายใน
การเรียนภาษาใหม่
การเดินทางท่องเที่ยว
วิศวกรรมศาสตร์
ดาราศาสตร์
ประวัติศาสตร์
หุ่นยนต์
ดนตรี
การเงิน
การจัดการเวลา
การแพทย์
การออกกำลังกาย
การงานอาชีพ
ทรัพยากรธรรมชาติ
การประมง
การเขียนโปรแกรม
การศึกษา
การเงินส่วนบุคคลเกมออนไลน์
การท่องเที่ยว
กีฬา
คณิตศาสตร์
```