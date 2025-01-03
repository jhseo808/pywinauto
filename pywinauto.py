from pywinauto import findwindows
from pywinauto import application

# 현재 윈도우 화면에 있는 프로세스 목록 리스트를 반환
# 리스트의 각 요소는 element 객체로 프로세스 id, 핸들값, 이름 등의 정보 보유  
#procs = findwindows.find_elements()
#
#for proc in procs:
#    print(f"{proc} / 프로세스 : {proc.process_id}")

app = application.Application(backend='uia')

# 프로세스 경로
app.start("C:\\Program Files (x86)\\Notepad++\\Notepad++.exe")

# 컨트롤 요소 출력
dlg = app['Notepad++'] # 변수에 노트패드 윈도우 어플리케이션 객체를 할당
dlg['파일(F)'].select()
dlg.print_control_identifiers() # 노트패드의 컨트롤 요소를 트리로 모두 출력

#dlg['최대화Button'].click()
