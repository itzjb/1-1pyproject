import tkinter as tk
from tkinter import messagebox, simpledialog

#GUI
#프로그램 실행 시 할 일 목록을 저장할 파일이 없으면 새로 생성
try:
    with open("todo.txt", "x") as f:
        pass
except FileExistsError:
    pass


# 할 일 추가 함수
def add_task():
    # 날짜 입력 받기
    date = simpledialog.askstring("날짜 입력", "날짜를 입력하세요")
    if not date:  # 입력이 없으면 함수 종료
        return

    # 할 일 내용 입력 받기
    task = simpledialog.askstring("할 일 입력", "할 일을 입력하세요")
    if not task:  # 입력이 없으면 함수 종료
        return

    # 중요도 입력 받기 (1~5 사이의 정수)
    imp = simpledialog.askinteger("중요도 입력", "중요도를 입력하세요 (1(중요하지 않음)-5(가장 중요))", minvalue=1, maxvalue=5)
    if not imp:  # 입력이 없으면 함수 종료
        return

    # 주제 선택 (개인, 업무, 기타)
    categories = {"개인", "업무", "기타"}
    category = simpledialog.askstring("주제 선택", "주제를 선택하세요 \n개인, 업무, 기타")
    while category not in categories:  # 올바른 주제가 입력될 때까지 반복
        category = simpledialog.askstring("주제 선택", "올바른 주제를 선택하세요:\n개인, 업무, 기타")

    # 입력받은 데이터를 파일에 저장
    with open("todo.txt", "a") as f:
        f.write(f"{category} : {date} : {task} : {imp}\n")

    # 파일 내용을 정렬 (주제별, 중요도 순)
    with open("todo.txt", "r") as f:
        lines = f.readlines()
    sorted_lines = sorted(lines, key=lambda x: (x.strip().split(" : ")[0], int(x.strip().split(" : ")[3])))
    with open("todo.txt", "w") as f:
        f.writelines(sorted_lines)

    # 추가 완료 메시지 표시
    messagebox.showinfo("추가 완료", f"'{category} : {date} : {task}'이(가) 추가되었습니다.")


# 할 일 목록 보기 함수
def view_tasks():
    try:
        # 파일에서 할 일 목록 읽기
        with open("todo.txt", "r") as f:
            lines = f.readlines()
        if not lines:  # 파일이 비어 있으면 메시지 표시
            messagebox.showinfo("할 일 목록", "할 일이 없습니다.")
            return

        # 할 일 목록을 문자열로 변환하여 표시
        tasks = "분류 : 날짜 : 할 일 : 중요도\n" + "=" * 20 + "\n" + "".join(lines)
        messagebox.showinfo("할 일 목록", tasks)
    except FileNotFoundError:  # 파일이 없을 경우 메시지 표시
        messagebox.showinfo("할 일 목록", "할 일이 없습니다.")


# 할 일 삭제 함수
def delete_task():
    try:
        # 파일에서 할 일 목록 읽기
        with open("todo.txt", "r") as f:
            lines = f.readlines()
        if not lines:  # 파일이 비어 있으면 메시지 표시
            messagebox.showinfo("삭제", "할 일이 없습니다.")
            return

        updated_lines = []  # 삭제되지 않은 할 일을 저장할 리스트
        for line in lines:
            # 각 줄을 분류, 날짜, 할 일, 중요도로 분리
            category, date, task, imp = line.strip().split(" : ")
            # 삭제 여부를 사용자에게 확인
            delete = messagebox.askyesno("삭제 확인", f"'{category}' 중 {date}의 '{task}'을(를) 삭제하시겠습니까? (중요도 {imp})")
            if not delete:  # 삭제하지 않을 경우 리스트에 추가
                updated_lines.append(line)

        # 업데이트된 할 일 목록을 파일에 저장
        with open("todo.txt", "w") as f:
            f.writelines(updated_lines)

        # 삭제 완료 메시지 표시
        messagebox.showinfo("삭제 완료", "선택한 할 일이 삭제되었습니다.")
    except FileNotFoundError:  # 파일이 없을 경우 메시지 표시
        messagebox.showinfo("삭제", "할 일이 없습니다.")

# 프로그램 종료 함수
def exit_program():
    # GUI 창 닫기
    root.destroy()

# GUI 설정
root = tk.Tk()
root.title("TODO LIST")  # 프로그램 제목 설정

# 버튼을 담을 프레임 생성
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# 할 일 추가 버튼
btn_add = tk.Button(frame, text="할 일 추가", command=add_task, width=20)
btn_add.grid(row=0, column=0, pady=5)

# 할 일 목록 보기 버튼
btn_view = tk.Button(frame, text="할 일 목록 보기", command=view_tasks, width=20)
btn_view.grid(row=1, column=0, pady=5)

# 할 일 삭제 버튼
btn_delete = tk.Button(frame, text="할 일 삭제", command=delete_task, width=20)
btn_delete.grid(row=2, column=0, pady=5)

# 종료 버튼
btn_exit = tk.Button(frame, text="종료", command=exit_program, width=20)
btn_exit.grid(row=3, column=0, pady=5)

# GUI 이벤트 루프 시작
root.mainloop()
