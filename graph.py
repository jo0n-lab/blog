import matplotlib.pyplot as plt
import numpy as np

# 폰트 설정
plt.rcParams['font.family'] = 'Apple SD Gothic Neo'  # 폰트가 없을 경우 시스템 기본 폰트 사용

# 데이터
labels = ['Python', 'C/C++', 'Kotlin']

values_max = [24, 30, 8]
values_step = [0, 0, 0]
n_step=10
diff=max(values_max)/n_step

width = 0.4

# 막대그래프 생성
color = "#B9B9F7"

for step in range(n_step):
    graph_path='./static/images/bar_'+str(step)
    plt.clf()

    for i in range(3):
        cur_val=values_step[i]
        cur_max=values_max[i]
        if cur_val+diff>cur_max:
            values_step[i]=cur_max
        else:
            values_step[i]+=diff

    plt.figure(figsize=(3, 4.5))         
    plt.bar(labels, values_step, width=width, color=color)

    # 그리드 켜기
    plt.grid(True, axis='both', linestyle='--', alpha=0.7)

    # 그래프 제목 및 축 레이블 설정 (폰트 크기 조정)
    plt.title('Programming Language', fontsize=16)
    plt.xlabel('Language', fontsize=14)
    plt.ylabel('Months', fontsize=14)

    plt.ylim(0, 32)  # y축 0~30으로 고정
    plt.xlim(-0.5, 2.5)  # x축 레이블 갯수에 맞게 고정

    plt.tight_layout()
    plt.savefig(graph_path)



labels = ['PM' , 'AI','Embedded','Systems', 'Research', 'Mathematics']
values_max = [8, 9, 9, 8, 7, 7]
values_step = [0, 0, 0, 0, 0, 0]
n_step=50
diff=max(values_max)/n_step

# 각도 계산


for step in range(n_step):
    graph_path='./static/images/hex_'+str(step)
    plt.clf()

    for i in range(6):
        cur_val=values_step[i]
        cur_max=values_max[i]
        if cur_val+diff>cur_max:
            values_step[i]=cur_max
        else:
            values_step[i]+=diff

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    # color="#78ACFF"
    color="#0096FF"

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # 차트 데이터 그리기
    ax.fill(angles, values_step+values_step[:1], color='blue', alpha=0.25)
    ax.plot(angles, values_step+values_step[:1], color='blue', linewidth=2)

    # 레이블 추가 (폰트 크기 설정)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=18)  # 폰트 크기 14로 설정

    # 축 값 범위 설정
    ax.set_yticklabels([])

    # 제목 추가 (폰트 크기 설정)
    plt.title('Developer Skills', size=25, color='black', y=1.1)

    ax.set_ylim(0, 10)  # y축 범위를 0에서 최대값으로 고정

    print(values_step)

    plt.tight_layout()
    plt.savefig(graph_path)




