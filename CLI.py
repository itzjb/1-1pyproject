# CUI
# todo.txt 파일이 없으면 생성
try:
    f = open("todo.txt", "x") # 파일이 없으면 생성
    f.close()
except FileExistsError:
    pass # 파일이 이미 존재하면 아무 작업도 하지 않음


while 1:
    try :
        z = int(input("1 : 할 일 추가\n2 : 할 일 목록 보기\n3 : 할 일 삭제\n4 : 종료\n번호 입력 : "))
    except ValueError: # 잘못된 입력 처리
        print("-" * 10)
        print(f"{"-" * 10}\n잘못된 입력입니다. 다시 입력하세요.\n{"-" * 10}")
        print("-" * 10)
        continue
    if z == 1: # 할 일 추가
        print("-" * 10)
        date = input("날짜 입력 : ")
        task = input("할 일 입력 : ")

        imp = input("중요도 입력 (1-5): ")
        # 중요도 입력값이 1-5 범위인지 확인
        while (not imp.isdigit()) or (not (1 <= int(imp) <= 5)):
            print("*중요도는 1에서 5 사이의 숫자여야 합니다.*")
            imp = input("중요도 입력 (1-5): ")
        
        cont = input("주제 선택 : \n1. 개인\n2. 업무\n3. 기타\n번호 입력 : ")
        # 주제 입력값이 1-3 범위인지 확인
        categories = {"1": "개인", "2": "업무", "3": "기타"}
        while cont not in categories:
            print("*올바른 주제를 선택하세요.*")
            cont = input("주제 선택 :\n1. 개인\n2. 업무\n3. 기타\n번호 입력 : ")
        category = categories[cont]

        # 중요도 입력값이 1-5 범위인지 확인
        while (not imp.isdigit()) or (not (1 <= int(imp) <= 5)):
            print("*중요도는 1에서 5 사이의 숫자여야 합니다.*")
            imp = input("중요도 입력 (1-5): ")


        # 파일에 추가
        f = open("todo.txt", "a")
        f.write(f"{category} : {date} : {task} : {imp}\n")
        print(f"'{category} : {date} : {task}'이(가) 추가되었습니다.")
        f.close()
        print("-" * 10)

        # 주제와 중요도에 따라 정렬
        with open("todo.txt", "r") as f: 
            lines = f.readlines()
        sorted_lines = sorted(lines, key=lambda x: (x.strip().split(" : ")[0], int(x.strip().split(" : ")[3]))) # 주제와 중요도 기준으로 정렬
        with open("todo.txt", "w") as f:
            f.writelines(sorted_lines)


    elif z == 2: # 할 일 목록 보기
        f = open("todo.txt", "r")
        print("-" * 10)
        
        line = f.readline()
        if not line: # 파일이 비어있으면 
            print("할 일이 없습니다.")
            print("-" * 10)
            f.close()
            continue

        while 1: # 파일에서 한 줄씩 읽어오기
            print("분류 : 날짜 : 할 일 : 중요도")
            print("=" * 25)
            print(line.strip()) #위에서 읽은 첫 줄 출력
            line = f.readline() # 다음 줄 읽기
            if not line: # 더 이상 읽을 줄이 없으면
                break
            print(line.strip())
        print("-" * 10)
        f.close()


    elif z == 3: # 할 일 삭제
        f = open("todo.txt", "r")
        lines = f.readlines()
        if lines == []: # 파일이 비어있으면
            print(f"{"-" * 10}\n할 일이 없습니다.\n{"-" * 10}")
        f.close()

        updated_lines = [] # 수정된 할 일 목록을 저장할 리스트
        for line in lines:
            cont, date, task, imp = line.strip().split(" : ")
            delete = input(f"{"-"*10}\n'{cont}' 중 {date}의 '{task}'을(를) 마쳤나요? (중요도 {imp}) (y/n): ")
            if delete.lower() == 'y':
                print(f"{date}의 '{task}'을(를) 삭제합니다.\n{"-"*10}") # updated_lines 리스트에 추가하지 않음
            else:
                print(f"{date}의 '{task}'은(는) 유지합니다.\n{"-"*10}") # updated_lines 리스트에 추가
                updated_lines.append(line)
        f = open("todo.txt", "w")
        f.writelines(updated_lines) # 수정된 할 일 목록을 파일에 저장
        f.close()


    elif z == 4: # 종료
        print(f"{"-" * 10}\n프로그램을 종료합니다.\n{"-" * 10}")
        break

    else: # 잘못된 입력 처리
        print(f"{"-" * 10}\n잘못된 번호입니다. 다시 입력하세요.\n{"-" * 10}")
