
import os
#import s_Module #호출 : s_Module.Avg_()
from Student_Module import* #호출 : Avg_()
QUIT = 8


def main():
    choice = 0

    while choice != QUIT:
        
        choice = get_menu_choice()


        if choice == 1:
            Add()
        elif choice == 2:
            Search_Total()
        elif choice == 3:
            Search()
        elif choice == 4:
            Search_Grade()              
        elif choice == 5:
            Update()
        elif choice == 6:
            Delete()
        elif choice == 7:
            Delete_Total()   

def Search_Grade():
    #성적 검색
    #성적에 대하여 평가부분을 함수로 계산한 후
    #입력받은 평가에 해당하는 학생들의 자료를 출력
    
    print()


def get_menu_choice():
    print()
    
    print('---------------------------')
    print('학생 성적 관리  시스템')
    print('---------------------------')
    print('1. 성적 등록')
    print('2. 성적 출력')
    print('3. 이름 검색')
    print('4. 성적 검색')
    print('5. 정보 수정')
    print('6. 정보 삭제(개별)')
    print('7. 정보 삭제(전체)')
    print('8. 종료')
    print()

    choice = int(input('선택 >> '))

    while choice < 1 or choice > QUIT:
        choice = int(input('메뉴 번호를 확인해주세요: '))

    return choice


def Add():
    another = 'Y'
    while another == 'y' or another == 'Y':
        found = False

        search = input('학생의 이름을 입력하세요.: ')
        
        student_file_write = open ('student.txt', 'a')
        student_file = open('student.txt', 'r')
        st_name = student_file.readline()
        
        while st_name != '':
            line_kor = float(student_file.readline())
            line_math = float(student_file.readline())
            line_eng = float(student_file.readline())

            st_name = st_name.rstrip('\n')
            
            

            if st_name == search:
                print('학생이 이미 자료에 있습니다.')
                found = True
            st_name = student_file.readline()
        if found == False:
            subj1 = int(input('국어 점수 : '))
            subj2 = int(input('수학 점수 : '))
            subj3=  int(input('영어 점수 : '))

            student_file_write.write(search + '\n')
            student_file_write.write(str(subj1) + '\n')
            student_file_write.write(str(subj2) + '\n')
            student_file_write.write(str(subj3) + '\n')
            print('student.txt에 기록을 완료하였습니다.')
            
            print('추가할 자료가 더 있습니까?')
            another = input('Y = yes, anything else = no: ')

        student_file.close()
        student_file_write.close()
    
def Search_Total():
    student_file = open('student.txt', 'r')

    name = student_file.readline()  

    print( format('이름:','7s' ),
           format('국어:','>12s') , 
           format('영어:','>9s') , 
           format('수학:','>9s'),
           format('평균:','>10s'),
           format('평가:','>9s'),sep= ' ')
    print('--------------------------------------------------------------------------')
    subj1_list = []
    subj2_list = []
    subj3_list = []
    total_student = 0
    while name != '': 
        subj1 = float(student_file.readline())
        subj1_list.append(subj1)
        subj2 = float(student_file.readline())
        subj2_list.append(subj2)
        subj3 = float(student_file.readline())
        subj3_list.append(subj3)
        name = name.rstrip('\n')
        total_student += 1
        avg=Avg_(subj1,subj2,subj3)
        grade=Grade(avg)
        print( format(name,'10s' ),
               format( subj1,'>10.2f') , 
               format( subj2,'>10.2f') , 
               format( subj3,'>10.2f') ,
               format( avg,'>10.2f'),
               '   ',
               format(grade)
               , sep= '  ')
 

        name = student_file.readline()
    print('--------------------------------------------------------------------------')
    if total_student != 0 :
        print( format('최고점수','15s' ),
               format(Find_max(subj1_list),'.2f'),'  ', 
               format(Find_max(subj2_list),'.2f'),'   ', 
               format(Find_max(subj3_list),'.2f'),'   ', 
               sep= ' ')
        print( format('최저점수','15s' ),
               format(Find_min(subj1_list),'.2f'), '     ', 
               format(Find_min(subj2_list),'.2f'), '     ', 
               format(Find_min(subj3_list),'.2f'), '     ', 
               sep= ' ')
    print( format('총인원 : ','5s' ),total_student)
    
    student_file.close()

    
def Search():
    found = False

    search = input('찾을 학생의 이름을 입력하세요.: ')
    student_file = open('student.txt', 'r')
    st_name = student_file.readline()

    while st_name != '':
        line_kor = float(student_file.readline())
        line_math = float(student_file.readline())
        line_eng = float(student_file.readline())

        st_name = st_name.rstrip('\n')

        if st_name == search:
            print('이름:', format(st_name,'5s' ),
              '국어:',format( line_kor,'>4.1f') ,'수학:',format( line_math,'>4.1f'),'영어:',format( line_kor,'>4.1f') ,sep= '  ' )
            print()
            found = True

        st_name = student_file.readline()

    student_file.close()

    if not found:
        print('찾는 학생이 자료에 없습니다...')
    
def Update():
    found = False

    search = input('수정할  학생의 이름을 입력하세요.: ')
    new_kor = int(input('새로운 국어 점수는?: '))
    new_math = int(input('새로운 수학 점수는?: '))
    new_eng = int(input('새로운 영어 점수는?: '))

    student_file = open('student.txt', 'r')
    temp_file = open('temp.txt', 'w')
    descr = student_file.readline()

    while descr != '':
        kor = float(student_file.readline())
        math = float(student_file.readline())
        eng = float(student_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:
            temp_file.write(descr + '\n')
            temp_file.write(str(new_kor) + '\n')
            temp_file.write(str(new_math) + '\n')
            temp_file.write(str(new_eng) + '\n')

            found = True
        else:
            temp_file.write(descr + '\n')
            temp_file.write(str(kor) + '\n')
            temp_file.write(str(math) + '\n')
            temp_file.write(str(eng) + '\n')
        descr = student_file.readline()

    student_file.close()
    temp_file.close()

    os.remove('student.txt')
    os.rename('temp.txt', 'student.txt')

    if found:
        print('파일을 수정하였습니다.')
    else:
        print('찾는 학생은 자료에 없습니다....')

    
def Delete():
    found = False

    search = input('삭제하고자 하는 학생은?')

    student_file = open('student.txt', 'r')
    temp_file = open('temp.txt', 'w')

    name = student_file.readline()

    while name != '':
        subj1 = float(student_file.readline())
        subj2 = float(student_file.readline())
        subj3= float(student_file.readline())
        name = name.rstrip('\n')

        if name != search:  

            
            temp_file.write(name + '\n')
            temp_file.write(str(subj1) + '\n')
            temp_file.write(str(subj2) + '\n')
            temp_file.write(str(subj3) + '\n')

            found = True

        name = student_file.readline()

    student_file.close()
    temp_file.close()

    os.remove('student.txt')
    os.rename('temp.txt', 'student.txt')
 

    if found:
        print('파일을 삭제하였습니다.')
    else:
        print('찾는 학생이  자료에 없습니다....')


def Delete_Total():
    os.remove('student.txt')
    std_file = open('student.txt', 'w')
    std_file.close()

def Search_Grade():
    search = input('검색할 평점을 입력 하세요: ')
    student_file = open('student.txt', 'r')
    name = student_file.readline()
    #빈 리스트 작성
    name_list = []
    subj1_list= []
    subj2_list = []
    subj3_list =[]
    avg_list = []
    grade_list =[]
    #파일을 읽어서 리스트를 채움
    while name != '':
        subj1 = float(student_file.readline())
        subj1_list.append(subj1)
        subj2 = float(student_file.readline())
        subj2_list.append(subj2)
        subj3= float(student_file.readline())
        subj3_list.append(subj3)

        avg_list.append(Avg_(subj1,subj2,subj3))
        grade_list.append(Grade(Avg_(subj1,subj2,subj3)))
        
        name = name.rstrip('\n')
        name_list.append(name)
        name = student_file.readline()

    student_file.close()
    print( format('이름:','7s' ),
    format('국어:','>12s') , 
    format('영어:','>9s') , 
    format('수학:','>9s'),
    format('평균:','>10s'),
    format('평가:','>9s'),sep= ' ')
    print('--------------------------------------------------------------------------')    
    n=0
    student_total = 0
    #찾는 내용과 같은 내용이 평점 리스트에 있는경우 이름,점수,평균 리스트에서 값을 불러옴
    for k in grade_list:
        
        if search == k:
            student_total += 1
            print( format(name_list[n],'10s' ),
               format( subj1_list[n],'>10.2f') , 
               format( subj2_list[n],'>10.2f') , 
               format( subj3_list[n],'>10.2f') ,
               format( avg_list[n],'>10.2f'),
               '   ',
               format(grade_list[n])
               , sep= '  ')
            
        n += 1
    print('')
    print('인원수 : ', student_total)
    
main()
