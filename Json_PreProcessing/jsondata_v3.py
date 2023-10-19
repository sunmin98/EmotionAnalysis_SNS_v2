# *****************************************************************************
#
#	brief : 본 파일은 AI허브에서 다운로드한 SNS고도화 JSON데이터 에서 필요한 항목을 정제하기위하여
#	만들었습니다.
#	따라서 이 코드는 주어진 디렉토리에서 JSON 파일을 읽어와 특정 조건에 따라 데이터를 처리하고, 이 데이터를 CSV 파일로 저장하는 Python 프로그램입니다
#	file : jsondata_v3.py
#	date : 2023-10-16
#	autor : 김선민
#
# *****************************************************************************

import os
import json
import sys
import csv

last_list = []


# JSON 파일을 읽고 데이터 추출
def process_json_file(file_path):
	with open(file_path, "r") as f:
		json_data = json.load(f)
		topics = json_data["header"]["dialogueInfo"].get("multi_topic",
														 [json_data["header"]["dialogueInfo"]["single_topic"]])

		for topic in topics:

			# 활동성 : "문화/건강_취미/여가_문화생활"or"문화/건강_취미/여가_기타실외활동"or"문화/건강_취미/여가_스포츠"or"문화/건강_취미/여가_여행"
			# 비활동 : "문화/건강_취미/여가_독서","문화/건강_취미/여가_기타실내활동","문화/건강_건강/미용_질병/병원"
			if topic in ["문화/건강_취미/여가_문화생활" or "문화/건강_취미/여가_기타실외활동" or "문화/건강_취미/여가_스포츠" or "문화/건강_취미/여가_여행"]:
				utterance_values = [item["utterance"] for item in json_data["body"]]
				for utterance in utterance_values:
					last_list.append({"review": utterance, "label": ""})


# 진행 상황을 표시하는 프로그레스 바 출력
def display_progress_bar(iteration, total, bar_length=50):
	if total == 0:
		return
	progress = (iteration / total)
	arrow = '=' * int(round(bar_length * progress))
	spaces = ' ' * (bar_length - len(arrow))
	sys.stdout.write(f"\r[{arrow + spaces}] {int(progress * 100)}%")
	sys.stdout.flush()


# 데이터를 CSV 파일로 저장
def save_to_csv(data, output_file):
	with open(output_file, mode='w', newline='', encoding='utf-8-sig') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=["review", "label"])
		csv_writer.writeheader()
		for item in data:
			csv_writer.writerow(item)


# 디렉토리에서 JSON 파일을 찾음
def process_json_files_in_directory(root_dir):
	file_count = 0
	for (root, _, files) in os.walk(root_dir):
		for file in files:
			file_path = os.path.join(root, file)
			if file_path.endswith(".json"):
				process_json_file(file_path)
				file_count += 1
				display_progress_bar(file_count, total_file_count)

	print("\nProcessing complete!")

	# 데이터를 CSV 파일로 저장
	output_csv_file = "activate.csv"
	save_to_csv(last_list, output_csv_file)
	print(f"Data saved to {output_csv_file}")


# 주어진 디렉토리에서 JSON 파일수 카운트
def count_json_files(root_dir):
	json_count = 0
	for root, _, files in os.walk(root_dir):
		for file in files:
			if file.endswith(".json"):
				json_count += 1

	return json_count


if __name__ == "__main__":
	print("시작")
	# JSON파일 있는 폴더 경로 입력
	root_directory = "SNS_데이터_고도화"
	file_list = [f for f in os.listdir(root_directory) if f.endswith(".json")]
	total_file_count = count_json_files(root_directory)
	print(f"Total JSON files found: {total_file_count}")
	process_json_files_in_directory(root_directory)
