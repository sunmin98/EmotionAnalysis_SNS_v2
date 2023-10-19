# EmotionAnalysis_SNS_v2

SNS_데이터_고도화/02.라벨링데이터/SAMPLE_JSON_DATA는 AI-HUB에서 다운받은 원본 Json파일입니다, Json파일에서 추출한 csv파일은 용량문제로 카카오워크에 업로드 하였습니다. 

IMSTA_PACKAGE폴더는 인스타 크롤링 할때 사용하는 패키지 "Instaloader"를 제가 직접 수정하였기 때문에 따로 구별하였습니다.

Json_PreProcessing폴더는 Json파일에서 원하는 텍스트 문구를 추출하여 csv로 저장하는 "jsondata_v3.py"와 그 csv를 라벨링하고 데이터수를 조정하는 파일 "csv_labeling.ipynb"입니다.

"Determining_Activity.ipynb"는 csv를 학습학고 예측하는 활동,비활동 감정분석 파일입니다.

"Sns_crawling.py,Sns_crawling.ipynb" 인스타 게시물을 크롤링 하는 파일입니다 하지만 현재 수정사항이 생겨 작동하지는 않고있습니다.
